from django.contrib import admin

from .models import Group
from users.models import User


class usersInlineTable(admin.TabularInline):
    model = User
    fields = [
        'last_name',
        'first_name',
        'email',
        'age',
    ]


    extra = 0


class GroupAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'start_date',
        'end_date',
        'headman',
    ]

    fields = [
        'name',
        ('start_date', 'end_date'),
        'headman',
        'teachers',
    ]

    inlines = [usersInlineTable]


admin.site.register(Group, GroupAdmin)
