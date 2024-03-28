import jwt
import datetime
import os

from dotenv import load_dotenv

load_dotenv()


def create_token(user):
    print("Creating token 🏗️")
    payload = {
        'id': user.id,
        'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(minutes=15),
        'iat': datetime.datetime.now(datetime.UTC)
    }

    secret_key = os.environ["SECRET_KEY"]
    algorithm = os.environ["ALGORITHM"]

    token = jwt.encode(payload, secret_key, algorithm=algorithm)

    return token
