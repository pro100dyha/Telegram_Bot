from django.db import models
from django.templatetags.static import static


class Property(models.Model):
    external_id = models.PositiveIntegerField(
        verbose_name='ID користувача',
        unique=True
    )
    name = models.CharField(max_length=128, verbose_name="Ім'я користувача")

    def __str__(self):
        return f'#{self.external_id}{self.name}'

    class Meta:
        verbose_name = "Профіль"


class Category(models.Model):
    property_prof = models.ForeignKey(
        Property,
        verbose_name='Профиль',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=128)
    image = models.ImageField(
        upload_to='categorys/',
        null=True,
        blank=True,
    )
    description = models.TextField(max_length=160, null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    property_prof = models.ForeignKey(
        Property,
        verbose_name='Профиль',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=128)
    number = models.PositiveIntegerField()
    min_description = models.TextField(max_length=160, null=True, blank=True)
    price = models.PositiveIntegerField()
    description = models.TextField(
        max_length=1024 * 4,
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        upload_to='products/',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товары"
        verbose_name_plural = "Товар"


class Description(models.Model):
    property_prof = models.ForeignKey(
        Property,
        verbose_name='Профиль',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        upload_to='description/',
        null=True,
        blank=True,
    )
    text = models.TextField(max_length=160, null=True, blank=True)
