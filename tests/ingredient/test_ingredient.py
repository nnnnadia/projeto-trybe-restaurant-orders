from src.models.ingredient import Ingredient, Restriction


# Req 1
def test_ingredient():
    ingredient_1 = Ingredient("queijo mussarela")
    ingredient_2 = Ingredient("queijo mussarela")
    assert hash(ingredient_1) == hash(ingredient_2)

    ingredient_1 = Ingredient("presunto")
    ingredient_2 = Ingredient("presunto")
    assert ingredient_1 == ingredient_2

    ingredient_1 = Ingredient("presunto")
    ingredient_2 = Ingredient("queijo mussarela")
    assert hash(ingredient_1) != hash(ingredient_2)

    ingredient_1 = Ingredient("presunto")
    ingredient_2 = Ingredient("queijo mussarela")
    assert ingredient_1 != ingredient_2

    ingredient_1 = Ingredient("presunto")
    assert repr(ingredient_1) == "Ingredient('presunto')"
    assert ingredient_1.name == "presunto"

    restrictions_expected = {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }
    ingredient_1 = Ingredient("presunto")
    ingredient_2 = Ingredient("queijo mussarela")

    assert ingredient_1.restrictions != restrictions_expected
    assert ingredient_2.restrictions == restrictions_expected

    ingredient_1 = Ingredient("farinha")
    restrictions_expected = {Restriction.GLUTEN}
    assert set(ingredient_1.restrictions) == restrictions_expected
