from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render

from .forms import LoginForm, ReportForm
from .models import Teacher, Student, Report


def index(request):
    return HttpResponsePermanentRedirect("/login")


def login(request):
    if request.method == "POST":
        if request.POST.get("val") == '1':
            # login
            print(request.POST.get("role"))
            if request.POST.get("role") == '2':
                # teacher
                email = request.POST.get("email")
                password = request.POST.get("password")
                teachers = Teacher.objects.all()
                teacher = teachers.filter(email=email).first()
                if teacher is None:
                    return HttpResponse(
                        f"<h2>Привет, незнакомец! <a href="">На главную</a> </h2>")

                print(teacher.password, password)
                if teacher.password == password:
                    request.session['teacher_email'] = teacher.email
                    return HttpResponsePermanentRedirect("/teacher")
                else:
                    return HttpResponseRedirect("/login")

            elif request.POST.get("role") == '1':
                # student
                email = request.POST.get("email")
                password = request.POST.get("password")
                students = Student.objects.all()
                student = students.filter(email=email).first()
                if student is None:
                    return HttpResponse(
                        f"<h2>Привет, незнакомец! <a href="">На главную</a> </h2>")

                print(student.password, password)
                if student.password == password:
                    request.session['student_email'] = student.email
                    return HttpResponsePermanentRedirect("/student")
                else:
                    return HttpResponseRedirect("/login")
        else:
            # register
            return HttpResponseRedirect("/login")
    else:
        loginForm = LoginForm(initial={'password': 'pass'})
        return render(request, "login.html", {"loginForm": loginForm})


def logout(request):
    # del request.session['student_email']
    del request.session['teacher_email']
    return HttpResponsePermanentRedirect("/login")


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
        return HttpResponseRedirect("/teacher")

    else:
        teacherEmail = request.session.get('teacher_email')
        teachers = Teacher.objects.all()
        teacher = teachers.filter(email=teacherEmail).first()
        reports = Report.objects.all().filter(teacher_id=teacher.id)
        reportForm = ReportForm()
        return render(request, "teacherProfile.html",
                      {"reportForm": reportForm, "teacher": teacher, "reports": reports})
