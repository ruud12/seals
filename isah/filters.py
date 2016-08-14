import django_filters
from isah.models import Seal, SealSize
from django.db.models import Q




class SealFilter(django_filters.FilterSet):
	serial_number = django_filters.CharFilter(lookup_expr='icontains')
	size = django_filters.ModelChoiceFilter(queryset=SealSize.objects.order_by('size'))

	class Meta:
		model = Seal
		fields = ('serial_number', 'seal_type', 'size', 'company', 'vessel')

	# def custom_contact_filter(self, queryset, value):
	# 	if value != "":
	# 		results = queryset.filter(
	# 		Q(installedinvessel__contact__position__icontains = value) 
	# 		|
	# 		Q(installedinvessel__contact__user__first_name__icontains = value)
	# 		|
	# 		Q(installedinvessel__contact__user__last_name__icontains = value)
	# 		|
	# 		Q(installedinvessel__contact__user__username__icontains = value)
	# 		)	
	# 		return results
	# 	else:
	# 		return queryset



