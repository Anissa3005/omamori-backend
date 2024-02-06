import secrets
import jwt
import datetime
import os
import environ

from dotenv import load_dotenv

load_dotenv()


def create_token(user):
    # first we need to create our payload, with user data and experation date.
    # calculate the experation date, from the time the token is created the time token will be expiered
    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
        'iat': datetime.datetime.utcnow()
    }

    secret_key = os.environ["SECRET_KEY"]
    algorithm = os.environ["ALGORITHM"]

    token = jwt.encode(payload, secret_key, algorithm=algorithm)

    return token
