# E-commerce Homework

This project implements an e-commerce system with `Product` and `Category` classes.

## Functionality
- **Product class**:
  - Stores name, description, quantity, and private price (`__price`).
  - Getter/setter for `price` with validation (price > 0).
  - Class method `new_product` to create products from dictionaries.
- **Category class**:
  - Manages categories with name, description, and private product list (`__products`).
  - Tracks total categories (`category_count`) and products (`product_count`).
  - Method `add_product` to add products to `__products`.
  - Getter `products` returning a formatted string: "Name, X руб. Остаток: X шт.\n".
- **Main script**: Demonstrates classes, methods, getters, and setters as per `14.2_main.py` (`main.py` in root).
- **Tests**: Comprehensive tests for initialization, counters, methods, getters, and setters (`tests/test_classes.py`).
- **Linting**: Code adheres to PEP 8, checked with flake8 (0 errors).
- **Coverage**: 100% test coverage for functional code.