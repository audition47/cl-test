from app import greet

def test_greet_normal():
    assert greet("Alice") == "Hello, Alice!"

def test_greet_empty():
    assert greet("") == "Hello, !"

def test_greet_special():
    assert greet("123") == "Hello, 123!"
