from django.urls import path
from .views import (
    hello_world,
    hello_world_improve,
    cloud_message,
    cloud_message_submission,
    httpresponse,
    httpresponseredirect,
    httpResponsePermanentRedirect,
    httpResponseNotModified,
    httpResponseBadRequest,
    httpResponseForbidden,
    httpResponseNotAllowed,
    httpResponseGone,
    httpResponseServerError,
    httpResponseNotFound,
    json_response_class,
    different_response_type,
    httpResponsePermanentRedirect,
)

urlpatterns = [

    path('', hello_world_improve, name='hello_world_improve'),
    path('hello_world/', hello_world, name='hello_world'),
    path('cloud_message/', cloud_message, name='cloud_message'),
    path('cloud_message_submission/', cloud_message_submission, name='cloud_message_submission'),
    path('different_response_type/', different_response_type, name='different_response_type'),
    path('httpresponse/', httpresponse, name='httpresponse'),
    path('httpresponseredirect/', httpresponseredirect, name='httpresponseredirect'),
    path('httpResponsePermanentRedirect/', httpResponsePermanentRedirect, name='httpResponsePermanentRedirect'),
    path('httpResponseNotModified/', httpResponseNotModified, name='httpResponseNotModified'),
    path('httpResponseBadRequest/', httpResponseBadRequest, name='httpResponseBadRequest'),
    path('httpResponseForbidden/', httpResponseForbidden, name='httpResponseForbidden'),
    path('httpResponseNotAllowed/', httpResponseNotAllowed, name='httpResponseNotAllowed'),
    path('httpResponseGone/', httpResponseGone, name='httpResponseGone'),
    path('httpResponseServerError/', httpResponseServerError, name='httpResponseServerError'),
    path('httpResponseNotFound/', httpResponseNotFound, name='httpResponseNotFound'),
    path('json_response_class/', json_response_class, name='json_response_class'),
    path('httpResponsePermanentRedirect/', httpResponsePermanentRedirect, name='httpResponsePermanentRedirect'),
]