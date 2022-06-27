from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def indexView(request):
    context = {'segment': 'index'}

    return render(request, 'core/index.html', context)


@login_required(login_url="/login/")
def tablesView(request):
    context = {'segment': 'tables'}

    return render(request, 'core/tables.html', context)


@login_required(login_url="/login/")
def profileView(request):
    context = {'segment': 'profile'}

    return render(request, 'core/profile.html', context)


@login_required(login_url="/login/")
def billingView(request):
    context = {'segment': 'billing'}

    return render(request, 'core/billing.html', context)
