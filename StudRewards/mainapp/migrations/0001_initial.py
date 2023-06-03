# Generated by Django 4.2.1 on 2023-06-03 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Activity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("description", models.CharField(max_length=50)),
                ("units", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("lastName", models.CharField(max_length=20)),
                ("firstName", models.CharField(max_length=20)),
                ("dateOfBirth", models.DateField()),
                ("email", models.CharField(max_length=30)),
                ("password", models.CharField(max_length=60)),
                ("course", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("lastName", models.CharField(max_length=20)),
                ("firstName", models.CharField(max_length=20)),
                ("dateOfBirth", models.DateField()),
                ("email", models.CharField(max_length=30)),
                ("password", models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name="Report",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.CharField(max_length=20)),
                ("date", models.DateField()),
                ("checked", models.IntegerField()),
                (
                    "activity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainapp.activity",
                    ),
                ),
                ("students", models.ManyToManyField(to="mainapp.student")),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mainapp.teacher",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="activity",
            name="students",
            field=models.ManyToManyField(to="mainapp.student"),
        ),
    ]
