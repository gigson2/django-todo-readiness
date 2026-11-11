from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import ToDoItem


def create_todo(text, days):
    return ToDoItem.objects.create(
        text=text,
        due_date=date.today() + timedelta(days=days),
    )


class ToDoViewsTest(TestCase):
    def test_all_tasks_hides_past_due_items(self):
        past = create_todo("Past task", -7)
        today = create_todo("Today's task", 0)
        future = create_todo("Future task", 7)

        response = self.client.get(reverse("index"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context["object_list"], [today, future])
        self.assertNotContains(response, past.text)

    def test_today_filter_only_shows_items_due_today(self):
        today = create_todo("Today's task", 0)
        create_todo("Future task", 1)

        response = self.client.get(reverse("today"))

        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(response.context["object_list"], [today])


class ToDoAdminTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_superuser(
            username="Instructor",
            password="test-password",
        )
        self.client.force_login(self.user)
        self.item = create_todo("Admin-managed task", 0)

    def test_admin_exposes_list_add_edit_and_delete_pages(self):
        urls = (
            reverse("admin:todo_todoitem_changelist"),
            reverse("admin:todo_todoitem_add"),
            reverse("admin:todo_todoitem_change", args=[self.item.pk]),
            reverse("admin:todo_todoitem_delete", args=[self.item.pk]),
        )

        for url in urls:
            with self.subTest(url=url):
                self.assertEqual(self.client.get(url).status_code, 200)
