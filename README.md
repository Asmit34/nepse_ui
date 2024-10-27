# Django Stock Management System

## Overview

This project is a Django-based stock management system that utilizes a PostgreSQL database named **stock**. The database is pre-populated with data from CSV files. This README provides step-by-step instructions for setting up the project on another user's machine.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python** (version 3.x)
- **Django** (version compatible with the project)
- **PostgreSQL** (with the `postgres` user)
- **psycopg2** or **psycopg2-binary** library for PostgreSQL
- **Git** (optional, for version control)

You can install the required Python packages using pip:


# Database Setup

## Create the Database

Ensure you have a PostgreSQL server running. Create a database named `stock` using the following SQL command:

```sql
CREATE DATABASE stock;
```
## Restore Existing Data
If you have received a database dump file (stock_dump.sql), restore the database using the following command:


```bash
psql -U postgres -d stock -f stock_dump.sql
```
Make sure to adjust the command if your PostgreSQL username is different.

## Environment Variables
The project uses environment variables to configure database access. You need to set the following environment variables on your machine:

```bash
DB_NAME: The name of the database (default: stock)
DB_USER: The PostgreSQL user (default: postgres)
DB_PASSWORD: The password for the PostgreSQL user
DB_HOST: The database host (default: localhost)
DB_PORT: The database port (default: 5432)

```

### Setting Environment Variables
On Windows

Open Command Prompt and run:

```bash
set DB_NAME=stock
set DB_USER=postgres
set DB_PASSWORD=your_actual_password
set DB_HOST=localhost
set DB_PORT=5432
```
On Linux or macOS

Open Terminal and run:

```bash
export DB_NAME=stock
export DB_USER=postgres
export DB_PASSWORD=your_actual_password
export DB_HOST=localhost
export DB_PORT=5432
```

## Running the Project
Once the database is set up and the environment variables are configured, you can run the project. You may need to run the following commands to apply migrations and start the server:


```bash
Copy code
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

```


### Instructions for Use
Feel free to adjust any sections as needed, and let me know if you need any additional information or modifications!
