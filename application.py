import argparse
import backend
import frontend

parser = argparse.ArgumentParser(description="Run the application.")

parser.add_argument(
    "-st",
    "--stack",
    help="Which stack to run. Options are 'frontend' or 'backend'.",
    type=str,
    required=True,
)

args = parser.parse_args()

if args.stack == "frontend":
    app = frontend.create_app()
elif args.stack == "backend":
    app = backend.create_app()
else:
    raise Exception("Invalid stack argument. Options are 'frontend' or 'backend'.")


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], host=app.config["HOST"], port=app.config["PORT"])
