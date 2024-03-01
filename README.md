# Task Manager Api

Keep track of tasks with custom project folders and secure user account creation.

## Features

- User management and authentication with JWT
- Create, view and edit tasks within projects
- Assign priority levels according to task urgency
- Well documented API endpoints for seamless integration with web and mobile frontends

## Technologies Used

- Python
- Django
- Django Rest Framework
- PostgreSQL

## Instructions for Running the Project

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Swai15/Task-Manager-Backend.git

   ```

2. **Set Up Virtual Environment (Recommended):**

   ```bash
   python3 -m venv env
   source env/bin/activate

   ```

3. **Install Dependencies:**

   ```bash
    pip install -r requirements.txt

   ```

4. **Environment Variables:**

   ```bash
   DEBUG=True
   SECRET_KEY=your_secret_key

   DATABASE_URL=your_database_url
    Or
   Switch to default SQLite database by uncommenting it in settings
   ```

5. **Run Migrations:**

   ```bash
   python manage.py migrate

   ```

6. **Run the Development Server:**

   ```bash
   python manage.py runserver

   ```

7. **Access API Documentation:**

   Visit https://jules.pythonanywhere.com/api/docs/swagger for the interactive API documentation provided by Drf-Spectacular.

## Project Progress Tracking and Frontend

The development progress of this project was being actively tracked using using this [board](https://trello.com/b/9X0ipFzH/task-manager).

The Api's frontend can be found [here](https://github.com/Swai15/Task-Manager-Frontend)
