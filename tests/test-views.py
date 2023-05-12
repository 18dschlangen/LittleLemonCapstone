from django.test import TestCase, Client
from django.urls import reverse
from Restaurant.models import Menu
from Restaurant.serializers import MenuSerializer
import json

class MenuItemViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.menu1 = Menu.objects.create(
            ID=1,
            Title='Spaghetti',
            Price=10.99,
            Inventory=5,
        )
        self.menu2 = Menu.objects.create(
            ID=2,
            Title='Lasagna',
            Price=12.99,
            Inventory=3,
        )

    def test_get(self):
        response = self.client.get(reverse('menu_list'))
        menus = Menu.objects.all()
        serialized_data = MenuSerializer(menus, many=True).data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), serialized_data)

    def test_post(self):
        new_menu = {
            'ID': 3,
            'Title': 'Pizza',
            'Price': '8.99',
            'Inventory': 10,
        }
        response = self.client.post(reverse('menu_list'), new_menu)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Menu.objects.count(), 3)
        self.assertEqual(Menu.objects.get(ID=3).Title, 'Pizza')