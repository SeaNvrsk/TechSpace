import logging
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

logger = logging.getLogger('customLogger')


@login_required(login_url="/login/")
def indexView(request):
    logger.info("Rendering of index page")
    context = {'segment': 'index'}

    return render(request, 'core/index.html', context)


@login_required(login_url="/login/")
def tablesView(request):
    logger.info("Rendering of tables page")
    context = {'segment': 'tables'}

    return render(request, 'core/tables.html', context)


@login_required(login_url="/login/")
def profileView(request):
    logger.info("Rendering of profile page")
    context = {'segment': 'profile'}

    return render(request, 'core/profile.html', context)


@login_required(login_url="/login/")
def billingView(request):
    logger.info("Rendering of billing page")
    context = {'segment': 'billing'}

    return render(request, 'core/billing.html', context)
