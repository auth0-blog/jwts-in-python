# Code Samples: Using PyJWT to Verify and Create JWTs

This repo contains the code used in the ["How To Handle JWTs in Python"](https://auth0.com/blog/how-to-handle-jwt-in-python) blog post check it out to learn how to create and verify JWTs using Python and PyJWT. ;)

## Prerequisites

- Python >= 3.6

## Setup

Grab the repo and install the dependencies.

```bash
git clone git@github.com:auth0-blog/jwts-in-python.git
cd whats-new-flask-2
python3 -m venv .env
source .env/bin/activate
pip install -U pip
pip install -r requirements.txt
```

You'll also need to copy a pair of public/private SSH RSA keys into the `.ssh` folder. Currently there is a public example key in there used in the `examples/verify_jwt_rsa256_ssh.py` file but to use the `examples/create_jwt_rsa256_ssh.py` you'll need either a private key under the `.ssh` folder or to adjust the path to a preexisting folder.

In case you want to generate new keys [you'll find instructions here](https://auth0.com/blog/how-to-handle-jwt-in-python/#Generating-a-RSA-Key-Pair).

## Running scripts

```console
python examples/verify_jwt_rsa256_ssh.py
```

## Wrapping up

If you ran into any issues, reach out in the [comments of the blog post](https://auth0.com/blog/how-to-handle-jwt-in-python) or [feel free to tweet me](https://twitter.com/jesstemporal). Thanks!