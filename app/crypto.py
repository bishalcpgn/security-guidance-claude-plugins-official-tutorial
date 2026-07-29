import hmac
 
 
def token_matches(supplied, expected):
    return hmac.compare_digest(
        supplied.encode(), expected.encode()
    )
