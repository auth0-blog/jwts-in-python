import jwt

from cryptography.hazmat.primitives import serialization


public_key = open('.ssh/example_id_rsa.pub', 'r').read()
key = serialization.load_ssh_public_key(public_key.encode())

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI0MjQyIiwibmFtZSI6Ikplc3NpY2EgVGVtcG9yYWwiLCJuaWNrbmFtZSI6Ikplc3MifQ.HgHJPl6b5W0CiDz4cNuyRcs5B3KgaoRbMvZBgCkcXOSOCAc0m7R10tSm6d86u8oW8NgzGoIAlKxBw0CIPhdx5N7MWTE2gshzQqhuq5MB9tNX1pYrLsiOMbibeMasvcf97Kd3JiLAzPPJe6XXB4PNL4h_4RcW6aCgUlRhGMPx1eRkGxAu6ndp5zzWiHQH2KVcpdVVdAwbTznLv3OLvcZqSZj_zemj__IAZPMkBBnhdjYPn-44p9-xrNmFZ9qBth4Ps1ZC1_A6lH77Mi1zb48Ou60SUT1-dhKLU09yY3IX8Pas6xtH6NbZ-e3FxjofO_OL47p25CvdqMYW50JVit2tjU6yzaoXde8JV3J40xuQqwZeP6gsClPJTdA-71PBoAYbjz58O-Aae8OlxfWZyPsyeCPQhog5KjwqsgHUQZp2zIE0Y50CEfoEzsSLRUbIklWNSP9_Vy3-pQAKlEpft0F-xP-fkSf9_AC4-81gVns6I_j4kSuyuRxlAJBe3pHi-yS2'
header_data = jwt.get_unverified_header(token)

payload_data = jwt.decode(jwt=token, key=public_key, algorithms=[header_data['alg'], ])
print('header: ', header_data)
print('payload: ', payload_data)