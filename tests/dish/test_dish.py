import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    dish_1 = Dish("Pizza", 10.99)
    dish_2 = Dish("Pizza", 10.99)
    dish_3 = Dish("Lasanha", 12.99)

    assert dish_1.name == "Pizza"
    assert hash(dish_1) == hash(dish_2)
    assert hash(dish_1) != hash(dish_3)
    assert dish_1 == dish_1
    assert dish_1 == dish_2
    assert dish_1 != dish_3
    assert repr(dish_1) == "Dish('Pizza', R$10.99)"

    with pytest.raises(TypeError):
        dish_1 = Dish("Pizza", "string value")

    with pytest.raises(ValueError):
        dish_1 = Dish("Pizza", -99)

    ingredient = Ingredient("queijo mussarela")
    assert str(ingredient) not in map(str, dish_1.get_ingredients())

    ingredient_1 = Ingredient("queijo mussarela")
    ingredient_2 = Ingredient("farinha")
    dish_1.add_ingredient_dependency(ingredient_1, 42)
    dish_1.add_ingredient_dependency(ingredient_2, 66)
    restrictions_expected = {
        Restriction.GLUTEN,
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
    restrictions_obtained = dish_1.get_restrictions()
    assert restrictions_obtained == restrictions_expected

    ingredients_expected = {
        ingredient_1,
        ingredient_2,
    }
    ingredients_obtained = dish_1.get_ingredients()
    assert ingredients_obtained == ingredients_expected
