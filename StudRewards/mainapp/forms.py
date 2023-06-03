from django import forms


class LoginForm(forms.Form):
    email = forms.CharField(label="email:")
    password = forms.CharField(label="password:")


class ReportForm(forms.Form):
    description = forms.CharField()
    choice = [
        (1, "first"),
        (2, "second"),
    ]
    activity = forms.ChoiceField(label="activities", choices=choice)
    students = forms.MultipleChoiceField(label="students", choices=choice)

