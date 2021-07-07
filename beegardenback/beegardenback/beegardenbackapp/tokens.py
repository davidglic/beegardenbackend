import jwt
import datetime


# settings
lifespan = 15
key = 'asecret'

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
        return(True, decoded_token)
    except Exception as err:
        return (False, err)

# test = create_token(3)
# print(test)
# print(decode_token('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjozLCJleHAiOjE2MjU2OTAwMjV9.sS2n-ujwv_PwTSfjfmk_Me3rQ88QEps32Hy88AQ4l3c'))
# print(decode_token(test))