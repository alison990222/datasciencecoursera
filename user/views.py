from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import coders
from django.views.decorators.http import require_http_methods

# def index(request):
# return HttpResponse("Hello, world. You're at the polls index.")


def getUserInfo(request):
    context = {}
    if request.method == 'GET':
        print("get")
        try:
            userID = request.GET.get('id')
            user = coders.objects.get(id=userID)
            industryType = user.industryType.split(',')
            skillType = user.skillType.split(',')
            experience = user.experience.all()
            project = user.project.all()
            context['userID'] = userID
            context['name'] = user.username
            context['industryType'] = industryType
            context['skillType'] = skillType
            context['location'] = user.location
            context['experience'] = experience
            context['project'] = project
            context['github'] = user.github
            context['msg'] = "success"
            context['errorNum'] = 0

        except Exception as e:
            context['msg'] = str(e)
            context['errorNum'] = 1
            # raise Http404(e)
        return render(request, 'index.html', context)
        # return HttpResponse(json.dumps(data), content_type="application/json")
    # elif request.method == 'POST':
    #     print("post")
    #     try:
    #         # data = request.POST -> this line gets all the data
    #         userID = request.POST["id"] # ["username"]
    #         user = coders.objects.get(id=userID)
    #         print(request.POST)
    #         #user.username = request.POST["username"] 
    #         user.save()
    #         industryType = user.industryType.split(',')
    #         skillType = user.skillType.split(',')
    #         experience = user.experience.all()
    #         project = user.project.all()
    #         context['userID'] = userID
    #         context['name'] = user.username
    #         context['industryType'] = industryType
    #         context['skillType'] = skillType
    #         context['location'] = user.location
    #         context['experience'] = experience
    #         context['project'] = project
    #         context['msg'] = "success"
    #         context['errorNum'] = 0
    #     except Exception as e:
    #         print("there")
    #         context['msg'] = str(e)
    #         context['errorNum'] = 1
    #     return render(request, 'index.html', context)


@require_http_methods(["GET"])
def getHomePage(request):
    context = {}
    return render(request, 'base.html', context)


@require_http_methods(["POST"])
def editProfile(request):
    context = {}
    try:
        # data = request.POST -> this line gets all the data
        userID = request.POST["id"] # ["username"]
        user = coders.objects.get(id=userID)
        print(request.POST)
        user.username = request.POST["username"] 
        user.workType = request.POST.getlist("workType")
        #TODO: format of worktype 
        user.save()
        industryType = user.industryType.split(',')
        skillType = user.skillType.split(',')
        experience = user.experience.all()
        project = user.project.all()
        context['userID'] = userID
        context['name'] = user.username
        context['industryType'] = industryType
        context['workType'] = user.workType
        context['skillType'] = skillType
        context['location'] = user.location
        context['experience'] = experience
        context['project'] = project
        context['msg'] = "success"
        context['errorNum'] = 0
    except Exception as e:
        print("there")
        context['msg'] = str(e)
        context['errorNum'] = 1
    return render(request, 'index.html', context)
