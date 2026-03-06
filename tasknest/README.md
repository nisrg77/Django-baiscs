# TaskNest - Django Task Management App

## Project Overview
TaskNest is a comprehensive task management web application built with Django. It features a full CRUD (Create, Read, Update, Delete) system for effective task tracking.

## Features
- **Task Dashboard**: View all tasks sorted by creation date.
- **Create Task**: Add new tasks with titles and descriptions.
- **Update Task**: Edit existing task details and mark them as completed.
- **Delete Task**: Remove tasks with a confirmation prompt.
- **Responsive UI**: Clean nd simple interface styled with CSS.

## Prerequisites
- Python 3.x
- Django 6.0+

## Setup Steps

### 1. Environment Setup
Assuming you are in `d:\Django-baiscs`:
```bash
# Activate virtual environment
.\venv\Scripts\activate
```

### 2. Project Initialization
```bash
# Create the Django project
django-admin startproject tasknest

# Navigate into the project directory
cd tasknest
```

### 3. App Creation & Configuration
The project consists of a `tasks` app. Use the included code to set up models, views, and urls.

#### Migrations
Apply the database migrations to set up the schema:
```bash
python manage.py makemigrations
python manage.py migrate
```

## How to Run

1. Navigate to the project directory:
   ```bash
   cd d:\Django-baiscs\tasknest
   ```

2. Run the development server:
   ```bash
   python manage.py runserver
   ```

3. Open your browser to: http://127.0.0.1:8000/



### Visual indicator for Completed Tasks
We modified the task list to show a green tick instead of a strikethrough for completed tasks. Here is the step-by-step process:

1.  **Open Template**: Edited `tasks/templates/tasks/task_list.html`.
2.  **Remove Old Style**: Found the `<h2>` tag displaying the task title and removed the conditionally applied inline CSS `text-decoration: line-through`.
3.  **Add New Indicator**: Added a conditional check `{% if task.completed %}` inside the `<h2>` tag.
4.  **Insert Tick Symbol**: Inside the check, added a `<span>` element containing the HTML entity for a checkmark (`&#10004;`) and styled it with `color: #28a745;` (green).

## Project Structure
- `tasknest/`: Project configuration.
- `tasks/`: Main application directory.
    - `models.py`: Database schema for Tasks.
    - `views.py`: Logic for task operations (list, create, update, delete).
    - `forms.py`: Form handling for task input.
    - `urls.py`: URL routing for task views.
    - `templates/tasks/`: HTML templates for the UI.
        - `base.html`: Common layout and styling.
        - `task_list.html`: Home page displaying tasks.
        - `task_form.html`: Form for adding/editing tasks.
        - `task_confirm_delete.html`: Deletion confirmation page.
