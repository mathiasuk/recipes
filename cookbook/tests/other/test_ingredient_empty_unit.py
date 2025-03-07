from django.test import TestCase
from cookbook.tests.factories import SpaceFactory, FoodFactory
from cookbook.models import Ingredient, Space, Unit


class TestIngredientEmptyUnit(TestCase):

    def setUp(self):
        self.space = SpaceFactory.create()
        self.food = FoodFactory.create(space=self.space)

    def test_empty_unit_ingredient(self):
        ingredient = Ingredient.objects.create(
            food=self.food,
            space=self.space,
            amount=10,
            note='Test without unit',
            unit=None
        )
        self.assertIsNone(ingredient.unit)
        self.assertIsNotNone(ingredient.food)

        self.assertIsInstance(ingredient, Ingredient)
        self.assertEqual(ingredient.food, self.food)
        self.assertEqual(ingredient.space, self.space)
        self.assertEqual(ingredient.amount, 10)
        self.assertEqual(ingredient.note, 'Test without unit')


class TestIngredientEmptyUnit(TestCase):
    def test_empty_unit_ingredient(self):
        space = Space.objects.first()
        ingredient = Ingredient.objects.create(
            food_id=1,
            space=space,
            amount=10,
            note='Test without unit'
        )
        self.assertIsNone(ingredient.unit)
        self.assertIsNotNone(ingredient.food)

        self.assertIsInstance(ingredient, Ingredient)
        self.assertEqual(ingredient.food, self.food)
        self.assertEqual(ingredient.space, self.space)
        self.assertEqual(ingredient.amount, 10)
        self.assertEqual(ingredient.note, 'Test without unit')

        self.assertIsNone(ingredient.unit)

        self.assertIsNotNone(ingredient.food)
        self.assertIsNotNone(ingredient.space)
        self.assertIsNotNone(ingredient.amount)
        self.assertIsNotNone(ingredient.note)
        self.assertTrue(ingredient.unit is None)
        self.assertTrue(ingredient.food is not None)

    def test_create_ingredient_empty_unit(self):
        
        
        ingredient_data = {
                'food': self.food.id,
                'amount': 10,
                'space': self.space.id,
                'note': 'Test without unit'
            }
        api_client = self.client_create_ingredient(data=ingredient_data)
        self.assertEqual(api_client.status_code, 201)

        ingredient = Ingredient.objects.filter(id=api_client.json['id']).first()
        
        self.assertIsNone(ingredient.unit)
        self.assertIsNotNone(ingredient.food)

        self.assertIsInstance(ingredient, Ingredient)
        self.assertEqual(ingredient.food_id, self.food.id)
        self.assertEqual(ingredient.space, self.space)
        self.assertEqual(ingredient.amount, 10)
        self.assertEqual(ingredient.note, 'Test without unit')
