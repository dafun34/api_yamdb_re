import django_filters as filters

from .models import Title, Genre, Category


class TitleFilter(filters.FilterSet):
    genre = filters.CharFilter(field_name='genre__slug')
    category = filters.CharFilter(field_name='category__slug')
    name = filters.CharFilter(field_name='name', lookup_expr='contains')

    class Meta:
        model = Title
        fields = ('genre', 'category', 'name', 'year')


class GenreFilter(filters.FilterSet):
    class Meta:
        model = Genre
        fields = ('name', 'slug')


class CategoryFilter(filters.FilterSet):

    class Meta:
        model = Category
        fields = ('name', 'slug')
