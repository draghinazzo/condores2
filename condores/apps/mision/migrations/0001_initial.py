# Generated by Django 3.2.5 on 2021-12-21 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='catCargo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deletec_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Modelo Cargo',
                'verbose_name_plural': 'Modelo Cargo',
            },
        ),
        migrations.CreateModel(
            name='catMedio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deletec_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Modelo Medio',
                'verbose_name_plural': 'Modelo Medio',
            },
        ),
        migrations.CreateModel(
            name='catServicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deletec_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Modelo Servicio',
                'verbose_name_plural': 'Modelo Servicio',
            },
        ),
        migrations.CreateModel(
            name='catSexo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deletec_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('sexo', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Modelo catalogo sexo',
                'verbose_name_plural': 'Modelo catalogo sexo',
            },
        ),
        migrations.CreateModel(
            name='catSolicitante',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deletec_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Modelo CatSolicitante',
                'verbose_name_plural': 'Modelo CatSolicitante',
            },
        ),
        migrations.CreateModel(
            name='catTipoE',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deletec_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('nombre', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Modelo tipo empleado',
                'verbose_name_plural': 'Modelo tipo empleado',
            },
        ),
        migrations.CreateModel(
            name='HistoricalcatTipoE',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('deletec_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminacion')),
                ('nombre', models.CharField(max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Modelo tipo empleado',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalcatSolicitante',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('deletec_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminacion')),
                ('nombre', models.CharField(max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Modelo CatSolicitante',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalcatSexo',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('deletec_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminacion')),
                ('sexo', models.CharField(max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Modelo catalogo sexo',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalcatServicio',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('deletec_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminacion')),
                ('nombre', models.CharField(max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Modelo Servicio',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalcatMedio',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('deletec_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminacion')),
                ('nombre', models.CharField(max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Modelo Medio',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalcatCargo',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('deletec_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminacion')),
                ('nombre', models.CharField(max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Modelo Cargo',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
