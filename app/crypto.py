"""Protected file. The PreToolUse hook refuses all edits here."""
 
import hmac
 
 
def token_matches(supplied, expected):
    return hmac.compare_digest(
        supplied.encode(), expected.encode()
    )
