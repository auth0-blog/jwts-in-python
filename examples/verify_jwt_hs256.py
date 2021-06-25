import jwt


token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI0MjQyIiwibmFtZSI6Ikplc3NpY2EgVGVtcG9yYWwiLCJuaWNrbmFtZSI6Ikplc3MifQ.EDkUUxaM439gWLsQ8a8mJWIvQtgZe0et3O3z4Fd_J8o'
secret = 'my_super_secret'
header_data = jwt.get_unverified_header(token)

payload_data = jwt.decode(
    token,
    key=secret,
    algorithms=[header_data['alg'], ]
)
print(payload_data)