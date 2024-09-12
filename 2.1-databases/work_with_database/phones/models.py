from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    price = models.IntegerField(verbose_name="Стоимость")
    image = models.ImageField(verbose_name="Изображение")
    release_date = models.DateField(verbose_name="Дата выхода")
    lte_exists = models.BooleanField(default=False, verbose_name="LTE")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL")

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
