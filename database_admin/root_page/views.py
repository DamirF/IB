from django.shortcuts import render

# Create your views here.


def get_root_page(request):
    return render(request, "index_root.html", {})
