import logging
from datetime import datetime, timedelta, timezone

import jwt
from fastapi import HTTPException
from jwt import ExpiredSignatureError, InvalidTokenError

from ..enum import Constants


class JWT:
    secrete = Constants().secret
    algorithm = "HS256"

    @classmethod
    def encode_jwt(cls, user_data: dict):
        try:
            payload = user_data.copy()
            payload["iat"] = datetime.now(timezone.utc)
            payload["exp"] = datetime.now(timezone.utc) + timedelta(hours=1)
            encode = jwt.encode(payload, cls.secrete, algorithm=cls.algorithm)
            return encode
        except Exception:
            logging.exception("Error while encoding the JWT")
            raise

    @classmethod
    def decode_jwt(cls, decode_jwt: str):
        try:
            decode = jwt.decode(decode_jwt, cls.secrete, cls.algorithm)
            return decode

        except ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token has expired") from None

        except InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token") from None

        except Exception:
            logging.exception("Error while decoding the JET")
            raise
