# Django To Do List

I completed this project for the MIS Readiness Web Development Project by following the JetBrains introductory Django tutorial. The finished application is deployed at [gigson2.pythonanywhere.com](https://gigson2.pythonanywhere.com/).

The application has an All Tasks page and a Today page. All Tasks displays current and upcoming items, while Today displays only items due on the current date. I used a Django model to store each task and its due date, class-based views to retrieve the records, templates to display the tables, and URL routes for navigation.

I also registered the ToDoItem model in the Django admin panel. The admin account can view, add, edit, and delete tasks. I added three task records to the deployed application for review and created the instructor account with the credentials provided in Canvas.

## Run the project locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The task list opens at `http://127.0.0.1:8000/`, and the admin panel is at `http://127.0.0.1:8000/admin/`.
