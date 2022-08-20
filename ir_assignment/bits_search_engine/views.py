import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View

# Create your views here.
class Dash(View):

    def __init__(self) -> None:
        self.d = {}

    def get(self, request): # initial landing page or dashboard
        return render(request, 'dash.html', self.d)

    def post(self, request): # search in the existing corpus/video files
        pass


class PostVideos(View):

    def __init__(self) -> None:
        self.d = {}

    def post(self, request): # uploading new video files
        pass

    

