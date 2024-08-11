from django.shortcuts import render
from .models import Thread
from .forms import ThreadForm, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def index(req):
    return render(req, 'index.html')

def thread_list(req):
    threads = Thread.objects.all().order_by('-created_at')
    return render(req, 'thread_list.html', {'threads': threads})
@login_required
def thread_create(req):
    if req.method == 'POST':
        form = ThreadForm(req.POST, req.FILES)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.user = req.user
            thread.save()
            return redirect('thread_list')
        else:
            return render(req, 'thread_form.html', {'form': form})
        
    else:
        form = ThreadForm()
        return render(req, 'thread_form.html', {'form': form})
@login_required    
def thread_edit(req, thread_id): 
    thread = get_object_or_404(Thread, pk=thread_id, user = req.user)
    if req.method == 'POST':
        form = ThreadForm(req.POST, req.FILES, instance = thread)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.save()
            return redirect('thread_list')
    else:
        form = ThreadForm(instance = thread)
        return render(req, 'thread_form.html', {'form': form})
@login_required
def thread_delete(req, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id, user = req.user)
    if req.method == 'POST':
        thread.delete()
        return redirect('thread_list')
    return render(req, 'thread_confirm_delete.html', {'thread': thread})

def register(req):
    form = UserRegistrationForm()
    if req.method == 'POST':
        form = UserRegistrationForm(req.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(req, 'registration/register.html', {'form': form})