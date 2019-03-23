# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse(" <html> <head> <title>Initial Display</title> </head> <body> <div>This is an initial display</div> <div>Here, data collected and indexed by ScentGather will be displayed</div> </body> </html>")
