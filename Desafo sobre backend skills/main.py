import jwt


def create_token(data, secret):
    data_encode = jwt.encode(data,secret, algorithm='HS256')
    return data_encode


def verify_signature(token):
    secret = 'acelera'
    try:
        data_decode = jwt.decode(token,secret, algorithm='HS256')
        return data_decode
    except jwt.exceptions.InvalidTokenError:
        return {"error" : 2}
