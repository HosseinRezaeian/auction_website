from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_jalali.forms import jDateField,jDateTimeField
from django_jalali.admin.widgets import AdminjDateWidget,AdminSplitjDateTime


class LoginForm(forms.Form):
    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={'class': 'w-52 h-7 border border-black rounded-lg px-2 py-1', 'dir': 'ltr'}))

    password = forms.CharField(
        label="کلمه عبور",
        widget=forms.PasswordInput(attrs={'class': 'w-52 h-7 border border-black rounded-lg px-2 py-1', 'dir': 'ltr'}))


class SingupForm(forms.Form):
    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={'class': 'w-52 h-7 border border-black rounded-lg px-2 py-1', 'dir': 'ltr'}))

    name = forms.CharField(
        label='نام ',
        widget=forms.TextInput(attrs={'class': 'w-52 h-7 border border-black rounded-lg px-2 py-1', 'dir': 'ltr'}))

    email = forms.CharField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'class': 'w-52 h-7 border border-black rounded-lg px-2 py-1', 'dir': 'ltr'}))

    phone = forms.CharField(
        label='شماره تلفن',
        widget=forms.TextInput(attrs={'class': 'w-52 h-7 border border-black rounded-lg px-2 py-1', 'dir': 'ltr'}))

    password = forms.CharField(
        label="کلمه عبور",
        widget=forms.PasswordInput(attrs={'class': 'w-52 h-7 border border-black rounded-lg px-2 py-1', 'dir': 'ltr'}))


class AddDocument(forms.Form):
    datefrom = jDateField(
        label="تاریخ شروع",
        widget=AdminjDateWidget())

    dateto = jDateField(
        label="تاریخ پایان",
        widget=AdminjDateWidget())

    def clean(self):
        datefrom = self.cleaned_data.get('datefrom')
        dateto = self.cleaned_data.get('dateto')

    fileupload = forms.FileField(label='انتخاب فایل', widget=forms.FileInput())

    class Meta:
        fields = ['fileupload', 'datefrom', 'dateto']
        widgets = {
            'datefrom': forms.DateInput(attrs={'type': 'date'}),
            'dateto': forms.DateInput(attrs={'type': 'date'}),
        }


class AddPost(forms.Form):
    name = forms.CharField(
        label='نام',
        widget=forms.TextInput(attrs={
            'class': 'block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6',
            'dir': 'ltr'
        })
    )

    discription = forms.CharField(
        label='تـوضیــحات',
        widget=forms.TextInput(attrs={
            'class': 'block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6',
            'dir': 'ltr'
        })
    )

    price = forms.IntegerField(
        label='قیمت',
        widget=forms.TextInput(attrs={
            'class': 'block w-full rounded-md border-0 px-3.5 py-2 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6',
            'dir': 'ltr'
        })
    )

    device_project_choices = forms.ChoiceField(
        choices=[('2', 'مزایده انگلیسی '), ('1', 'مزایده عمومی')],
        label='نوع'
    )

    # pic = forms.FileField(widget=forms.TextInput(attrs={
    #     "name": "images",
    #     "type": "File",
    #     "class": "form-control",
    #     "multiple": "True",
    #     'accept': 'image/*'
    # }), label="")

    datefrom = jDateTimeField(
        label="تاریخ شروع",
        widget=AdminSplitjDateTime()
    )

    dateto = jDateTimeField(
        label="تاریخ پایان",
        widget=AdminSplitjDateTime()
    )

