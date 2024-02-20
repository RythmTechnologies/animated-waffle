from django.db import models
from apps.main.mixin import TimeBasedStampModel
from tinymce.models import HTMLField

class About(TimeBasedStampModel):
  title = models.CharField(("Hakkımızda Başlık"), max_length=150)
  content = HTMLField(("Hakkımızda İçerik"))

  class Meta:
    verbose_name = "Hakkımızda"
    verbose_name_plural = "Hakkımızda Yazıları"

  def __str__(self) -> str:
      return self.title


