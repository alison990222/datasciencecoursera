from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import *
from .models import company as cpy
from .models import job as jobModel
from django.views.decorators.http import require_http_methods
from django.utils import timezone

def getCompanyInfo(request, companyID):
    context = {}
    if request.method == 'POST':
        print(request.POST)
        try:
            compID = request.POST["id"] 
            comp = cpy.objects.get(id=compID)
            postForm = request.POST["form"]
            if postForm == "apply":
                position = request.POST["position"]
                appliObj = application(
                    feedback = request.POST["detail"],
                )
                appliObj.save()

                # appliObj.company = comp
                # comp.company_appli.add(appliObj)
                # appliObj.job = jobModel.objects.get(name=position)
                # jobModel.objects.get(name=position).job_appli.add(appliObj)

        except Exception as e:
            context['msg'] = str(e)
            context['errorNum'] = 1
        
    try:
        comp = cpy.objects.get(id=companyID)

        applicationObj = comp.company_appli.all()
        appliList = []
        for appli in applicationObj:
            appliList.append({
                'applicant': appli.coder.username,
                'job': appli.job.name,
                'time': appli.time.strftime("%Y-%m-%d %H:%M:%S"),
            })

        jobObj = comp.job.all()
        jobList = []
        for job in jobObj:
            jobList.append({
                'id':job.id,
                'name': job.name,
                'mission': job.teamMission,
                'stage': job.currentStage,
                'quali': job.qualification,
                'work': job.work,
                'team': job.teamCulture,
                'contact': job.contact,
            })

        basicInfo= [{
            'item': "Founded Date" ,
            'content': comp.foundDate.strftime("%Y-%m"),
        },{
            'item': "Company Size",
            'content': comp.companySize,
        },{
            'item': "Last Funding Type",
            'content': comp.fundingType,
        },{
            'item': "Job Type",
            'content': comp.jobType,
        }]
        context['cpy'] = comp
        context['appli'] = appliList
        context['basicInfo'] = basicInfo
        context['jobList'] = jobList

        context['msg'] = "success"
        context['errorNum'] = 0
    except Exception as e:
        context['msg'] = str(e)
        context['errorNum'] = 1
    return render(request, 'company.html', context)



def getUserInfo(request, userID):
    context = {}
    context['username'] = userID
    if request.method == 'POST':
        try:
            # data = request.POST -> this line gets all the data
            userID = request.POST["id"]  # ["username"]
            user = coders.objects.get(id=userID)
            postForm = request.POST["form"]
            print(request.POST)
            if postForm == "personalInfo":
                username = request.POST["username"]
                location = request.POST["location"]
                position = request.POST["position"]
                workType = request.POST.getlist("workType")
                linkedin = request.POST["linkedin"]
                github = request.POST["github"]
                stack = request.POST["stack"]
                email = request.POST["email"]
                if username:
                    user.username = username
                if location:
                    user.location = location
                if position:
                    user.position = position
                if workType:
                    user.workType = workType
                if linkedin:
                    user.linkedin = linkedin
                if github:
                    user.github = github
                if stack:
                    user.stackoverflow = stack
                if email:
                    user.email = email
                user.save()
            if postForm == "addExp":
                industry = request.POST.getlist("industry")

                datefrom = request.POST["datefrom"]
                dateto = request.POST["dateto"]
                company = request.POST["company"]
                if company:
                    expObj = experienceInfo(
                        company=company,
                    )
                    
                    expObj.position = request.POST["position"]
                    expObj.field = request.POST["field"]
                    # if datefrom:
                    #     expObj.time = datefrom
                    expObj.detail = request.POST["detail"]
                    expObj.save()
                    expObj.coder = coders.objects.get(id=userID)
                    coders.objects.get(id=userID).experience.add(expObj)
                if industry:
                    user.industryType = industry

            if postForm == "editExp":
                expid = request.POST["expid"]
                expObj = experienceInfo.objects.get(id=expid)
                expObj.company = request.POST["company"]
                expObj.position = request.POST["position"]
                expObj.detail = request.POST["detail"]
                expObj.save()

            if postForm == "addPro":
                name = request.POST["name"]
                skillType = request.POST.getlist("skillType")
                if name:
                    Obj = projectInfo(
                        name=name,
                    )
                    # Obj.time = request.POST["date"]
                    Obj.detail = request.POST["detail"]
                    Obj.field = request.POST["field"]
                    Obj.github = request.POST["github"]
                    Obj.save()
                    Obj.coder = coders.objects.get(id=userID)
                    coders.objects.get(id=userID).project.add(Obj)
                if skillType:
                    user.skillType = skillType

            if postForm == "editPro":
                proid = request.POST["Proid"]
                proObj = projectInfo.objects.get(id=proid)
                proObj.name = request.POST["name"]
                proObj.detail = request.POST["detail"]
                proObj.save()

            if postForm == "addOther":
                name = request.POST["name"]
                detail = request.POST["detail"]
                if name:
                    Obj = otherInfo(
                        name=name,
                    )
                    Obj.save()
                    Obj.coder = coders.objects.get(id=userID)
                    coders.objects.get(id=userID).otherInfo.add(Obj)

            user.save()

        except Exception as e:
            if request.user.is_authenticated and request.user.username == userID:
                print(str(e))
                user = coders()
                user.username = userID
                user.save()
            context['msg'] = "success create"
            context['msg'] = str(e)
            context['errorNum'] = 1
    # if request.method == 'GET':
    try:
        user = coders.objects.get(username=userID)

        industryType = user.industryType
        if industryType:
            user.industryType = industryType.split(',')
        skillType = user.skillType
        if skillType:
            user.skillType = skillType.split(',')
        workType = user.workType
        if workType:
            user.workType = workType.split(',')

        applicationObj = user.coder_appli.all()
        appliList = []
        for appli in applicationObj:
            appliList.append({
                'company': appli.company.name,
                'job': appli.job.name,
                'time': appli.time.strftime("%Y-%m-%d %H:%M:%S"),
                'status': appli.status,
            })

        experience = user.experience.all()
        experienceList = []
        for exp in experience:
            experienceList.append({
                'id': exp.id,
                'name': exp.position + " @ " + exp.company,
                'detail': exp.detail,
                'field': exp.field,
            })

        project = user.project.all()
        projectList = []
        for pro in project:
            projectList.append({
                'id': pro.id,
                'name': pro.name,
                'detail': pro.detail,
                'field': pro.field,
                'github': pro.github,
            })

        context['user'] = user
        context['workType'] = user.workType
        context['industryType'] = user.industryType
        context['skillType'] = user.skillType

        context['experience'] = experienceList
        context['project'] = projectList
        context['appli'] = appliList

        context['msg'] = "success"
        context['errorNum'] = 0

    except Exception as e:
        if request.user.is_authenticated and request.user.username == userID:
            print(str(e))
            user = coders()
            user.username = userID
            user.save()
            context['msg'] = "success create"
        context['msg'] = str(e)
        context['errorNum'] = 1
        # raise Http404(e)
        # return render(request, 'index.html', context)
    return render(request, 'index.html', context)


@require_http_methods(["GET"])
def getHomePage(request):
    context = {}
    return render(request, 'home.html', context)
