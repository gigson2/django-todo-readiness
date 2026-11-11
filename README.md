# Django To Do List

This project follows the JetBrains introductory Django tutorial used by the MIS Readiness Web Development Project. It provides:

- an **All Tasks** table that excludes past-due tasks;
- a **Today** filter;
- Django admin pages for viewing, adding, editing, and deleting tasks;
- an idempotent setup command for the required instructor account and three sample tasks.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
INSTRUCTOR_PASSWORD=Mavericks python manage.py setup_readiness_demo
python manage.py runserver
```

Open `http://127.0.0.1:8000/` for the task list and `http://127.0.0.1:8000/admin/` for the admin panel.

## Deploy to PythonAnywhere

1. Clone the GitHub repository in a PythonAnywhere Bash console.
2. Create a virtual environment and install `requirements.txt`.
3. Configure a PythonAnywhere web app with this repository as its source directory and `myDjangoProject/wsgi.py` as its WSGI entry point.
4. Add the PythonAnywhere hostname to `DJANGO_ALLOWED_HOSTS` in the web app's WSGI configuration.
5. Run the database and readiness setup commands from the Bash console:

```bash
python manage.py migrate
INSTRUCTOR_PASSWORD=Mavericks python manage.py setup_readiness_demo
```

6. Reload the web app and verify the **All Tasks**, **Today**, and **Admin** pages.

The instructor login required by the assignment is `Instructor` with the password supplied through `INSTRUCTOR_PASSWORD`.
