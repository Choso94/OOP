from src.classes import Product, Category


if __name__ == "__main__":
    product1 = Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5
    )
    product2 = Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8
    )
    product3 = Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14
    )

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        name="Смартфоны",
        description=(
            "Смартфоны, как средство не только коммуникации, "
            "но и получения дополнительных функций для удобства жизни"
        ),
        products=[product1, product2, product3]
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products.strip().split("\n")))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product(
        name="55\" QLED 4K",
        description="Фоновая подсветка",
        price=123000.0,
        quantity=7
    )
    category2 = Category(
        name="Телевизоры",
        description=(
            "Современный телевизор, который позволяет наслаждаться "
            "просмотром, станет вашим другом и помощником"
        ),
        products=[product4]
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products.strip().split("\n")))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
