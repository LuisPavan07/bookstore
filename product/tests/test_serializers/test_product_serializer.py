import pytest

from product.factories import ProductFactory, CategoryFactory
from product.serializers.product_serializer import ProductSerializer


@pytest.mark.django_db
def test_product_serializer():
    categories = CategoryFactory.create_batch(3)
    product = ProductFactory(category=categories)
    serializer = ProductSerializer(product)
    data = serializer.data

    assert data["title"] == product.title
    assert data["price"] == product.price
    assert data["description"] == product.description
    assert len(data["category"]) == 3
    assert data["category"][0]["title"] == categories[0].title
