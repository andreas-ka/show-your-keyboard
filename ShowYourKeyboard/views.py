""" Error handling system Module """
from django.shortcuts import render


def page_not_found_view(request, exception):
    """ 404 error view """
    data = {}
    return render(request, 'templates/404.html', data)


def custom_500_error_view(request, exception):
    """ 500 error view """
    data = {}
    return render(request, 'templates/500.html', data)


def custom_403_error_view(request, exception):
    """ 403 error view """
    data = {}
    return render(request, 'templates/403.html', data)