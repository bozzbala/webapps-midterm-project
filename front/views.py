from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Task
from .models import Task
from django.views.decorators.http import require_POST

# Create your views here.
def tasks(request):
    tasks_list = Task.objects.order_by('completed', '-id').values()
    template = loader.get_template('tasks.html')
    context = {
        'list': tasks_list,
    }
    return HttpResponse(template.render(context, request))

@require_POST
def create_task(request):
    new_task = Task(
        title=request.POST['title'],
        description=request.POST['description']
    )
    new_task.save()
    return redirect('tasks')

def task(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'task.html', {'task': task})

def task_edit(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.save()
        return redirect('tasks')
    return render(request, 'task_edit.html', {'task': task})

def task_delete(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('tasks')

@require_POST
def task_complete(request, id):
    task = get_object_or_404(Task, pk=id)
    task.completed = True
    task.save()
    return redirect('tasks')