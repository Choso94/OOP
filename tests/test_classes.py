import pytest
from src.classes import Product, Category, Smartphone, LawnGrass


@pytest.fixture
def sample_product():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )


@pytest.fixture
def sample_smartphone():
    return Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый"
    )


@pytest.fixture
def sample_lawngrass():
    return LawnGrass(
        name="Газонная трава",
        description="Элитная трава для газона",
        price=500.0,
        quantity=20,
        country="Россия",
        germination_period="7 дней",
        color="Зеленый"
    )


@pytest.fixture
def sample_category(sample_smartphone):
    return Category(
        name="Смартфоны",
        description=(
            "Смартфоны, как средство не только коммуникации, "
            "но и получения дополнительных функций для удобства жизни"
        ),
        products=[sample_smartphone]
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
    assert len(sample_category._Category__products) == 1
    assert isinstance(sample_category._Category__products[0], Product)


def test_category_count():
    Category.category_count = 0
    category1 = Category("Books", "Printed books", [])
    assert Category.category_count == 1
    assert category1.name == "Books"
    category2 = Category("Toys", "Children toys", [])
    assert Category.category_count == 2
    assert category2.name == "Toys"


def test_product_count(sample_product):
    Category.product_count = 0
    category = Category(
        "Electronics",
        "Electronic devices",
        [sample_product, sample_product]
    )
    assert Category.product_count == 2
    assert len(category._Category__products) == 2


def test_empty_category():
    Category.category_count = 0
    Category.product_count = 0
    category = Category("Empty", "No products", [])
    assert len(category._Category__products) == 0
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_add_product(sample_product, sample_smartphone, sample_lawngrass):
    Category.product_count = 0
    category = Category("Test", "Test category", [])
    category.add_product(sample_product)
    assert len(category._Category__products) == 1
    assert Category.product_count == 1
    assert category._Category__products[0] == sample_product
    category.add_product(sample_smartphone)
    assert len(category._Category__products) == 2
    assert Category.product_count == 2
    category.add_product(sample_lawngrass)
    assert len(category._Category__products) == 3
    assert Category.product_count == 3
    with pytest.raises(TypeError):
        category.add_product("not a product")


def test_products_getter(sample_smartphone):
    category = Category("Test", "Test category", [sample_smartphone])
    expected = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
    assert category.products == expected


def test_new_product():
    product_data = {
        "name": "Test Product",
        "description": "Test description",
        "price": 1000.0,
        "quantity": 10
    }
    product = Product.new_product(product_data)
    assert product.name == "Test Product"
    assert product.description == "Test description"
    assert product.price == 1000.0
    assert product.quantity == 10


def test_price_getter_setter(sample_product):
    assert sample_product.price == 180000.0
    sample_product.price = 200000.0
    assert sample_product.price == 200000.0
    sample_product.price = 0
    assert sample_product.price == 200000.0
    sample_product.price = -100
    assert sample_product.price == 200000.0


def test_product_str(sample_product):
    expected = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(sample_product) == expected


def test_category_str(sample_smartphone):
    category = Category("Test", "Test category", [sample_smartphone])
    expected = "Test, количество продуктов: 5 шт."
    assert str(category) == expected


def test_product_add(sample_product):
    product2 = Product("Test", "Test desc", 1000.0, 2)
    result = sample_product + product2
    expected = (180000.0 * 5) + (1000.0 * 2)  # 900000 + 2000
    assert result == expected
    with pytest.raises(TypeError):
        sample_product + "not a product"


def test_smartphone_initialization(sample_smartphone):
    assert sample_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert sample_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert sample_smartphone.price == 180000.0
    assert sample_smartphone.quantity == 5
    assert sample_smartphone.efficiency == 95.5
    assert sample_smartphone.model == "S23 Ultra"
    assert sample_smartphone.memory == 256
    assert sample_smartphone.color == "Серый"


def test_lawngrass_initialization(sample_lawngrass):
    assert sample_lawngrass.name == "Газонная трава"
    assert sample_lawngrass.description == "Элитная трава для газона"
    assert sample_lawngrass.price == 500.0
    assert sample_lawngrass.quantity == 20
    assert sample_lawngrass.country == "Россия"
    assert sample_lawngrass.germination_period == "7 дней"
    assert sample_lawngrass.color == "Зеленый"


def test_add_restriction(sample_smartphone, sample_lawngrass):
    smartphone2 = Smartphone(
        name="Iphone 15",
        description="512GB",
        price=210000.0,
        quantity=8,
        efficiency=98.2,
        model="15",
        memory=512,
        color="Gray"
    )
    result = sample_smartphone + smartphone2
    expected = (180000.0 * 5) + (210000.0 * 8)  # 900000 + 1680000
    assert result == expected
    with pytest.raises(TypeError):
        sample_smartphone + sample_lawngrass
