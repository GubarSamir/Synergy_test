import datetime

from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(null=True, blank=True)
    headman = models.OneToOneField(
        'users.User',
        on_delete=models.SET_NULL,
        null=True,
        related_name='headed_group'
    )


    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
