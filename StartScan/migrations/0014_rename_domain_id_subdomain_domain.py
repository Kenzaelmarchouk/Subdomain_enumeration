# Generated by Django 4.1.2 on 2022-10-06 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StartScan', '0013_foundfrom_tool_rename_domain_id_domaininfo_domain_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subdomain',
            old_name='domain_id',
            new_name='domain',
        ),
    ]
