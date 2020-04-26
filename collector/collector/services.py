from logging import getLogger

import requests
from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from collector.config import settings

logger = getLogger(__name__)


class RecaptchaService:
    def verify_response(self, response):
        verification_resp = requests.post(
            "https://www.google.com/recaptcha/api/siteverify",
            params={"response": response, "secret": settings.RECAPTCHA_SECRET},
        )
        verification_result = verification_resp.json()

        if not self._is_successful(verification_result):
            logger.warning(f"reCAPTCHA verification failed. Response: {verification_result}")
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST, detail="reCAPTCHA verification failed"
            )

        logger.info(f'reCAPTCHA score: {verification_result.get("score")}')

    def _is_successful(self, verification_result):
        return (
            verification_result["success"]
            and verification_result["score"] > settings.RECAPTCHA_THRESHOLD
        )
