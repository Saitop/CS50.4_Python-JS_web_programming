
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

class NewTaskForm(forms.Form):
    """docstring for NewTaskForm"""
    # def __init__(self, arg):
    #     super(NewTaskForm, self).__init__()
    #     self.arg = arg
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(reqeust):
    if reqeust.method == "POST":
        form = NewTaskForm(reqeust.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            reqeust.session['tasks'] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(reqeust, "tasks/add.html", {
                "form": form
                })
    return render(reqeust, "tasks/add.html", {
        "form": NewTaskForm()
    })