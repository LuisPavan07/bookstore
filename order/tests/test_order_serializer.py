import pytest

from order.factories import OrderFactory
from product.factories import ProductFactory
from order.serializers.order_serializer import OrderSerializer

@pytest.mark.django_db
def test_order_serializer():
    products = ProductFactory.create_batch(3, price=1000)
    order = OrderFactory(product=products)
    
    serializer = OrderSerializer(order)
    data = serializer.data
    
    assert len(data['product']) == 3
    assert data['total'] == 3000
    assert data['product'][0]['title'] == products[0].title