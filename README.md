# E-commerce Homework

This project implements an e-commerce system with `Product`, `Smartphone`, `LawnGrass`, and `Category` classes.

## Functionality
- **Product class**:
  - Stores name, description, quantity, and private price (`__price`).
  - Getter/setter for `price` with validation (price > 0).
  - Class method `new_product` to create products from dictionaries.
  - `__str__` method returns: "Name, X руб. Остаток: X шт.".
  - `__add__` method returns sum of `price * quantity` for two products of the same class, raises `TypeError` for different classes.
- **Smartphone class** (inherits from `Product`):
  - Additional attributes: `efficiency`, `model`, `memory`, `color`.
- **LawnGrass class** (inherits from `Product`):
  - Additional attributes: `country`, `germination_period`, `color`.
- **Category class**:
  - Manages categories with name, description, and private product list (`__products`).
  - Tracks total categories (`category_count`) and products (`product_count`).
  - Method `add_product` adds only `Product` or its subclasses, raises `TypeError` otherwise.
  - Getter `products` returns formatted string of products using their `__str__`.
  - `__str__` method returns: "Name, количество продуктов: X шт.".
- **Main script**: Demonstrates classes, inheritance, `__add__`, and `add_product` restrictions as per `16.1_main.py` (`main.py` in root).
- **Tests**: Comprehensive tests for initialization, counters, methods, getters, setters, `__str__`, `__add__`, and new classes (`tests/test_classes.py`).
- **Linting**: Code adheres to PEP 8, checked with flake8 (0 errors).
- **Coverage**: 100% test coverage for functional code.