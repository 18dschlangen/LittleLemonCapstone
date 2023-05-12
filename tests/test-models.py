from django.test import TestCase
from Restaurant.models import Menu

class MenuModelTest(TestCase):
    def test_get_menu(self):
        menu = Menu.objects.create(
            ID=1,
            Title='Spaghetti',
            Price=10.99,
            Inventory=5,
        )
        expected_string = 'Spaghetti : 10.99'
        self.assertEqual(str(menu), expected_string)