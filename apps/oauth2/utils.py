import base64
from datetime import datetime, timedelta
import json

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
import jwt
from jwt.algorithms import RSAAlgorithm


def generate_payload(issuer, expires_in, **extra_data):
    """
    :param issuer: identifies the principal that issued the token.
    :type issuer: str
    :param expires_in: number of seconds that the token will be valid.
    :type expires_in: int
    :param extra_data: extra data to be added to the payload.
    :type extra_data: dict
    :rtype: dict
    """
    now = datetime.utcnow()
    issued_at = now
    expiration = now + timedelta(seconds=expires_in)
    payload = {
        "iss": issuer,
        "exp": expiration,
        "iat": issued_at,
    }

    if extra_data:
        payload.update(**extra_data)

    return payload


def payload_enricher(user):
    return {
        "id": str(user.pk),
        "email": str(user.email),
        "firstName": user.first_name or "",
        "lastName": user.last_name or "",
        "superuser": user.is_superuser or False,
        "admin": user.is_superuser or user.is_staff or False,
    }


def encode_jwt(payload, headers=None):
    """
    :type payload: dict
    :type headers: dict, None
    :rtype: str
    """
    private_key_name = "JWT_PRIVATE_KEY_RSA"
    private_key = getattr(settings, private_key_name, None)
    if not private_key:
        raise ImproperlyConfigured("Missing setting {}".format(private_key_name))
    private_key = RSAAlgorithm.from_jwk(private_key)
    encoded = jwt.encode(payload, private_key, algorithm="RS256", headers=headers)
    return encoded.decode("utf-8")


def decode_jwt(jwt_value):
    """
    :type jwt_value: str
    """
    try:
        headers_enc, payload_enc, verify_signature = jwt_value.split(".")
    except ValueError:
        raise jwt.InvalidTokenError()

    payload_enc += "=" * (-len(payload_enc) % 4)  # add padding
    payload = json.loads(base64.b64decode(payload_enc).decode("utf-8"))

    public_key_name = "JWT_PUBLIC_KEY_RSA"

    if not public_key:
        raise ImproperlyConfigured("Missing setting {}".format(public_key_name))
    public_key = RSAAlgorithm.from_jwk(private_key_json)
    decoded = jwt.decode(jwt_value, public_key, algorithms=["RS256"])
    return decoded
