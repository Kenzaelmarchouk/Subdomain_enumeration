# Generated by Django 4.1.2 on 2022-11-21 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StartScan', '0016_alter_tool_tool_desciption'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foundfrom',
            name='subdomain',
        ),
        migrations.RemoveField(
            model_name='foundfrom',
            name='tool',
        ),
        migrations.RemoveField(
            model_name='subdomain',
            name='domain',
        ),
        migrations.DeleteModel(
            name='DomainInfo',
        ),
        migrations.DeleteModel(
            name='FoundFrom',
        ),
        migrations.DeleteModel(
            name='SubDomain',
        ),
        migrations.DeleteModel(
            name='Tool',
        ),
    ]
