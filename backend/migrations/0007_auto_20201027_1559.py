# Generated by Django 3.1.2 on 2020-10-27 10:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20201027_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bottomlevel',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='bottomlevel',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='middlelevel',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='middlelevel',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='toplevel',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='toplevel',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='parameter',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parameter',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.farm')),
            ],
            options={
                'db_table': 'Node',
            },
        ),
        migrations.AddField(
            model_name='parameter',
            name='node',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.node'),
            preserve_default=False,
        ),
    ]
