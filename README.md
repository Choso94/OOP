# E-commerce Homework

This project implements an e-commerce system with `Product` and `Category` classes.

## Functionality
- **Product class**:
  - Stores name, description, quantity, and private price (`__price`).
  - Getter/setter for `price` with validation (price > 0).
  - Class method `new_product` to create products from dictionaries.
  - `__str__` method returns: "Name, X руб. Остаток: X шт.".
- **Category class**:
  - Manages categories with name, description, and private product list (`__products`).
  - Tracks total categories (`category_count`) and products (`product_count`).
  - Method `add_product` adds only `Product` or its subclasses, raises `TypeError` otherwise.
  - Getter `products` returns formatted string of products using their `__str__`.
  - `__str__` method returns: "Name, количество продуктов: X шт.".
- **Main script**: Demonstrates classes, `add_product`, `new_product`, and price getter/setter (`main.py` matches `14.2_main.py`).
- **Tests**: Comprehensive tests for initialization, counters, methods, getters, setters, and `__str__` (`tests/test_classes.py`).
- **Linting**: Code adheres to PEP 8, checked with flake8 (0 errors).
- **Coverage**: 100% test coverage for functional code.