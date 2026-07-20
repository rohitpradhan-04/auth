import jwt
from ..enum import Constants
import logging
from datetime import datetime, timezone, timedelta
from fastapi import HTTPException
from jwt import ExpiredSignatureError, InvalidTokenError


class JWT:
    secrete = Constants().secret
    algorithm = "HS256"

    @classmethod
    def EncodeJwt(cls, user_data: dict):
        try:
            payload = user_data.copy()
            payload["iat"] = datetime.now(timezone.utc)
            payload["exp"] = datetime.now(timezone.utc) + timedelta(hours=1)
            encode = jwt.encode(payload, cls.secrete, algorithm=cls.algorithm)
            return encode
        except Exception as e:
            logging.exception("Error while encoding the JWT")
            raise

    @classmethod
    def Decodejwt(cls, encodedJwt: str):
        try:
            decode = jwt.decode(encodedJwt, cls.secrete, cls.algorithm)
            return decode

        except ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token has expired")

        except InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")

        except Exception as e:
            logging.exception("Error while decoding the JET")
            raise
