from django.contrib import admin
from projects.models import (
    Certificate,
    CertifyingInstitution,
    Profile,
    Project,
)

# Register your models here.


class CertificateInLine(admin.StackedInline):
    model = Certificate


class CertifyingInstitutionAdmin(admin.ModelAdmin):
    inlines = [CertificateInLine]


admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(CertifyingInstitution, CertifyingInstitutionAdmin)
admin.site.register(Certificate)
