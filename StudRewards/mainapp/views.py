from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse


def index(request):
    header = "Заголовок"  # обычная переменная
    message = ["python", "django"]  # список

    data = {"header": header, "message": message}
    return TemplateResponse(request, "index.html", data)


def about(request):
    return HttpResponse("О сайте")


def contact(request):
    return HttpResponse("Контакты")
