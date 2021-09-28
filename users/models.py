import datetime
from django.db import models
from groups.models import Group
from core.models import Person


class User(Person):
    enroll_date = models.DateField(default=datetime.date.today)
    graduate_date = models.DateField(default=datetime.date.today)
    graduate_date2 = models.DateField(default=datetime.date.today)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='users')

    def __str__(self):
        return f'{self.full_name()}, {self.birthdate}, {self.id}, {self.group}'

