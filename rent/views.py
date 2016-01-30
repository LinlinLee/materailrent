from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def rent_index(request):
    context = {
	'test': 'just for test.',
        'welcome': 'hello world.'
    }
    return render(request, 'rent_index.html')

