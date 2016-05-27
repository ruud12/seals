import django_filters
from seals.models import Seal

class SealFilter(django_filters.FilterSet):
	installedInVessel__name = django_filters.CharFilter(lookup_expr='icontains', label='Vessel name')
	size__gt = django_filters.NumberFilter(name='size',lookup_expr='gt', label='size greater than')
	size__st = django_filters.NumberFilter(name='size',lookup_expr='lt', label='size smaller than')

	class Meta:
		model = Seal

