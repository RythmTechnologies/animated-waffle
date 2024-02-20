from django.db import models
from apps.main.mixin import TimeBasedStampModel, MyS3Storage


class Main(TimeBasedStampModel):
  title = models.CharField(("Anasayfa İçerik Başlık"), max_length=50)
  short_title = models.CharField(("Anasayfa İçerik Kısa Yazı"), max_length=50)
  image = models.ImageField(("Anasayfa İçerik Resim"), upload_to="anasayfa/",storage=MyS3Storage(), height_field=None, width_field=None, max_length=None)

  class Meta:
    verbose_name="Ana Sayfa"
    verbose_name_plural="Ana Sayfa Tasarımları"

  def __str__(self) -> str:
      return self.title

class Logo(TimeBasedStampModel):
  name = models.CharField(("Logo Adı"), max_length=50)
  image = models.ImageField(("Logo"), upload_to="logo/",storage=MyS3Storage(), height_field=None, width_field=None, max_length=None)

  class Meta:
    verbose_name="Logo"
    verbose_name_plural="Site Logo"

  def __str__(self) -> str:
      return self.name