# Generated by Django 3.2.5 on 2021-12-27 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mision', '0003_catinstitucion_descripcion_emergencia_historicaldescripcion_emergencia_historicalinstructores_histor'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalsolicitud_emergencia',
            name='descripcionEmergencia',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='mision.descripcion_emergencia'),
        ),
        migrations.AddField(
            model_name='historicalsolicitud_emergencia',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='solicitud_emergencia',
            name='descripcionEmergencia',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mision.descripcion_emergencia'),
        ),
        migrations.AddField(
            model_name='solicitud_emergencia',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
