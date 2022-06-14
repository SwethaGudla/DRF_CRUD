import secrets
import jwt
encoded_jwt = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
print(encoded_jwt)
token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0OTYwNDUzLCJpYXQiOjE2NTQ5Nzk5NTMsImp0aSI6Ijg1MjJkZjliMTZhZTQ5ZGI5YjM0NjIxMDJmMjUwOGRiIiwidXNlcl9pZCI6MiwidXNlciI6ImFkbWluIiwiZGF0ZSI6IjIwMjItMDYtMTEiLCJlbWFpbCI6ImFkbWluQG9qYXMuY29tIn0.9NAC9PsaamqgBBe4WtR_FUDkyVmzUNkzTGNAb2N63eg"
secret="django-insecure-ck!-4rbo!6-wa&rvys41*sm0o!2#jg!qc8u!ux4ugaoe=84-cm"
x=jwt.decode(token, secret,algorithms=["HS256"])
print(x)