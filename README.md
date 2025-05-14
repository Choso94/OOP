# E-commerce Homework

This project implements an e-commerce system with `Product`, `Category`, `Smartphone`, and `LawnGrass` classes.

## Functionality
- **BaseProduct** (abstract base class):
  - Defines common product attributes (`name`, `description`, `price`, `quantity`).
  - Abstract methods: `__init__`, `price` (getter/setter), `new_product`, `__str__`.
- **PrintInitMixin**:
  - Logs object creation with class name and parameters.
- **Product class**:
  - Inherits from `PrintInitMixin` and `BaseProduct`.
  - Stores private price (`__price`), getter/setter with validation (price > 0).
  - Class method `new_product` creates products from dictionaries.
  - `__str__` returns: "Name, X руб. Остаток: X шт.".
  - `__add__` sums price * quantity for same-class products, raises `TypeError` otherwise.
- **Smartphone** and **LawnGrass**:
  - Inherit from `Product`, add specific attributes (efficiency, model, memory, color; country, germination_period, color).
- **Category class**:
  - Manages categories with private product list (`__products`).
  - Tracks total categories (`category_count`) and products (`product_count`).
  - `add_product` adds only `Product` or subclasses, raises `TypeError` otherwise.
  - Getter `products` returns formatted product strings.
  - `__str__` returns: "Name, количество продуктов: X шт.".
- **Main script**: Demonstrates classes, `new_product`, categories (`main.py` matches `16.2_main.py`).
- **Tests**: Comprehensive tests for all functionality, including `BaseProduct` and `PrintInitMixin` (`tests/test_classes.py`).
- **Linting**: Code adheres to PEP 8, checked with flake8 (0 errors).
- **Coverage**: 100% test coverage for functional code.