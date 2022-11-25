from django.db import models

from skymarkets import settings


class Ad(models.Model):
    image = models.ImageField(
        upload_to="images/",
        verbose_name="фото",
        help_text="Разместите фото для объявления",
        null=True,
        blank=True)
    title = models.CharField(
        max_length=200,
        verbose_name="Название товара",
        help_text="Введите название товара"
    )
    price = models.PositiveIntegerField(
        verbose_name="Цена товара",
        help_text="Введите цену товара"
    )
    description = models.TextField(
        max_length=1000,
        verbose_name="Описание товара",
        help_text="Напишите описание товара"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="ads"
    )
    created_at = models.DateTimeField(
        default=False,
        blank=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Comment(models.Model):
    text = models.CharField(
        max_length=2000,
        verbose_name="Комментарий",
        help_text="Напишите комментарий",
        null=True,
        blank=True
    )
    author = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        related_name="ads"
    )
    ad = models.ForeignKey(
        Ad,
        on_delete=models.CASCADE,
        null=True
    )
    created_at = models.DateTimeField(
        default=False,
        blank=True
    )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
