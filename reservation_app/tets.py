# tests.py
from django.test import TestCase
from .models import Menu

class MenuTestCase(TestCase):
    def test_menu_creation(self):
        item = Menu.objects.create(name="Pizza", price=9.99)
        self.assertEqual(item.name, "Pizza")
