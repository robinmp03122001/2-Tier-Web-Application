from flask import Flask
import os
import psycopg2

app =Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host = os.environ['DB_HOST'],
        database = os.environ['DB_NAME'],
        user = os.environ['DB_USER'],
        password = os.environ['DB_PASS']
    )
    return conn

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        conn.close()
        return "<h1> 2-Tier App is Running! DB Connection Successful.</h1>"
    except:
        return f"<h1>App is running, but DB failed: {e}</h1>" 


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)