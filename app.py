def greet(name):
    return f"Hello, {name}!"

def test_greet():
    assert greet("World") == "Hello, World!"
    assert greet("") == "Hello, !"

if __name__ == "__main__":
    print(greet("CI/CD!"))
