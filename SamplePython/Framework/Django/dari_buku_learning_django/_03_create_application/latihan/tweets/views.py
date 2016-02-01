from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from django.views.generic import View
from user_profile.models import User
from models import Tweet

class Index(View):
    def get(self, request):
        return render(request, 'base.html')
    
    def post(self, request):
        return HttpResponse('I am called from a post Request')

class Profile(View):
    """User Profile page reachable from /user/<username> URL"""
    def get(self, request, username):
        params = dict()()()
        user = User.objects.get(username=username)
        tweets = Tweet.objects.filter(user=user)
        params["tweets"] = tweets
        params["user"] = user
        return render(request, 'profile.html', params)

