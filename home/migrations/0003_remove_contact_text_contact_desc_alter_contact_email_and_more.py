# Generated by Django 4.0.4 on 2022-05-05 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_contact_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='text',
        ),
        migrations.AddField(
            model_name='contact',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
