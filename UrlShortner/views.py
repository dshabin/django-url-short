from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .forms import UrlForm
from .models import Url
import random
from django.contrib.auth.models import User
import base64
from django.http import JsonResponse
from django.shortcuts import redirect


def shortner(request):
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data['url']
            all_users = User.objects.all()
            random_user = all_users[random.randint(0,len(all_users)-1)]
            query = Url.objects.filter(address=address)
            if query :
                encoded_url =base64.b64encode(address.encode())
                return HttpResponseRedirect('/' + encoded_url.decode("utf-8") )
            url_object = Url(address=address,submitter=random_user)
            url_object.save()
            encoded_url =base64.b64encode(address.encode())
            return HttpResponseRedirect('/' + encoded_url.decode("utf-8") )
    else:
        form = UrlForm()

    return render(request, 'shortner/index.html', {'form': form})

def show_info(request):
    encoded_url = request.META['PATH_INFO'].split('!')[1]
    decoded_url = base64.b64decode(encoded_url)
    url_object = Url.objects.filter(address=decoded_url)[0]
    data = {}
    data['first_name'] =  url_object.submitter.first_name
    data['visit_counter'] = url_object.visit_counter
    return JsonResponse(data)

def resolver(request):
    encoded_url = request.META['PATH_INFO'].split('/')[1]
    decoded_url = base64.b64decode(encoded_url)
    url_object = Url.objects.filter(address=decoded_url)[0]
    visit_counter = int(url_object.visit_counter)
    visit_counter += 1
    url_object.visit_counter = str(visit_counter)
    url_object.save()
    return JsonResponse({"message" : "I have to redirect to " + str(decoded_url) + ". See the browser address bar for encoded url. "})
