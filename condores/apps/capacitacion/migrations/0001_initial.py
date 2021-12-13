# Generated by Django 3.2.5 on 2021-12-08 16:37

from django.db import migrations, models
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='capacitacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deletec_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('numeroEmpleado', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Modelo capacitacion',
                'verbose_name_plural': 'Modelo capacitacion',
            },
        ),
        migrations.CreateModel(
            name='cursos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deletec_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('nombreCurso', models.CharField(max_length=255)),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
            ],
            options={
                'verbose_name': 'Modelo Cursos',
                'verbose_name_plural': 'Modelo Cursos',
            },
        ),
        migrations.CreateModel(
            name='Historicalcapacitacion',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('deletec_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminacion')),
                ('numeroEmpleado', models.CharField(max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Modelo capacitacion',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Historicalcursos',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('deletec_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminacion')),
                ('nombreCurso', models.CharField(max_length=255)),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Modelo Cursos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Historicalinstructor',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('deletec_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminacion')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido1', models.CharField(max_length=255)),
                ('apellido2', models.CharField(max_length=255)),
                ('especialidad', models.CharField(max_length=255)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Modelo Instructor',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='instructor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('deletec_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido1', models.CharField(max_length=255)),
                ('apellido2', models.CharField(max_length=255)),
                ('especialidad', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Modelo Instructor',
                'verbose_name_plural': 'Modelo Instructor',
            },
        ),
    ]
