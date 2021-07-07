import jwt
import datetime
import time
print("Testing Auth Token System")
test_token = jwt.encode({'user': 1}, "secretkey", algorithm="HS256")
print("test token: " + test_token)
decoded_token = jwt.decode(test_token, "secretkey", algorithms=["HS256"])
print("decode result: " + str(decoded_token))
try:
    print("testing inccorect key:")
    decoded_token = jwt.decode(test_token, "secretke", algorithms=["HS256"])
except Exception as err:
    print(err)
try:
    print("testing altered Token:")
    altered_token = 'eyJ0eXAiOiJKV1qiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoxfQ.QxG0XZc88cSOvIJz1JFLxC6BhtgIhGzq-9FcF0UkTm0'
    decoded_token = jwt.decode(altered_token, "secretkey", algorithms=["HS256"])
    print(type(decoded_token))
except Exception as err:
    print(err)

try:
    print("testing timeout Token (5s):")
    time_token = test_token = jwt.encode({'user': 2, 'exp': datetime.datetime.utcnow()+datetime.timedelta(seconds=4)}, "secretkey", algorithm="HS256")
    print("Waiting 1s.")
    time.sleep(1)
    decoded_token = jwt.decode(time_token, "secretkey", algorithms=["HS256"])
    print(decoded_token)
    print("Waiting 5s.")
    time.sleep(5)
    decoded_token = jwt.decode(time_token, "secretkey", algorithms=["HS256"])
    print(decoded_token)
except Exception as err:
    print(err)