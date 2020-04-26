from datetime import datetime, timezone
from uuid import uuid4

from fastapi import Depends, FastAPI
from starlette import status

from collector.db import get_db, t_news_draft
from collector.schema import VerificationRequestSchema
from collector.services import RecaptchaService
from collector.storage import get_bucket, get_file_url

app = FastAPI()


@app.get("/")
def health_check() -> None:
    return


@app.post("/verification-request", status_code=status.HTTP_201_CREATED)
def create_verification_request(
    payload: VerificationRequestSchema = Depends(),
    db=Depends(get_db),
    bucket=Depends(get_bucket),
    recaptcha_service: RecaptchaService = Depends(),
):
    recaptcha_service.verify_response(payload.recaptcha)

    image_name = f"{str(uuid4())}.jpg"
    news_draft = dict(
        id=str(uuid4()).replace("-", ""),
        reporter_email=payload.email,
        comment=payload.comment,
        url=payload.url,
        text=payload.text,
        screenshot_url=get_file_url(bucket, image_name),
        reported_at=datetime.now(tz=timezone.utc),
    )

    db.execute(t_news_draft.insert().values(news_draft))

    bucket.upload_fileobj(
        payload.image.file, image_name, ExtraArgs={"ACL": "public-read"},
    )

    return news_draft
