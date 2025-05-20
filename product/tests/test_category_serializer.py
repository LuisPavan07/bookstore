import pytest

from product.factories import CategoryFactory
from product.serializers.category_serializer import CategorySerializer

@pytest.mark.django_db
def test_category_serializer():
    category = CategoryFactory(
        title='Título do teste',
        slug='teste-slug',
        description='Descricão para o teste',
        active=True,
    )
    serializer = CategorySerializer(category)
    data = serializer.data
    
    assert data['title'] == 'Título do teste'
    assert data['slug'] == 'teste-slug'
    assert data['description'] == 'Descricão para o teste'
    assert data['active'] is True