from django.shortcuts import render
from core.forms import StartUpInternshipModelForm
from core.models import StartUpInternships
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from core.exceptions import FileSizeExceedException

def startup_form(request):

    if request.method == "POST":
        all_post_files = request.FILES
        if all_post_files['description_file'].size > settings.MAX_STARTUP_FILE_UPLOAD:
            try:
                raise FileSizeExceedException
            except:
                pass        #will render back form with custom original params
        else:
            form_submit = StartUpInternshipModelForm(request.POST, all_post_files)
            if form_submit.is_valid():
                form_submit.save(commit=True)
                return HttpResponseRedirect(reverse("startupform"))

    form = StartUpInternshipModelForm()

    return render(request, 'core/startup_form.html', {'form' : form})

def student_intership_view(request):
    
    all_internships = StartUpInternships.objects.all()

    return render(request, 'core/startup_internship_view.html', {'all_internships' : all_internships})
