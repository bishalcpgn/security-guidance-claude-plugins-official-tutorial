import sqlite3
 
 
def get_conn():
    return sqlite3.connect(":memory:")
 
 
def find_user_by_email(email):
    """Baseline: parameter binding, not string building."""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, email FROM users WHERE email = ?", (email,)
    )
    return cur.fetchone()
