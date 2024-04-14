def greeting(name: str) -> str:
    return "Hello " + name


greeting(3)  # Argument 1 to "greeting" has incompatible type "int"; expected "str"
greeting(b"Alice")  # Argument 1 to "greeting" has incompatible type "bytes"; expected "str"
greeting("World!")  # No error


def bad_greeting(name: str) -> str:
    return "Hello " * name  # Unsupported operand types for * ("str" and "str")


def greet_all(names: list[str]) -> None:
    for name in names:
        print("Hello " + name)


names = ["Alice", "Bob", "Charlie"]
ages = [10, 20, 30]

greet_all(names)  # Ok!
greet_all(ages)  # Error due to incompatible types
