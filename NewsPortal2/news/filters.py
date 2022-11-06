import django_filters
from django_filters import FilterSet

from .models import Author, Category, Post


class PostFilter(FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        label='Title of post',
        lookup_expr='icontains'
    )
    category = django_filters.filters.ModelMultipleChoiceFilter(
        field_name='category__name',
        to_field_name='name',
        queryset=Category.objects.all()
    )
    time_of_creation = django_filters.DateTimeFilter(
        field_name='time_of_creation',
        label='Date/Time of creation',
        lookup_expr='gte',
        input_formats=['%d.%m.%Y', '%d.%m.%Y %H:%M']  # задаем формат даты и времени для ввода
    )
