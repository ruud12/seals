import django_filters
from seals.models import Seal

class SealFilter(django_filters.FilterSet):
	installedInVessel__name = django_filters.CharFilter(lookup_expr='icontains')
	size__gt = django_filters.NumberFilter(name='size',lookup_expr='gt')

	class Meta:
		model = Seal

