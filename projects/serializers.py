from rest_framework import serializers
from projects.models import (
    Certificate,
    CertifyingInstitution,
    Profile,
    Project,
)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "name", "github", "linkedin", "bio"]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "github_url",
            "keyword",
            "key_skill",
            "profile",
        ]


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"


class NestedCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ["name"]


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = NestedCertificateSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = "__all__"

    def create(self, validated_data):
        certificates = validated_data.pop("certificates")
        created_institution = CertifyingInstitution.objects.create(
            **validated_data
        )
        for certificate in certificates:
            certificate_data = {
                "name": certificate["name"],
                "certifying_institution": created_institution,
            }
            CertificateSerializer().create(validated_data=certificate_data)
        return created_institution
