import django_tables2 as tables 
from seals.models import Seal

class SealTable(tables.Table):


	class Meta:
		model = Seal

		sequence = ('...','vessel')