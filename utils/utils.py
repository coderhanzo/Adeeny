import magic
from drf_extra_fields.fields import Base64FileField

"""
this will encode files to base64 and check mime. 
used in serialisers not models
"""

class Base64File(Base64FileField):
  ALLOWED_TYPES = ("pdf", "jpg", "jpeg", "png")

  def get_file_extension(self, filename, decoded_file):
    mime_type = magic.from_buffer(decoded_file, mime=True)

    return mime_type.split("/")[1]