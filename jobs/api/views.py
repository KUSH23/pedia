from rest_framework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from .serializers import JobsSerializer, JobsReadSerializer
from jobs.models import Jobs

class JobAPIView(
    CreateModelMixin, 
    ListAPIView): 
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = JobsSerializer
    passed_id                   = None
    search_fields               = ('group')
    ordering_fields             = ('group', 'timestamp')
    queryset                    = Jobs.objects.all()
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class JobAPIReadView(
    CreateModelMixin, 
    ListAPIView): 
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = JobsReadSerializer
    passed_id                   = None
    search_fields               = ()
    ordering_fields             = ('group_name')
    queryset                    = Jobs.objects.all().order_by('group')
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class JobAPIDetailView(
    UpdateModelMixin,
    DestroyModelMixin, 
    RetrieveAPIView):
    permission_classes          = []
    authentication_classes      = []
    serializer_class            = JobsReadSerializer
    queryset                    = Jobs.objects.all()
    lookup_field                = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class GroupAPIDetailView(JobAPIReadView):
    serializer_class            = JobsReadSerializer
    def get_queryset(self, *args, **kwargs):
        group = self.kwargs.get("group", None)
        if group is None:
            return Jobs.objects.none()
        return Jobs.objects.filter(group=group)

    def post(self, request, *args, **kwargs):
        return Response({"detail": "Not allowed here"}, status=400)