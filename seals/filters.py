import django_filters
from seals.models import Seal
from django.db.models import Q

class SealFilter(django_filters.FilterSet):
<<<<<<< HEAD
	installedInVessel__name = django_filters.CharFilter(lookup_expr='icontains', label='Vessel name')
	size__gt = django_filters.NumberFilter(name='size',lookup_expr='gt', label='size greater than')
	size__st = django_filters.NumberFilter(name='size',lookup_expr='lt', label='size smaller than')
=======
	installedinvessel__name = django_filters.CharFilter(lookup_expr='icontains', label='Vessel name')
	size__gt = django_filters.NumberFilter(name='size',lookup_expr='gt', label='Size greater than')
	size__lt = django_filters.NumberFilter(name='size',lookup_expr='lt', label='Size smaller than')
	serial_number = django_filters.CharFilter(lookup_expr='icontains')
	installedinvessel__company__name = django_filters.CharFilter(lookup_expr='icontains', label='Company')

	installedinvessel__contact = django_filters.MethodFilter(action='custom_contact_filter', label='Contact')
>>>>>>> origin/master

	class Meta:
		model = Seal


	def custom_contact_filter(self, queryset, value):
		if value != "":
			results = queryset.filter(
			Q(installedinvessel__contact__position__icontains = value) 
			|
			Q(installedinvessel__contact__user__first_name__icontains = value)
			|
			Q(installedinvessel__contact__user__last_name__icontains = value)
			|
			Q(installedinvessel__contact__user__username__icontains = value)
			)	
			return results
		else:
			return queryset




