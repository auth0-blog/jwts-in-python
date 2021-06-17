import jwt


payload_data = {
    'sub': '4242',
    'name': 'Jessica Temporal',
    'nickname': 'Jess'
}

secret = 'my_super_secret'
token = jwt.encode(payload=payload_data, key=secret)
print(token)