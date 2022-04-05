from django.test import TestCase
from django.utils import timezone
from geo_location.models import Cities


class ModelTest(TestCase):
    def save_city(self, name="Las Vegas", location ="0101000020E61000009A5FCD0182CA5CC02FC4EA8F30164240"):
        return Cities.objects.Create(name = name, location = location, created_at = timezone.now())

    def test_save_city(self):
        save = self.save_city()
        self.assertTrue(isinstance(save, Cities))
        self.assertEqual(save.__unicode__(), save.name)