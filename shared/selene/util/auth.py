"""Logic for generating and validating JWT authentication tokens."""
from datetime import datetime
from time import time

import jwt


class AuthenticationError(Exception):
    pass


class AuthenticationToken(object):
    def __init__(self, secret: str, duration: int):
        self.secret = secret
        self.duration = duration
        self.jwt: str = ''
        self.is_valid: bool = None
        self.is_expired: bool = None

    def generate(self, account_id):
        """
        Generates a JWT token
        """
        payload = dict(
            iat=datetime.utcnow(),
            exp=time() + self.duration,
            sub=account_id
        )
        token = jwt.encode(payload, self.secret, algorithm='HS256')

        # convert the token from byte-array to string so that
        # it can be included in a JSON response object
        self.jwt = token.decode()

    def validate(self):
        """Decodes the auth token and performs some preliminary validation."""
        self.is_expired = False
        self.is_valid = True
        account_id = None

        if self.jwt is None:
            self.is_expired = True
        else:
            try:
                payload = jwt.decode(self.jwt, self.secret)
                account_id = payload['sub']
            except jwt.ExpiredSignatureError:
                self.is_expired = True
            except jwt.InvalidTokenError:
                self.is_valid = False

        return account_id