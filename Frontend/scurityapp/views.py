from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def check_name():
    name_result = "Show the checking result of app name"
    return name_result

def app_style():
    app_style_result = "Show the checking result of app style"
    return app_style_result

def check_app_code():
    app_code_result = "Show the checking result of app code"
    return app_code_result

# 视图函数
def my_view(request):
    name_result = check_name()
    app_style_result = app_style()
    app_code_result = check_app_code()
    context = {
        'name_result': name_result,
        'app_style_result': app_style_result,
        'app_code_result': app_code_result
    }
    return render(request, 'scurityapp/front.html', context)