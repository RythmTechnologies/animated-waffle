from django.db import models
from apps.main.mixin import TimeBasedStampModel, MyS3Storage
from tinymce.models import HTMLField
from autoslug import AutoSlugField


class Photos(models.Model):
   image = models.ImageField(("Resimler"), upload_to="projects/images/",storage=MyS3Storage(), height_field=None, width_field=None, max_length=None)
   class Meta:
    verbose_name = "Proje Resim"
    verbose_name_plural = "Projeye Ait Resimler"

    def __str__(self) -> str:
        return str(self.image.url)

class Projects(TimeBasedStampModel):
  name = models.CharField(("Proje Adı"), max_length=50)
  image = models.ImageField(("Proje Resmi"), upload_to="projects/",storage=MyS3Storage(),height_field=None, width_field=None, max_length=None)
  descriptions = HTMLField(("Proje Açıklaması"))
  type = models.CharField(("Proje Türü"), max_length=50)
  location = models.CharField(("Proje Konumu"), max_length=50)
  date = models.DateField(("Proje Yapılma Tarihi"), auto_now=False, auto_now_add=False)
  slug = AutoSlugField(
        populate_from="name", editable=False, always_update=True, blank=True
    )
  projects_image = models.ManyToManyField(Photos, verbose_name=("Proje Resimleri"), blank=True)

  class Meta:
    verbose_name = "Proje"
    verbose_name_plural = "Projeler"

  def __str__(self) -> str:
      return self.name

