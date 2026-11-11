import os
from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

from todo.models import ToDoItem


class Command(BaseCommand):
    help = "Create the instructor account and three sample tasks for the readiness project."

    def handle(self, *args, **options):
        password = os.environ.get("INSTRUCTOR_PASSWORD")
        if not password:
            raise CommandError("Set INSTRUCTOR_PASSWORD before running this command.")

        user_model = get_user_model()
        instructor, _ = user_model.objects.get_or_create(
            username="Instructor",
            defaults={"is_staff": True, "is_superuser": True},
        )
        instructor.is_staff = True
        instructor.is_superuser = True
        instructor.set_password(password)
        instructor.save()

        tasks = (
            ("Review Django models", date.today()),
            ("Practice using the admin panel", date.today()),
            ("Verify the deployed application", date.today() + timedelta(days=1)),
        )
        for text, due_date in tasks:
            ToDoItem.objects.get_or_create(text=text, defaults={"due_date": due_date})

        self.stdout.write(self.style.SUCCESS("Instructor account and sample tasks are ready."))
