from rest_framework.viewsets import ModelViewSet
from .models import Manager, Intern
from .serializers import ManagerSerializer, InternSerializer
from rest_framework.response import Response

class ManagerViewSet(ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

    def list(self, request):
        managers = self.get_queryset()
        data = [{"name": m.name, "role": m.get_role()} for m in managers]
        return Response(data)

class InternViewSet(ModelViewSet):
    queryset = Intern.objects.all()
    serializer_class = InternSerializer

    def list(self, request):
        interns = self.get_queryset()
        data = [{"name": i.name, "role": i.get_role()} for i in interns]
        return Response(data)

# Superuser Login (for grading): emmiwisz
# Email: anayoemmanuel24@gmail.com
# Password: Anayo.2006
