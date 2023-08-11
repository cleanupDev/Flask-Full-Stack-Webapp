# Frontend Routes Documentation

## Table of Contents

- [Frontend Routes Documentation](#frontend-routes-documentation)
  - [Table of Contents](#table-of-contents)
  - [Routes](#routes)
  - [/](#)
  - [/home/](#home)
  - [/login/](#login)
  - [/register/](#register)
  - [/logout/](#logout)

## Routes

| Route | Method | Description |
| ----- | ------ | ----------- |
| [/](#index) | GET | Index |
| [/home/](#home) | GET | Home |
| [/login/](#login) | GET | Login |
| [/register/](#register) | GET | Register |
| [/logout/](#logout) | GET | Logout |

## [/](#index)

**Method:** GET

**Description:** Index

**Status:** 200

**Response:**

Rendered HTML

## [/home/](#home)

**Method:** GET

**Description:** Flask Login protected route

**Status:** 200

**Response:**

Rendered HTML

## [/login/](#login)

**Method:** GET

**Description:** Login

**Status:** 200

**Response:**

Redirect to `/home/`

## [/register/](#register)

**Method:** GET

**Description:** Register

**Status:** 200

**Response:**

Redirect to `/login/`

## [/logout/](#logout)

**Method:** GET

**Description:** Logout

**Status:** 200

**Response:**

Redirect to `/`
