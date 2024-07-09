from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.gis.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Coordinates(models.Model):
    region = models.CharField(verbose_name=_("Region"), max_length=250, default="n/a")
    city = models.CharField(verbose_name=_("City"), max_length=250, default="n/a")
    # location = models.PointField()

    def __str__(self) -> str:
        return self.location


class Mosque(models.Model):
    name = models.CharField(
        verbose_name=_("Mosque Name"), max_length=250, default="n/a"
    )
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
    name_imam = models.CharField(
        verbose_name=_("Imam's Name"), max_length=250, default="n/a"
    )  # make the name of the imam a foreign key with the imam user/profile
    location = models.ForeignKey(
        Coordinates, on_delete=models.CASCADE, blank=True, null=True
    )

    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return "{0}/{1}".format("mosque image", filename)

    mosque_image = models.FileField(
        upload_to=user_directory_path, blank=True, null=True
    )
    certificate = models.FileField(upload_to=user_directory_path, blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name if self.name else ""

class MediaFile(models.Model):
    MEDIA_TYPES = (
        ("audio", "Audio"),
        ("video", "Video"),
        ("profile_picture", "Profile Picture"),
    )
    title = models.CharField(max_length=255)
    file = models.FileField(
        upload_to="media/", blank=True, null=True
    )  # Default path, will be overridden
    media_type = models.CharField(max_length=20, choices=MEDIA_TYPES)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # File is new and not yet saved
            if self.media_type == "audio":
                self.file.field.upload_to = MediaFile.audio_upload_path(
                    self, self.file.name
                )
            elif self.media_type == "video":
                self.file.field.upload_to = MediaFile.video_upload_path(
                    self, self.file.name
                )
            elif self.media_type == "profile_picture":
                self.file.field.upload_to = MediaFile.profile_picture_upload_path(
                    self, self.file.name
                )
        super(MediaFile, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    @staticmethod
    def user_directory_path(instance, filename, media_type):
        # This method can be adjusted or removed if not directly used
        return "{0}/{1}".format(media_type, filename)

    @staticmethod
    def audio_upload_path(instance, filename):
        return "audios/{0}".format(filename)

    @staticmethod
    def video_upload_path(instance, filename):
        return "videos/{0}".format(filename)

    @staticmethod
    def profile_picture_upload_path(instance, filename):
        return "profile_pictures/{0}".format(filename)


class Sermon(models.Model):
    title = models.CharField(max_length=250, default="n/a")
    description = models.TextField(blank=True, null=True)
    speaker_name = models.CharField(max_length=250, default="n/a")
    sermon_type = models.CharField(max_length=250, default="n/a")
    audio = models.ManyToManyField(MediaFile, blank=True, related_name="sermon_audio")
    video = models.ManyToManyField(MediaFile, blank=True, related_name="sermon_video")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.speaker_name}"


class Annoucement(models.Model):
    title = models.CharField(max_length=250, default="n/a")
    description = models.TextField(blank=True, null=True)

    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return "{0}/{1}".format("annoucement image", filename)

    image = models.FileField(upload_to="annoucements/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
