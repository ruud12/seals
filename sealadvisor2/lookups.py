from ajax_select import register, LookupChannel

@register('company_search')
class CompanyLookup(LookupChannel):

    model = Company

    def get_query(self, q, request):
          return self.model.objects.filter(name__icontains=q).order_by('name')