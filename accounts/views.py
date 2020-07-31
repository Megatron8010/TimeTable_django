from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from django.forms import CheckboxSelectMultiple, CheckboxInput, DateInput
from accounts.models import Movie,TableUser
from funky_sheets.formsets import HotView
from rest_framework import viewsets
from rest_framework.decorators import api_view,authentication_classes
from accounts.serializers import DataSerializer
from django.http import HttpResponseRedirect, HttpResponse,JsonResponse
from rest_framework.permissions import IsAuthenticated
from django.contrib import messages
    


class CreateMovieView(HotView):
    # Define model to be used by the view
    model = Movie
    # Define template
    template_name = 'create.html'
    # Define custom characters/strings for checked/unchecked checkboxes
    checkbox_checked = 'yes' # default: true
    checkbox_unchecked = 'no' # default: false
    # Define prefix for the formset which is constructed from Handsontable spreadsheet on submission
    prefix = 'table'
    # Define success URL
    success_url = reverse_lazy('update')
    # Define fields to be included as columns into the Handsontable spreadsheet
    fields = (
        'director',
        'title',
        'ratings',
        'imdb_link',
        'cast',
    )
    # Define extra formset factory kwargs
    factory_kwargs = {
        'widgets': {
            'release_date': DateInput(attrs={'type': 'date'}),
            'genre': CheckboxSelectMultiple(),
            'parents_guide': CheckboxInput(),
        }
    }
    # Define Handsontable settings as defined in Handsontable docs
    hot_settings = {
        'autoWrapRow': 'true',
        'startRows': '5',
        'startCols': '5',
        'rowHeaders': 'true',
        'contextMenu': 'true',
        'licenseKey': 'non-commercial-and-evaluation',
        'search': 'true',
        # When value is dictionary don't wrap it in quotes
        'headerTooltips': {
            'rows': 'false',
            'columns': 'true'
        }
    }

class UpdateMovieView(CreateMovieView):
  template_name = 'update.html'
  # Define 'update' action
  action = 'update'
  # Define 'update' button
  button_text = 'Update'

# @api_view(['GET'])
# def my_view(request):
#     print("random stuff")
#     return JsonResponse({'username': request.user.username})
    
# Create your views here.
def indexView(request):
    return render(request,'index.html')

@login_required
def dashboardView(request):
    return render(request,'dashboard.html')

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #login(request,user)
            return redirect('signin')
    else:
            form = UserCreationForm()
    return render(request,'register.html',{"form": form})

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('create')
            else:
                messages.error(request,'username or password not correct')
        else:
            messages.error(request,'username or password not correct')
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'