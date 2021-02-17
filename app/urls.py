# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app.views import major, pages

urlpatterns = [

    # The home page
    path('', pages.index, name='home'),
    path('jurusan', major._page, name='major_page'),
    path('jurusan/<int:pk>', major._get_one, name='major_one'),
    path('jurusan/form/', major._form, name='major_form'),
    path('jurusan/form/<int:pk>', major._form, name='major_form'),
    path('jurusan/remove/<int:pk>', major._remove, name='major_remove'),

    # Matches any html file
    re_path(r'^.*\.*', pages.pages, name='pages'),

]
