from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

@login_required(login_url="/login")
def _page(request):
    context = {}

    # {"form": form, "msg" : msg, "success" : success }

    return render(request, "app/major/page.html", context)

@login_required(login_url="/login")
def _form(request, pk=None):
    context = {}

    # {"form": form, "msg" : msg, "success" : success }

    return render(request, "app/major/form.html", context)