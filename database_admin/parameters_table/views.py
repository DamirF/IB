from django.shortcuts import render
from .modelGenerator import get_data, get_columns

# Create your views here.


def get_params_table(request):
    columns = get_columns()
    table = get_data()
    return render(request, "params_table.html", {"table": table, "columns": columns})
