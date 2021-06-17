import jwt

from jwt.exceptions import ExpiredSignatureError


token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0MiIsIm5hbWUiOiJKZXNzIFRlbXBvcmFsIiwiZXhwIjoxNTE2MjM5MDIyfQ.uqeQ60enLaCQEZ-7C0d_cgQSrWfgXRQuoB1LZD0j06E'

header_data = jwt.get_unverified_header(token)

secret = 'my_super_secret'

try:
    payload = jwt.decode(
        token,
        key=secret,
        algorithms=[header_data['alg'], ]
    )
except ExpiredSignatureError as error:
    print(f'Unable to decode the token, error: {error}')