from django.db import models
from django.core.validators import MaxLengthValidator


# Create your models here.
class Profile(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[MaxLengthValidator(limit_value=500)],
        null=False,
        blank=False,
    )
    github = models.URLField(
        validators=[MaxLengthValidator(limit_value=500)],
        null=False,
        blank=False,
    )
    linkedin = models.URLField(
        validators=[MaxLengthValidator(limit_value=500)],
        null=False,
        blank=False,
    )
    bio = models.TextField(
        validators=[MaxLengthValidator(limit_value=500)],
        null=False,
        blank=False,
    )

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    name = models.CharField(
        max_length=50,
        validators=[MaxLengthValidator(limit_value=500)],
        null=False,
        blank=False,
    )
    description = models.TextField(
        max_length=500,
        validators=[MaxLengthValidator(limit_value=500)],
        null=False,
        blank=False,
    )
    github_url = models.URLField(
        validators=[MaxLengthValidator(limit_value=500)],
        null=False,
        blank=False,
    )
    keyword = models.CharField(
        validators=[MaxLengthValidator(limit_value=500)],
        max_length=50,
        null=False,
        blank=False,
    )
    key_skill = models.CharField(
        validators=[MaxLengthValidator(limit_value=500)],
        max_length=50,
        null=False,
        blank=False,
    )
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="projects",
    )

    def __str__(self) -> str:
        return self.name


class CertifyingInstitution(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[MaxLengthValidator(limit_value=500)],
        null=False,
        blank=False,
    )
    url = models.URLField(
        validators=[MaxLengthValidator(limit_value=500)],
        null=False,
        blank=False,
    )

    def __str__(self) -> str:
        return self.name


class Certificate(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[MaxLengthValidator(limit_value=500)],
        null=False,
        blank=False,
    )
    certifying_institution = models.ForeignKey(
        CertifyingInstitution,
        on_delete=models.CASCADE,
        related_name="certificates"
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        validators=[MaxLengthValidator(limit_value=500)],
        null=False,
        blank=False,
    )
    profiles = models.ManyToManyField(
        Profile,
        related_name="certificates",
    )

    def __str__(self) -> str:
        return self.name
