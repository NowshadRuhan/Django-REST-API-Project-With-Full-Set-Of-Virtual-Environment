from django.shortcuts import render
import requests
# Create your views here.
def IndexView(request):
    user = False
    if request.method == "POST":
        username = request.POST.get('username')
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        user = response.json()
    diction = {
        'title':'Home | API EXAMPLE',
        'text':'API example with Virtual Enviroment',
        'text1':'Github API',
        'user':user
    }
    return render(request, 'index.html', context=diction)
