from django.test import TestCase
from .models import MenuItems

# Create your tests here.
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItems.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")
