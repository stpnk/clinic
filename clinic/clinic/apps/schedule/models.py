from django.db import models
from datetime import time

class Doctor(models.Model):
    """model for Doctor"""

    name = models.CharField(max_length=150, verbose_name='ФИО')
    specialization = models.CharField(max_length=100, verbose_name='Специализация')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Врач'


class Appointment(models.Model):
    """model for Appointment"""

    TIME_CHOICES = (
        (time(9,0), '09:00'),
        (time(10,0), '10:00'),
        (time(11,0), '11:00'),
        (time(12,0), '12:00'),
        (time(13,0), '13:00'),
        (time(14,0), '14:00'),
        (time(15,0), '15:00'),
        (time(16,0), '16:00'),
        (time(17,0), '17:00'),
    )

    doctor = models.ForeignKey(Doctor, verbose_name='Врач')
    name = models.CharField(max_length=150, verbose_name='ФИО')
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(choices=TIME_CHOICES, verbose_name='Время')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Запись'