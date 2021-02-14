from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from app.models import Student, Major

@login_required(login_url="/login")
def _page(request):
    context = {
        "title": "Halaman Jurusan",
        "breadcrumb": "Jurusan",
        "segment": "major",
        "data": Major.objects.annotate(total_students=Count('student'))
    }

    return render(request, "app/major/page.html", context)

@login_required(login_url="/login")
def _form(request, pk=None):
    context = {}

    # {"form": form, "msg" : msg, "success" : success }

    return render(request, "app/major/form.html", context)