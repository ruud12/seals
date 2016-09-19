from tastypie.resources import ModelResource
from angular.models import Job


class JobResource(ModelResource):

    class Meta:
        queryset = Job.objects.all()
        resource_name = 'job'
        allowed_methods = ['post','get','patch','delete']
        always_return_data = True


