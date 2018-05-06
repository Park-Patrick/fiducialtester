from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from .models import Document
from .forms import DocumentForm

def index(request):
    return HttpResponse("Hello, world. I don't know what I'm doing..")

# def simple_upload(request):
#	if request.method == 'POST' and request.FILES['myfile']:
#		myfile = request.FILES['myfile']
#		fs = FileSystemStorage()
#		filename = fs.save(myfile.name, myfile)
#		uploaded_file_url = fs.url(filename)
#		return render(request, 'simple_upload.html', {
#			'uploaded_file_url': uploaded_file_url
#		})
#	return render(request, 'simple_upload.html')


def upload_file(request):
	if request.method == 'POST':
		print("Hello")
		print(request.__dict__)
		form = DocumentForm(request.POST, request.FILES)
		print(form.is_valid())
		if form.is_valid():
			# file is saved
			form.save()
			return HttpResponseRedirect('/calc/')
	else:
		form = DocumentForm()
	return render(request, 'simple_upload.html', {'form': form})

