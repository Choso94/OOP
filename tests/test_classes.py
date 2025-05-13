import pytest
from src.classes import Product, Category


@pytest.fixture
def sample_product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )


@pytest.fixture
def sample_category(sample_product):
    return Category(
        name="Смартфоны",
        description=(
            "Смартфоны, как средство не только коммуникации, "
            "но и получения дополнительных функций для удобства жизни"
        ),
        products=[sample_product]
    )


def test_product_initialization(sample_product):
    assert sample_product.name == "Samsung Galaxy S23 Ultra"
    assert sample_product.description == "256GB, Серый цвет, 200MP камера"
    assert sample_product.price == 180000.0
    assert sample_product.quantity == 5


def test_category_initialization(sample_category):
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == (
        "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )
    assert len(sample_category.products) == 1
    assert isinstance(sample_category.products[0], Product)


def test_category_count():
    Category.category_count = 0  # Сбрасываем счетчик
    category1 = Category("Books", "Printed books", [])
    assert Category.category_count == 1
    assert category1.name == "Books"  # Используем переменную
    category2 = Category("Toys", "Children toys", [])
    assert Category.category_count == 2
    assert category2.name == "Toys"  # Используем переменную


def test_product_count(sample_product):
    Category.product_count = 0  # Сбрасываем счетчик
    category = Category(
        "Electronics",
        "Electronic devices",
        [sample_product, sample_product]
    )
    assert Category.product_count == 2
    assert len(category.products) == 2  # Используем переменную


def test_empty_category():
    Category.category_count = 0
    Category.product_count = 0
    category = Category("Empty", "No products", [])
    assert len(category.products) == 0
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_multiple_products():
    product1 = Product("Test1", "Desc1", 100.0, 1)
    product2 = Product("Test2", "Desc2", 200.0, 2)
    category = Category("Test", "Test category", [product1, product2])
    assert len(category.products) == 2
    assert category.products[0].name == "Test1"
    assert category.products[1].name == "Test2"