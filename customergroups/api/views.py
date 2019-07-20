from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from .serializers import CustomerGroupSerializer, CustomerReadGroupSerializer
from customergroups.models import CustomerGroup

class CustomerGroupAPIView(
    CreateModelMixin, 
    ListAPIView): 
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = CustomerGroupSerializer
    passed_id                   = None
    search_fields               = ('group_name')
    ordering_fields             = ('group_name', 'timestamp')
    queryset                    = CustomerGroup.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CustomerGroupReadAPIView(
    CreateModelMixin, 
    ListAPIView): 
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = CustomerReadGroupSerializer
    passed_id                   = None
    search_fields               = ('group_name')
    ordering_fields             = ('group_name', 'timestamp')
    queryset                    = CustomerGroup.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class CustomerGroupAPIDetailView(
    UpdateModelMixin,
    DestroyModelMixin, 
    RetrieveAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = CustomerReadGroupSerializer
    queryset                    = CustomerGroup.objects.all()
    lookup_field                = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


