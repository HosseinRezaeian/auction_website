from django.shortcuts import render, redirect

from django.views import View
from . import forms
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser, Documents
from products.models import ProductOrService
import jdatetime


# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('homepage')


class Login(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'usermodel/Login.html', {'form': forms.LoginForm})

    def post(self, request, *args, **kwargs):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('homepage')
            else:
                form = forms.LoginForm()
                return redirect('login')

        else:
            form = forms.LoginForm()
            return render(request, 'login.html', {'form': form})


class Singup(View):
    def get(self, request):
        return render(request, 'usermodel/Singup.html', {'form': forms.SingupForm})

    def post(self, request, *args, **kwargs):
        form = forms.SingupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            if CustomUser.objects.filter(name=name) or CustomUser.objects.filter(username=username):
                return render(request, 'usermodel/signup.html', {'form': form})
            else:
                CustomUser.objects.create_user(username=username, name=name, email=email,is_staff=True, phone=phone,
                                               password=password)
            return redirect('homepage')  # Change 'success_page' to your success URL
        else:
            return render(request, 'usermodel/signup.html', {'form': form})


def profile(request):
    return render(request, 'usermodel/info.html')


def documents(request):
    return render(request, 'usermodel/adddocument.html')


class DocumentView(View):
    def get(self, request):
        return render(request, 'usermodel/adddocument.html', {'form': forms.AddDocument})

    def post(self, request, *args, **kwargs):
        form = forms.AddDocument(request.POST, request.FILES)  # Include request.FILES for file upload
        if form.is_valid():
            fileupload = form.cleaned_data['fileupload']
            datefrom = jdatetime.datetime.strptime(str(form.cleaned_data['datefrom']), '%Y-%m-%d').togregorian().date()
            dateto = jdatetime.datetime.strptime(str(form.cleaned_data['dateto']), '%Y-%m-%d').togregorian().date()

            doc = Documents.objects.create(document=fileupload, date_from=str(datefrom), date_to=str(dateto),
                                           user=request.user)
            doc.save()
            # Redirect to a success page or another view
        return render(request, 'usermodel/adddocument.html', {'form': form})


class PostAuction(View):
    def get(self, request):
        return render(request, 'usermodel/addpost.html', {'form': forms.AddPost})

    def post(self, request, *args, **kwargs):
        form = forms.AddPost(request.POST,request.FILES)
        if form.is_valid():
            datefrom = form.cleaned_data['datefrom']
            dateto = form.cleaned_data['dateto']
            discription = form.cleaned_data['discription']
            # device_project_choices = form.cleaned_data['device_project_choices']
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']

            product = ProductOrService.objects.create(start_date=datefrom, end_date=dateto, description=str(discription),
                                           auctioneer=request.user,title=name,base_price=price)
            product.save()
        return render(request, 'usermodel/addpost.html', {'form': form})
