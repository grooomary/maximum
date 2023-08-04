from django.db import models

class Advert(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, есть ли торг')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
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