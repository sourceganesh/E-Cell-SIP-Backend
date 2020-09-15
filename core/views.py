from django.shortcuts import render

def startup_form(request):
    from django.urls import reverse
    from django.conf import settings
    from core.exceptions import FileSizeExceedException
    from core.forms import StartUpInternshipModelForm
    from django.http import HttpResponseRedirect

    if request.method == "POST":
        all_post_files = request.FILES
        if all_post_files['description_file'].size > settings.MAX_STARTUP_FILE_UPLOAD:
            try:
                raise FileSizeExceedException
            except:
                pass        # code to render back form with custom original params to be done
        else:
            form_submit = StartUpInternshipModelForm(request.POST, all_post_files)
            if form_submit.is_valid():
                form_submit.save(commit=True)
                return HttpResponseRedirect(reverse("startupform"))

    form = StartUpInternshipModelForm()

    return render(request, 'core/startup_form.html', {'form' : form})

def student_intership_view(request):
    from core.models import StartUpInternships
    from core.helper import parse_date

    post_date = None
    last_date = None
    if request.method == "GET":
        post_date = request.GET.get('post-date')
        last_date = request.GET.get('last-date')

    all_internships = StartUpInternships.objects.all()

    if post_date:
        post_date_dt = parse_date(post_date)
        all_internships = all_internships.filter(created_at__date__gte=post_date_dt)
    
    if last_date:
        last_date_dt = parse_date(last_date)
        all_internships = all_internships.filter(last_date_to_apply__lte=last_date_dt)
    

    return render(request, 'core/startup_internship_view.html', {'all_internships' : all_internships})
