import pytest
from cart import Cart

def test_add_item():
    cart = Cart()
    cart.add_item("Laptop", 1000, 1)
    assert len(cart.items) == 1
    assert cart.items[0]["name"] == "Laptop"
    assert cart.items[0]["price"] == 1000

def test_total_price():
    cart = Cart()
    cart.add_item("Laptop", 1000, 2)
    cart.add_item("Maus", 50, 1)
    assert cart.total_price() == 2050

def test_remove_item():
    cart = Cart()
    cart.add_item("Laptop", 1000, 1)
    cart.remove_item("Laptop")
    assert len(cart.items) == 0

def test_clear_cart():
    cart = Cart()
    cart.add_item("Laptop", 1000, 1)
    cart.add_item("Maus", 50, 1)
    cart.clear_cart()
    assert len(cart.items) == 0

def test_invalid_price_or_quantity():
    cart = Cart()
    with pytest.raises(ValueError):
        cart.add_item("Fehlerhaftes Produkt", -10, 1)
