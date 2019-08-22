from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,AccessRecord,Webpage
from . import forms
# Create your views here.
def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_records": webpages_list}
    #my_dict={'insert_me':"hello i am from moved views.py"}
    return render(request,'first_app/index.html',date_dict)
def form_name(request):
    form = forms.Formname()
    if request.method=="POST":
        form = forms.Formname(request.POST)
        if form.is_valid():
            print("Validation success")
            print("Name "+form.cleaned_data['name'])
            print("Email "+form.cleaned_data['email'])
            print("Text "+form.cleaned_data['text'])
    return render(request,'first_app/form_page.html',{'form':form})
