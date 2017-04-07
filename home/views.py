from django.shortcuts import render
from django.http import HttpResponse, Http404

def index(request):
    context = {}
    context['request'] = request
    context['styles'] = ["style/css/main.css","style/css/mondrian.css"]
    context['cols'] = range(10)
    context['rows'] = range(5)
    context['sqrs'] = map(lambda x: {"sqr": x, "mess": ""}, range(8))
    context['sqrs'][0]["mess"]="GitHub"
    context['sqrs'][1]["mess"]="Click For A Brief Story About This Site"
    context['sqrs'][2]["mess"]="My LinkedIn"
    context['sqrs'][6]["mess"]="About Me"
    context['sqrs'][7]["mess"]="MrSusanovo"
    context['sqrs'][7]["mess1"]="Created for Dumping Junk Code."
    context['sqrs'][7]["mess2"]="(Current Page: Tribute to Mondrian.)"
    context['menu'] = ["Home","About", "Gallery","GitHub","Cool","Intro"]
    context['scripts'] =["js/bckgrd.js","js/menu.js","js/mondrian.js"]
    return render(request, "index.html", context)

def intro(request):
    context = {}
    context['request'] = request
    context['styles'] = ["style/css/main.css","style/css/mondrian.css"]
    context['title'] = "Initially This Website Was Expected To Be A Personal Webpage For Co-op Job Search.It Turns Out To Be A Bad Idea Especially I Started The Project Near The End Of Term.Hosting With Apache2 Cost Me 2 Assignments And 2 Nights. This Web Page Was Accessible To The Whole World 24 Hours After I Bought The Domain.Sorry, Except For North Korea And Probably Some Country Inside The Great Fire Wall. I Spent 60 Bucks On This Server, But This SH*T Does Not Even Worth That Much. I Mean At Least It Has To Be A Dynamic Website. Otherwise The Employers Won't Be Able To Tell The Difference Between Me And Those Who Do not Know What AJAX Is. Probably They Are Hosting Their Webpages On Github And Have Higher Marks Than I Do. There Will Be More, This Is Just A Beginning. I Am Tom Feng. Welcome To MrSusanovo. Further Funcionalities Under Construction.If You See This Scentence.Probably You Are Inside The Great Fire Wall."
    context['mainPart'] = ""
    context['menu'] = ["Home","About", "Gallery","GitHub","Cool","Other"]
    context['scripts'] =["js/title.js","js/bckgrd.js","js/mondrian.js"]
    return render(request, "intro.html", context)
    # return HttpResponse("currently underconstruction. Problems need to be solved: 1. Django static fil(css) not loaded , got 404. 2.Django template not working.")

def my_info(request):
    if request.is_ajax():
        context = {}
        context['content'] = " About Me Page(This is achieved by AJAX!). Upcomming, parallex scrolling personal webpage."
        return render(request, "about.html", context)
    else:
        raise Http404

def menu_home(request):
    if request.is_ajax():
        context = {}
        context['cols'] = range(10)
        context['rows'] = range(5)
        context['sqrs'] = map(lambda x: {"sqr": x, "mess": ""}, range(8))
        context['sqrs'][0]["mess"]="GitHub"
        context['sqrs'][1]["mess"]="Click For A Brief Story About This Site"
        context['sqrs'][2]["mess"]="My LinkedIn"
        context['sqrs'][6]["mess"]="About Me"
        context['sqrs'][7]["mess"]="MrSusanovo"
        context['sqrs'][7]["mess1"]="Created for Dumping Junk Code."
        context['sqrs'][7]["mess2"]="(Current Page: Tribute to Mondrian.)"
        return render(request, "mondrian.html", context)
    else:
        raise Http404

# Create your views here.
