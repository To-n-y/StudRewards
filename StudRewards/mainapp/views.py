from django.http import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render

from .forms import LoginForm, ReportForm
from .models import Teacher


def index(request):
    return HttpResponsePermanentRedirect("/login")


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        teachers = Teacher.objects.all()
        teacher = teachers.filter(email=email).first()
        if teacher is None:
            return HttpResponse(
                f"<h2>Привет, незнакомец! <a href="">На главную</a> </h2>")
        return HttpResponse(f"<h2>Привет, {teacher.firstName}, твой пароль: {password} <a href="">На главную</a> </h2>")

    else:
        loginForm = LoginForm(initial={'password': 'pass'})
        return render(request, "login.html", {"loginForm": loginForm})


def teacherProfile(request):
    if request.method == "POST":
        description = request.POST.get("description")
        activity = request.POST.get("activity")
        students = request.POST.getlist("students")
        teachers = Teacher.objects.all()
        teacher = teachers.filter(email="mail@mail.ru").first()
        if teacher is None:
            return HttpResponse(
                f"<h2>Привет, незнакомец! <a href="">На главную</a> </h2>")
        print("STUDENTS ", students)
        return HttpResponse(f"<h2>Привет, , твой пароль:  <a href="">На главную</a> </h2>")

    else:
        reportForm = ReportForm()
        return render(request, "teacherProfile.html", {"reportForm": reportForm})
