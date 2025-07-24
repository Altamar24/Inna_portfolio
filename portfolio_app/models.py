from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from PIL import Image


def validate_image_size(image):
    """Проверяет, что изображение имеет размер 610x890 пикселей"""
    img = Image.open(image)
    width, height = img.size
    if width != 610 or height != 890:
        raise ValidationError(
            _('Изображение должно быть размером 610x890 пикселей (получено: %(width)sx%(height)s)'),
            params={'width': width, 'height': height},
        )


class Contact(models.Model):
    title = models.CharField('Название', max_length=20)
    whatsapp_url = models.URLField('Ссылка на WhatsApp', null=True, max_length=200)
    instagram_url = models.URLField('Ссылка на Instagram', null=True, max_length=200)
    telegram_url = models.URLField('Ссылка на Telegram', null=True, max_length=200)
    phone_number = models.CharField('Номер телефона', null=True, max_length=20)
    mail = models.EmailField('Почта мэйл', null=True, max_length=50)
    address = models.CharField('Адрес', null=True, max_length=150)
    
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
    
    def __str__(self):
        return self.title
    

class Price(models.Model):
    name_service = models.CharField('Наименование услуги', max_length=60)
    price_service = models.CharField('Цена услуги', max_length=60)

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'
    
    def __str__(self):
        return self.name_service


class Photo(models.Model):
    name = models.CharField('Название изображения', max_length=100)
    image = models.ImageField(
        'Новое изображение', 
        upload_to='replaceable_images/', 
        validators=[validate_image_size], 
        help_text='Загрузите сюда новое изображение для замены'
        )
    name_service = models.CharField('Вид услуги', max_length=50, default='Wedding day',)
    description = models.TextField('Описание', max_length=50)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    def __str__(self):
        return self.name
    

class Question(models.Model):
    question_faq = models.CharField('Вопрос', max_length=150)
    answer_faq = models.CharField('Ответ', max_length=400)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
    
    def __str__(self):
        return self.question_faq