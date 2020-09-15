from django.shortcuts import render
from core.forms import StartUpInternshipModelForm
from core.models import StartUpInternships

def startup_form(request):

    if request.method == "POST":
        form_submit = StartUpInternshipModelForm(request.POST, request.FILES)
        if form_submit.is_valid():
            form_submit.save(commit=True)

    form = StartUpInternshipModelForm()

    return render(request, 'core/startup_form.html', {'form' : form})

def student_intership_view(request):
    
    all_internships = StartUpInternships.objects.all()

    return render(request, 'core/startup_internship_view.html', {'all_internships' : all_internships})
