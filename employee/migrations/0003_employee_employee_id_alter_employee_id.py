# Generated by Django 4.2.6 on 2024-03-20 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employee', '0002_monthlyregister_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='employee_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='employee_detail', to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]