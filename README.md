# FocusFlow Task Management Web App

FocusFlow is a task management web application built using Flask and PostgreSQL. It allows users to organize and manage their tasks efficiently, providing features such as task creation, category assignment, and user authentication.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Database Setup](#database-setup)
- [Routes and Functionality](#routes-and-functionality)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication:** Secure user authentication system to protect user data.
- **Task Creation:** Create and manage tasks with detailed information and descriptions.
- **Category Management:** Organize tasks by assigning them to different categories.
- **Dashboard:** View a personalized dashboard with an overview of tasks and categories.
- **Flask and PostgreSQL:** Built using Flask as the web framework and PostgreSQL as the database.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/) (3.6 or higher)
- [PostgreSQL](https://www.postgresql.org/) (with a database configured)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/OlaOluwalekan/FocusFlow.git
   cd FocusFlow
   ```

1. Install all dependencies

   ```shell
   pip install -r requirements.txt
   ```

1. Configure environment variables

   ```
   // .env

   DB_HOST=your_postgresql_host
   DB_USER=your_postgresql_user
   DB_PASSWORD=your_postgresql_password
   DB_NAME=your_database_name
   SECRET_KEY=your_flask_secret_key
   ```

1. Run the application

   ```shell
   python app.py
   ```

## Database Setup

FocusFlow uses a PostgreSQL database hosted on [Supabase](https://supabase.com/) to store user data. Follow the steps below to set up the database connection.

### Prerequisites

- [Supabase Account](https://app.supabase.io/)
- [psycopg2](https://pypi.org/project/psycopg2/) Python library

### Connection Details

1. Create a Supabase account if you haven't already: [Sign Up](https://app.supabase.io/signup)

1. Log in to your Supabase account and create a new project.

1. Create a project

1. Navigate to the project settings to find the database URL, API key, and other credentials.

### Configuration

Create a `.env` file in the root directory of your project and add the following:

    ```env
    DB_HOST=your_supabase_host
    DB_USER=your_supabase_user
    DB_PASSWORD=your_supabase_password
    DB_NAME=your_supabase_database
    ```

Install the psycopg2 database connector

    ```shell
    pip install psycopg2
    ```

Now, you can use the following code in your Flask application to connect to your Supabase database:

```python
import os
import psycopg2

# Load environment variables from .env
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

# Connect to Supabase
db = psycopg2.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME,
)

# Your application logic using the 'db' connection

```

## Routes and Functionality
