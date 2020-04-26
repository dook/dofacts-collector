from dataclasses import dataclass

from fastapi import File, Form, UploadFile
from pydantic.networks import EmailStr, HttpUrl

from collector import consts


class ShortHttpUrl(HttpUrl):
    max_length = consts.URL_LENGTH


@dataclass()
class VerificationRequestSchema:
    email: EmailStr = Form(...)
    comment: str = Form(..., max_length=consts.COMMENT_LENGTH)
    url: ShortHttpUrl = Form(...)
    text: str = Form(..., max_length=consts.TEXT_LENGTH)
    image: UploadFile = File(...)
    recaptcha: str = Form(...)
