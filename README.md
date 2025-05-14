# E-commerce Homework

This project implements an e-commerce system with `Product` and `Category` classes.

## Functionality
- **Product class**:
  - Stores name, description, quantity, and private price (`__price`).
  - Getter/setter for `price` with validation (price > 0).
  - Class method `new_product` to create products from dictionaries.
  - `__str__` method returns: "Name, X руб. Остаток: X шт.".
  - `__add__` method returns sum of `price * quantity` for two products.
- **Category class**:
  - Manages categories with name, description, and private product list (`__products`).
  - Tracks total categories (`category_count`) and products (`product_count`).
  - Method `add_product` to add products to `__products`.
  - Getter `products` returns formatted string of products using their `__str__`.
  - `__str__` method returns: "Name, количество продуктов: X шт.".
- **Main script**: Demonstrates classes, methods, `__str__`, and `__add__` as per `15.1_main.py` (`main.py` in root).
- **Tests**: Comprehensive tests for initialization, counters, methods, getters, setters, `__str__`, and `__add__` (`tests/test_classes.py`).
- **Linting**: Code adheres to PEP 8, checked with flake8 (0 errors).
- **Coverage**: 100% test coverage for functional code.