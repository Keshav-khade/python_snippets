"""
1. 🔐 Credentials → Environment variables
Your original:
password="Kartik@123"
Problem: credentials are sitting directly in source code.
Better:
password=os.getenv("DB_PASSWORD")
Now:
Python code ──────→ DB_PASSWORD
                       ↑
                    .env / environment
So your application code doesn't directly contain the secret.

2. 🧩 Connection function → reusable database layer
Instead of:
conn = mysql.connector.connect(...)
everywhere, create something like:
def create_connection():
    ...
Now your application has one place responsible for database connections.

3. 🚀 Connection Pool → reuse connections
And this is the really interesting one.
Without pooling:
# resource-management mechanism
Request 1 → CREATE connection → use → DESTROY
Request 2 → CREATE connection → use → DESTROY
Request 3 → CREATE connection → use → DESTROY
Request 4 → CREATE connection → use → DESTROY
If requests become frequent, repeatedly establishing connections creates unnecessary overhead.

"""

# this is how we can connect to the database
import mysql.connector
conn = None
try:
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user='root',
        database='devdb',
        password='Kartik@123',
    )
    if conn.is_connected():
        print("connection establishes successfully")
        print(conn.server_info)
        print(conn.database)
        print(conn.server_version)
        print(conn.server_port)
        print(conn.server_host)

        cur = conn.cursor()
        cur.execute("select * from dept")
        results = cur.fetchall()

        for row in results:
            print(row)
except mysql.connector.DatabaseError as msg:
    print(msg)
finally:
    if conn:
        conn.close()
        print("connection closed successfully")