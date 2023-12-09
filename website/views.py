from django.shortcuts import render, redirect
from .forms import CustomerRequestForm
from .models import CustomerRequestsDatabase


def index(request):
    return render(request, 'website/index.html')


def submit_request(request):
    if request.method == 'POST':
        form = CustomerRequestForm(request.POST)
        if form.is_valid():
            inst = CustomerRequestsDatabase(
                name=form.cleaned_data['name'],
                tel=form.cleaned_data['tel'],
                email=form.cleaned_data['email'],
                comment=form.cleaned_data['comment']
            )
            inst.save()
            return redirect('success_page')
    else:
        form = CustomerRequestForm()

    return render(request, 'website/index.html', {'form': form})


def submit_success(request):
    return render(request, 'website/success_page.html')