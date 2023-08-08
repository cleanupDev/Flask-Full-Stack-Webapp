# Flask Full Stack Webapp Template

---

## Description

This is template for a full-stack web application built with Flask. The application consists of separate frontend and backend Flask apps, with a MySQL database running in a Docker container. The project utilizes JWT (JSON Web Tokens) and CORS (Cross-Origin Resource Sharing) for authentication and security. Passwords are hashed using Flask-Bcrypt, and Flask-Login is used for frontend user authentication.

## Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [License](#license)

## Installation

To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt
```

To set up the environment variables, create files named `backend.env` and `frontend.env` in the `backend` and `frontend` directories, respectively. The contents of the files should be as the template files `backend.env.template` and `frontend.env.template`, respectively.

## Usage

MySQL database is run in a Docker container. To run the database, run the following command:

```bash
docker compose up -d
```

TODO

Visit `http://localhost:5000` in your browser to view the application.
The backend API is available at `http://localhost:5001`.

## License

This project is licensed under the MIT license.
