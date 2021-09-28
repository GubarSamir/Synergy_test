import datetime

from django.core.exceptions import ValidationError
from django.forms import ModelForm, DateInput

from users.models import User
import django_filters


class UserBaseForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'age',
            'birthdate',
            'enroll_date',
            'graduate_date',
            'group',
        ]
        # fields = '__all__'
        widgets = {'birthdate': DateInput(attrs={'type': 'date'})}

    @staticmethod
    def normalize_name(value):
        return value.lower().capitalize()

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        result = self.normalize_name(first_name)
        return result

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        result = self.normalize_name(last_name)
        return result

    # def clean_birthdate(self):
    #     birthdate = self.cleaned_data['birthdate']
    #     age = datetime.datetime.now().year - birthdate.year
    #     if age < 18:
    #         raise ValidationError('Age should be greater than 18 y.o.')
    #
    #     return birthdate

    def clean(self):
        enroll_date = self.cleaned_data['enroll_date']
        graduate_date = self.cleaned_data['graduate_date']
        if enroll_date > graduate_date:
            raise ValidationError('Enroll date coudnt be greater than graduate date!')


class UserCreateForm(UserBaseForm):
    class Meta(UserBaseForm.Meta):
        fields = [
            'first_name',
            'last_name',
            'birthdate',
            'enroll_date',
            'graduate_date',
        ]


class UserUpdateForm(UserBaseForm):
    class Meta(UserBaseForm.Meta):
        # fields = [
        #     'first_name',
        #     'last_name',
        #     # 'age',
        #     'birthdate',
        #     # 'enroll_date',
        #     # 'graduate_date',
        #     # 'graduate_date2',
        # ]
        fields = '__all__'


class usersFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'age': ['lt', 'gt'],
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
        }
