from django.db import models
from apps.main.mixin import TimeBasedStampModel


class Contact(TimeBasedStampModel):
    name = models.CharField(("Adı"), max_length=50)
    surname = models.CharField(("Soyadı"), max_length=50)
    email = models.EmailField(("Email Adresi"), max_length=254)
    message = models.TextField(("Mesaj İçeriği"))

    class Meta:
        verbose_name = "İletişim"
        verbose_name_plural = "İletişimler"

    def __str__(self) -> str:
        return f"{self.name} - {self.email}"


class CompanyInfo(TimeBasedStampModel):
    address = models.TextField(("Şirket Adresi"))
    phone = models.CharField(("Telefon Numarası"), max_length=50)
    email = models.EmailField(("Email Adresi"), max_length=254)

    class Meta:
        verbose_name = "Şirket"
        verbose_name_plural = "Şirket Bilgisi"

    def __str__(self) -> str:
        return self.address
