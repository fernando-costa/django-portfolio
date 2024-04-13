from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets, permissions
from projects.models import (
    Certificate,
    CertifyingInstitution,
    Profile,
    Project,
)
from projects.serializers import (
    CertificateSerializer,
    CertifyingInstitutionSerializer,
    ProfileSerializer,
    ProjectSerializer,
)


# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if request.method == "GET":
            profile_id = kwargs["pk"]
            profile = get_object_or_404(Profile, id=profile_id)

            return render(request, "profile_detail.html", {"profile": profile})
        return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CertifyingInstitutionViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
