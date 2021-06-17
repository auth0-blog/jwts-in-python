import jwt

from cryptography.hazmat.primitives import serialization


payload_data = {
    'sub': '4242',
    'name': 'Jessica Temporal',
    'nickname': 'Jess'
}

# you'll need to create or update the path to correspond to an available key
private_key = open('.ssh/id_rsa', 'r').read()
key = serialization.load_ssh_private_key(private_key.encode(), password=b'')

token = jwt.encode(payload=payload_data, key=key, algorithm='RS256')
print(token)