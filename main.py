from flask import Flask
from dotenv import load_dotenv
import os
import logging
from routers.course_router import course_router
from repositories.course_repository import init_db

load_dotenv()

app = Flask(__name__)
app.register_blueprint(course_router)

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

if __name__ == "__main__":
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8080))
    ENVIRONMENT = os.getenv("ENVIRONMENT", "Production")
    logging.info(f"Starting database with SQLite3")
    init_db()
    logging.info(f"Starting server on {HOST}:{PORT}")
    app.run(host=HOST, port=PORT, debug=True)
