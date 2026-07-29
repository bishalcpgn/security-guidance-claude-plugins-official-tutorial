"""Route stubs."""
 
from app.db import find_user_by_email
 
 
def require_role(role):
    """Pretend authorization check."""
    return True
 
 
def health():
    return {"status": "ok"}
