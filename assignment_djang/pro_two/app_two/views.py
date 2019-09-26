from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
#     my_dict = {'insert_me':"I am smelling some otu here"}
#     return render(request, "app_two/index.html", context=my_dict)

# We are going to be connecting views to the database.
from app_two.models import AccessRecord, Webpage, Topic

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict ={'access_record':webpages_list}
    return render(request, 'app_two/index.html', context=date_dict)
