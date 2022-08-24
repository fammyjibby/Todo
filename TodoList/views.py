from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todo = Todo.objects.all()
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"index.html",{'todos':todo,'forms':form})

def delete(request,pk):
    mytask = Todo.objects.get(id=pk)
    mytask.delete()
    return redirect('index')

def update(request,pk):
    mytodo = Todo.objects.get(id=pk)
    updatetodo = TodoForm(instance=mytodo) #enable us to be able to edit the tasks
    if request.method == 'POST':
        updatetodo = TodoForm(request.POST,instance=mytodo) #enables us to create or edit a new task without leaving the old task in the database
        if updatetodo.is_valid():
            updatetodo.save()
            return redirect('index')
    return render(request, 'update.html', {'mytodos':mytodo,'updatetodos':updatetodo})


