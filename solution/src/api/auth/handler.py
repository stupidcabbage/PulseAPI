import time
from jose import jwt
from config import jwt_settings
from schemas.tokens import TokenSchema


async def signJWT(login: str) -> TokenSchema:
    payload = {
        "login": login,
        "created_at": time.time(),
        "expires": time.time() + 6000
    }
    token = jwt.encode(payload, jwt_settings.SECRET_KEY,
                       algorithm=jwt_settings.ALGORITHM)
    return TokenSchema(token=token)


async def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, jwt_settings.SECRET_KEY,
                                   algorithms=[jwt_settings.ALGORITHM])
        return decoded_token
    except:
        return {}