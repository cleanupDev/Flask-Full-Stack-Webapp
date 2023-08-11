# Backend Routes Documentation

## Table of Contents

- [Backend Routes Documentation](#backend-routes-documentation)

## Routes

| Route | Method | Description |
| ----- | ------ | ----------- |
| [/](#index) | GET | Index |
| [/admin/](#admin/index) | GET | Admin Index |
| [/admin/ping/](#admin/ping) | GET | Admin Ping |
| [/admin/ping_auth/](#admin/ping_auth) | GET | Admin Ping Auth |
| [/admin/init_db/](#admin/init_db) | GET | Admin Init DB |
| [/admin/health/](#admin/health) | GET | Admin Health |
| [/admin/test_register/](#admin/test_register) | GET | Admin Test Register |
| [/admin/test_login/](#admin/test_login) | GET | Admin Test Login |
| [/auth/login](#auth/login) | POST | Auth Login |
| [/auth/register](#auth/register) | POST | Auth Register |
| [/auth/user](#auth/user) | GET | Auth User |

## [/](#index)

**Method:** GET

**Description:** Index

**Status:** 200

**Response:**

```json
{
    "status": "success", 
    "message": "Backend running"
}
```

## [/admin/](#admin/index)

**Method:** GET

**Description:** Admin Index

**Status:** 200

**Response:**

```json
{
    "status": "success", 
    "message": "Admin Index"
}
```

## [/admin/ping/](#admin/ping)

**Method:** GET

**Description:** Pings the database

**Status:** 200

**Response:**

```json
{
    "status": "success", 
    "message": "Pong!"
}
```

## [/admin/ping_auth/](#admin/ping_auth)

**Method:** GET

**Description:** JWT protected ping

**Status:** 200

**Response:**

```json
{
    "status": "success", 
    "message": "User authenticated"
}
```

## [/admin/init_db/](#admin/init_db)

**Method:** GET

**Description:** Initializes the database

**Status:** 200

**Response:**

```json
{
    "status": "success", 
    "message": "Database initialized"
}
```

## [/admin/health/](#admin/health)

**Method:** GET

**Description:** Health check

**Status:** 200

**Response:**

```json
{
    "status": "success", 
    "message": "Server is healthy"
}
```

## [/admin/test_register/](#admin/test_register)

**Method:** GET

**Description:** Register a test user (will be removed)

**Status:** 200

**Response:**

```json
{
    "status": "success",
    "message": "User registered successfully",
    "data": None,
}
```

## [/admin/test_login/](#admin/test_login)

**Method:** GET

**Description:** Login a test user (will be removed)

**Status:** 200

**Response:**

```json
{
    "status": "success",
    "message": "User logged in successfully",
    "data": {User data},
    "access_token": JWT access token,
}
```

## [/auth/login](#auth/login)

**Method:** POST

**Description:** Login a user

**Status:** 200

**Response:**

```json
{
    "status": "success",
    "message": "User logged in successfully",
    "data": {User data},
    "access_token": JWT access token,
}
```

## [/auth/register](#auth/register)

**Method:** POST

**Description:** Register a user

**Status:** 200

**Response:**

```json
{
    "status": "success",
    "message": "User registered successfully",
    "data": None,
}
```

## [/auth/user](#auth/user)

**Method:** GET

**Description:** Get user data for Frontend Flask Login User Loader

**Status:** 200

**Response:**

```json
{
    "status": "success",
    "message": "User retrieved successfully",
    "data": {User data},
}
```
