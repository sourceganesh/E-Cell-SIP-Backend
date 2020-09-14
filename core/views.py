from django.shortcuts import render
from core.forms import StartUpInternshipModelForm

def startup_form(request):

    if request.method == "POST":
        form_submit = StartUpInternshipModelForm(request.POST, request.FILES)
        if form_submit.is_valid():
            form_submit.save(commit=True)

    form = StartUpInternshipModelForm()

    return render(request, 'core/startup_form.html', {'form' : form})

def student_intership_view(request):
    
    pass
