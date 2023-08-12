import os
import argparse
import backend
import frontend

parser = argparse.ArgumentParser(description="Run the application.")

parser.add_argument(
    "-st",
    "--stack",
    help="Which stack to run. Options are 'frontend' or 'backend'.",
    type=str,
    required=False,
)

args = parser.parse_args()

if args.stack:
    stack = args.stack
else:
    stack = os.environ.get("STACK")


if stack == "frontend":
    app = frontend.create_app()
elif stack == "backend":
    app = backend.create_app()
else:
    raise Exception("Invalid stack argument. Options are 'frontend' or 'backend'.")


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], host=app.config["HOST"], port=app.config["PORT"])
