from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Task


def all_tasks(request):
    tasks = Task.objects.filter(active=True)
    data = serializers.serialize('json', tasks)
    return HttpResponse(data, content_type='application/json')


def new_task(request):
    title = request.GET.get('title')
    if title:
        task = Task(title=title)
        task.save()
        data = serializers.serialize('json', [task])
        return HttpResponse(data, content_type='application/json')
    else:
        return HttpResponse(status=404)


def update_task(request, id):
    task = Task.objects.filter(id=id, active=True)
    if task:
        title = request.GET.get('title')
        if title:
            task.update(title=title)
        data = serializers.serialize('json', task)
        return HttpResponse(data, content_type='application/json')
    else: return HttpResponse(status=404)


def delete_task(request, id):
    task = Task.objects.filter(id=id, active=True)
    if task:
        task.update(active=False)
        data = serializers.serialize('json', task)
        return HttpResponse(data, content_type='application/json')
    else: return HttpResponse(status=404)
