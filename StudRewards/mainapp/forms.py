from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(label="email:")
    password = forms.CharField(label="password:")
    rolesChoice = [
        (1, "student"),
        (2, "teacher"),
        (3, "admin"),
    ]
    role = forms.ChoiceField(label="role", choices=rolesChoice)


class ReportForm(forms.Form):
    description = forms.CharField()
    studentsChoice = [
        (1, "first"),
        (2, "second"),
    ]
    activity = forms.ChoiceField(label="activities", choices=studentsChoice)
    students = forms.MultipleChoiceField(label="students", choices=studentsChoice)

