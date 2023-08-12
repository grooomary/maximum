from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.utils.html import format_html


class Advertisement(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, есть ли торг')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.create_at.date() == timezone.now().date():
            created_time = self.create_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color: green; font-weight: 700;">Сегодня в {}</span>', created_time)
        return self.create_at.strftime("%d.%m.%Y в %H:%M:%S")

    @admin.display(description='Дата обновления')
    def updated_date(self):
        if self.update_at.date() == timezone.now().date():
            updated_time = self.update_at.time().strftime("%H:%M:%S")
            return format_html('<span style="color: #C74247; font-weight: 700;">Сегодня в {}</span>', updated_time)
        return self.update_at.strftime("%d.%m.%Y в %H:%M:%S")

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, ' \
               f'title={self.title}, price={self.price})>'

'''
Название
Цена
Описание
Дата создания
Дата обновления
Торг
'''