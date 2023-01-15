from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def checks(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, "index.html")
