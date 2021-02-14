import logging
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from app.models import Student, Major

_logger = logging.getLogger(__name__)
_logger.setLevel(level=logging.DEBUG)

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
    response = {}
    status = 200

    if request.POST:
        try:
            Major(
                name=request.POST.get('name'),
                code=request.POST.get('code'),
                desc=request.POST.get('description')
            ).save()
            status = 201
            response = {
                'log': 'Successfully saved new Major',
                'message': 'Berhasil menambah data'
            }
            _logger.info(response.get('log'))
        except Exception as err:
            _logger.error(str(err))
            status = 500
            response = {
                'log': str(err),
                'message': 'Terjadi kesalahan saat menambah data!'
            }

    return JsonResponse(response, safe=False, status=status)