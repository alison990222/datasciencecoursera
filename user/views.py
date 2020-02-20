from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import coders
from django.views.decorators.http import require_http_methods

# def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")


@require_http_methods(["GET"])
def getUserInfo(request):
    context = {}
    try:
        userID = request.GET.get('id')
        user = coders.objects.get(id=userID)
        context['userID'] = userID
        context['name'] = user.username
        context['msg'] = "success"
        context['errorNum'] = 0
    except Exception as e:
        context['msg'] = str(e)
        context['errorNum'] = 1
        # raise Http404(e)
    return render(request, 'index.html', context)
    # return HttpResponse(json.dumps(data), content_type="application/json")


@require_http_methods(["GET"])
def getHomePage(request):
    context = {}
    return render(request, 'base.html', context)
