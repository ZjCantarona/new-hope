from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from users.models import UserProfile

@login_required
def index(request):
    return HttpResponse('<h1>Django Include URLs</h1>')
    template = "index.html"
    try:
        profile = UserProfile.objects.get_or_create(user=request.user)
    except:
        profile = None
    context = {"home_active": "active", "profile": profile}
    return render(request, template, context)


"""@login_required
def search(request):
    template = "index.html"
    """
