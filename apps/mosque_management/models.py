from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class MediaImage(models.Model):

    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return "user_{0}/{1}".format("main", filename)

    image = models.FileField(upload_to=user_directory_path, blank=True, null=True)


class MediaFile(models.Model):

    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        filename = instance.name if instance.name else filename
        return "user_{0}/{1}".format("main", filename)

    name = models.CharField(
        verbose_name=_("File Name"), blank=True, null=True, max_length=500
    )
    file = models.FileField(upload_to=user_directory_path, blank=True, null=True)
    date_uploaded = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Mosque(models.Model):
    name = models.CharField(verbose_name=_("Mosque Name"), max_length=250)
    tel = PhoneNumberField(
        verbose_name=_("Phone Number"),
        blank=True,
        null=True,
    )
    mail = models.EmailField(
        verbose_name=_("Email Address"),
        blank=True,
        null=True,
    )
    imam = models.CharField(
        verbose_name=_("Imam's Name"), max_length=250
    )  # make the name of the imam a foreign key with the imam user/profile
    location = models.CharField(max_length=250,  blank=True, verbose_name=_("Mosque Location"))

    # mosque_image = models.ManyToManyField(
    #     MediaImage, blank=True, related_name="mosque_image"
    # )
    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return "{0}/{1}".format("mosque files", filename)

    image = models.FileField(upload_to=user_directory_path, blank=True, null=True)
    certificate = models.FileField(upload_to=user_directory_path, blank=True, null=True)

    additional_info = models.TextField(verbose_name=_("Content"), blank=True, null=True)

    def __str__(self):
        return self.name if self.name else ""


class PrayerTime(models.Model):
    title = models.CharField(max_length=250, default="n/a")
    time = models.TimeField(max_length=250, default="n/a")
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title


class Sermon(models.Model):
    class SermonType(models.TextChoices):
        audio = "AUDIO", _("Audio")
        video = "VIDEO", _("video")
        document = "DOCUMENT", _("Document")

    title = models.CharField(max_length=250, default="n/a")
    description = models.TextField(max_length=500, blank=True, null=True)
    speaker_name = models.CharField(max_length=250, default="n/a")
    sermon_type = models.CharField(
        choices=SermonType.choices, max_length=50, default="n/a"
    )
    docs = models.ManyToManyField(MediaFile, blank=True, related_name="sermon_docs")
    audio = models.ManyToManyField(MediaFile, blank=True, related_name="sermon_audio")
    video = models.ManyToManyField(MediaFile, blank=True, related_name="sermon_video")
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.speaker_name}"


class Annoucement(models.Model):
    title = models.CharField(max_length=250, default="n/a")
    description = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    location = models.PointField(blank=True, null=True)

    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return "{0}/{1}".format("annoucement image", filename)

    image = models.FileField(upload_to="user_directory_path", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
