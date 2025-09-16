from flask import Flask
import redis
from sqlalchemy import create_engine, text

app = Flask(__name__)

# Connect to Redis (cache)
cache = redis.Redis(host="cache", port=6379)

# Connect to PostgreSQL (DB)
engine = create_engine("postgresql://user:password@database:5432/mydb")

@app.route("/")
def home():
    # Cache test
    cache.set("greeting", "Hello from Flask + Redis + Postgres!")
    cached_msg = cache.get("greeting").decode()

    # DB test
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT message FROM greetings LIMIT 1;"))
            db_msg = result.scalar()
    except Exception as e:
        db_msg = f"DB error: {str(e)}"

    return f"<h1>{cached_msg}</h1><p>DB says: {db_msg}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
