# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app.views import major, pages

urlpatterns = [

    # The home page
    path('', pages.index, name='home'),
    path('jurusan', major._page, name='major'),
    path('jurusan/form/<int:pk>', major._form, name='major_form'),

    # Matches any html file
    re_path(r'^.*\.*', pages.pages, name='pages'),

]
