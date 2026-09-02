import os

from dotenv import load_dotenv
load_dotenv("dev.env")

from src.main.server.server import create_app

app = create_app()

HOST = os.getenv("HOST")
PORT = os.getenv("PORT")


if __name__ == "__main__":
    app.run(debug=True, host=HOST, port=PORT)