from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotModified, HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseGone, HttpResponseServerError, HttpResponseNotFound
import json
from django.http import JsonResponse
from django.views.generic import ListView
from .models import Message


"""
This is Example 1. I have made this by using HttpTesponse method.
"""


def hello_world(request):
    return HttpResponse('Hello World. Django is very funny.')


"""
This is Example 2. The improve version of hello world. I have made this by using Template Render method. Here the system used Django MVT Model. Which is stands for Model, View & Template.
"""


def hello_world_improve(request):
    hello_world = "Hello World. This is the improve version of hello world"
    return render(request, "index.html", {'hello_world': hello_world})


"""
This function is made for cloud message front end template.
"""


def cloud_message(request):
    if request.method == "GET":
        receiver = request.GET.get('receiver', 0)
        msg = Message.objects.filter(userB=receiver).order_by("-id")
    return render(request, "MsgSingleWeb.html", {'msg': msg})


"""
This function is made for cloud message submission form.
"""


def cloud_message_submission(request):
    if request.method == "POST":
        userA = request.POST['userA']
        userB = request.POST['userB']
        msg = request.POST['msg']

        msg_database = Message(userA=userA, userB=userB, msg=msg)
        msg_database.save()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# 10 different types of response in django

def different_response_type (request):
    return render (request, "dif.html")

def httpresponse(request):
    return HttpResponse("This is HttpResponse in Django")



def httpResponsePermanentRedirect_view(request):
    return HttpResponse("This is httpresponseredirect_view in Django")


def httpresponseredirect(request):
    pass
    # It has been used in cloud_message_submission function


def httpResponsePermanentRedirect(request):
    return HttpResponsePermanentRedirect()


def httpResponseNotModified(request):
    return HttpResponseNotModified()


def httpResponseBadRequest(request):
    return HttpResponseBadRequest("Http Response Bad Request In Django")


def httpResponseForbidden(request):
    return HttpResponseForbidden("httpResponseForbidden in Django")


def httpResponseNotAllowed(request):
    return HttpResponseNotAllowed(('POST',"Message"))


def httpResponseGone(request):
    return HttpResponseGone("")


def httpResponseServerError(request):
    return HttpResponseServerError("httpResponseServerError in Django")


def httpResponseNotFound(request):
    return HttpResponseNotFound("httpResponseNotFound in Django")



def json_response_class (request):
    response_data = {}
    response_data['result'] = 'This is Json'
    response_data['message'] = 'Response In DJango'
    return HttpResponse(json.dumps(response_data), content_type="application/json")

def json_response_updated (request):
    return JsonResponse({'foo':'bar'})