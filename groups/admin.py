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

    # readonly_fields = fields
    # show_change_link = True             # edit in User model

    extra = 0               # default = 3


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
