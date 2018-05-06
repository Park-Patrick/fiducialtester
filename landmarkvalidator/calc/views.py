from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from .csv_test import import_csv
import os

from .models import Document
from .forms import DocumentForm

def index(request):
    return HttpResponse("Hello, world. I don't know what I'm doing..")

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            doc=form.save()
            # file is processed
            truemarks = os.getcwd() + '/calc/meanlandmarks/'+doc.template+'_mean.fcsv'
            true, xyz, error = import_csv(doc.document.file.name, truemarks)
            print(xyz)
            return HttpResponseRedirect('/calc/')
    else:
        form = DocumentForm()
    return render(request, 'simple_upload.html', {'form': form})