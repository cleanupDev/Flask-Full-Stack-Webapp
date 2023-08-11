# Flask Full Stack Webapp Template

---

## Description

This is template for a full-stack web application built with Flask. The application consists of separate frontend and backend Flask apps, with a MySQL database running in a Docker container. The project utilizes JWT (JSON Web Tokens) for authentication and security. Passwords are hashed using Flask-Bcrypt, and Flask-Login is used for frontend user authentication.

## Table of Contents

* [Technologies](#technologies)
* [Installation](#installation)
* [Usage](#usage)
* [License](#license)

## Technologies

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
  * [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/)
  * [Flask-Login](https://flask-login.readthedocs.io/en/latest/)

* [MySQL](https://www.mysql.com/)
* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)

## Installation and Usage

### Docker

The Full Stack App can be run in Docker containers. Install Docker and Docker Compose, then run the following command:

```bash
docker compose up -d
```

### Local

To run the Full Stack App locally, first clone the repository:

```bash
git clone https://github.com/cleanupDev/Flask-Full-Stack-Webapp.git
```

A virtual environment is recommended.

```bash
python -m venv .venv
```

Activate the virtual environment based on your platform and install the necessary dependencies with the following command:

```bash
pip install -r requirements.txt
```

To set up the environment variables, create files named `backend.env` and `frontend.env` in the `backend/config` and `frontend/config` directories, respectively. The contents of the files should be as the template files `backend.env.template` and `frontend.env.template`.

MySQL database is run in a Docker container. To run the database, run the following command:

```bash
docker compose up -d mysql
```

To run the backend Flask app, run the following command:

```bash
python application.py --stack backend
```

To run the frontend Flask app, run the following command:

```bash
python application.py --stack frontend
```

## Documentation

Route documentation is available in the `docs/` directory.

[Backend Routes Documentation](docs/backend.md)

[Frontend Routes Documentation](docs/frontend.md)

## License

This project is licensed under the MIT license.
