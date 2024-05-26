# Generated by Django 5.0.2 on 2024-03-20 10:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myA', '0003_alter_student_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.OneToOneField(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='myA.studentid'),
        ),
        migrations.AlterField(
            model_name='studentid',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]