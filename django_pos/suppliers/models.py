from django.db import models

# Create your models here.


class Supplier(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    kra_pin = models.CharField(max_length=11, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to="suppliers/", blank=True, null=True)

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "email": self.email,
            "kra_pin": self.kra_pin,
            "website": self.website,
            "logo": self.logo.url if self.logo else "",
        }

    class Meta:
        ordering = ["name"]
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"
        db_table = "Suppliers"
