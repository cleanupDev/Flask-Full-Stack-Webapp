import backend
import frontend
import os
from dotenv import load_dotenv

load_dotenv()

STACK = os.environ.get("STACK")

if STACK == "frontend":
    app = frontend.app
elif STACK == "backend":
    app = backend.app
else:
    raise Exception("STACK environment variable not set")


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], host=app.config["HOST"], port=app.config["PORT"])
