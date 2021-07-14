import jwt
import datetime
from django.conf import settings

# Settings
# please change settings in settings.py
lifespan = 15
key = settings.JWT_TOKENS

def create_token(userid):
    token = jwt.encode({
        'user': userid,
        'exp': datetime.datetime.utcnow()+datetime.timedelta(seconds=lifespan*60)}, 
        key, 
        algorithm="HS256")
    return token

def decode_token(token):
    try:
        decoded_token = jwt.decode(token, key, algorithms=["HS256"])
        return (True, decoded_token)
    except Exception as err:
        return (False, err)

