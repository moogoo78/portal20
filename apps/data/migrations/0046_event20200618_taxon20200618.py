# Generated by Django 3.0.5 on 2020-06-18 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0045_merge_20200528_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event20200618',
            fields=[
                ('index', models.BigIntegerField(blank=True, null=True)),
                ('id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('eventid', models.TextField(blank=True, db_column='eventID', null=True)),
                ('parenteventid', models.TextField(blank=True, db_column='parentEventID', null=True)),
                ('samplingprotocol', models.TextField(blank=True, db_column='samplingProtocol', null=True)),
                ('samplesizevalue', models.FloatField(blank=True, db_column='sampleSizeValue', null=True)),
                ('samplesizeunit', models.TextField(blank=True, db_column='sampleSizeUnit', null=True)),
                ('samplingeffort', models.TextField(blank=True, db_column='samplingEffort', null=True)),
                ('eventdate', models.TextField(blank=True, db_column='eventDate', null=True)),
                ('eventtime', models.TextField(blank=True, db_column='eventTime', null=True)),
                ('locationid', models.TextField(blank=True, db_column='locationID', null=True)),
                ('decimallatitude', models.TextField(blank=True, db_column='decimalLatitude', null=True)),
                ('decimallongitude', models.TextField(blank=True, db_column='decimalLongitude', null=True)),
                ('geodeticdatum', models.TextField(blank=True, db_column='geodeticDatum', null=True)),
                ('coordinateuncertaintyinmeters', models.FloatField(blank=True, db_column='coordinateUncertaintyInMeters', null=True)),
                ('coordinateprecision', models.FloatField(blank=True, db_column='coordinatePrecision', null=True)),
                ('verbatimelevation', models.FloatField(blank=True, db_column='verbatimElevation', null=True)),
                ('verbatimlatitude', models.FloatField(blank=True, db_column='verbatimLatitude', null=True)),
                ('verbatimlongitude', models.FloatField(blank=True, db_column='verbatimLongitude', null=True)),
                ('verbatimcoordinatesystem', models.TextField(blank=True, db_column='verbatimCoordinateSystem', null=True)),
                ('year', models.FloatField(blank=True, null=True)),
                ('month', models.FloatField(blank=True, null=True)),
                ('day', models.FloatField(blank=True, null=True)),
                ('habitat', models.TextField(blank=True, null=True)),
                ('eventremarks', models.TextField(blank=True, db_column='eventRemarks', null=True)),
                ('countrycode', models.TextField(blank=True, db_column='countryCode', null=True)),
                ('county', models.TextField(blank=True, null=True)),
                ('locality', models.TextField(blank=True, null=True)),
                ('q_year', models.FloatField(blank=True, null=True)),
                ('q_month', models.FloatField(blank=True, null=True)),
                ('q_day', models.FloatField(blank=True, null=True)),
                ('municipality', models.TextField(blank=True, null=True)),
                ('geologicalcontextid', models.TextField(blank=True, db_column='geologicalContextID', null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('stateprovince', models.TextField(blank=True, db_column='stateProvince', null=True)),
                ('type', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'event_20200618',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Taxon20200618',
            fields=[
                ('index', models.BigIntegerField(blank=True, null=True)),
                ('id', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('taxonid', models.TextField(blank=True, db_column='taxonID', null=True)),
                ('scientificnameid', models.TextField(blank=True, db_column='scientificNameID', null=True)),
                ('kingdom', models.TextField(blank=True, null=True)),
                ('phylum', models.TextField(blank=True, null=True)),
                ('class_field', models.TextField(blank=True, db_column='class', null=True)),
                ('order', models.TextField(blank=True, null=True)),
                ('family', models.TextField(blank=True, null=True)),
                ('genus', models.TextField(blank=True, null=True)),
                ('specificepithet', models.TextField(blank=True, db_column='specificEpithet', null=True)),
                ('infraspecificepithet', models.TextField(blank=True, db_column='infraspecificEpithet', null=True)),
                ('scientificnameauthorship', models.TextField(blank=True, db_column='scientificNameAuthorship', null=True)),
                ('vernacularname', models.TextField(blank=True, db_column='vernacularName', null=True)),
                ('taxonremarks', models.TextField(blank=True, db_column='taxonRemarks', null=True)),
                ('scientificname', models.TextField(blank=True, db_column='scientificName', null=True)),
                ('taxonrank', models.TextField(blank=True, db_column='taxonRank', null=True)),
                ('taxonomicstatus', models.TextField(blank=True, db_column='taxonomicStatus', null=True)),
                ('acceptednameusageid', models.TextField(blank=True, db_column='acceptedNameUsageID', null=True)),
                ('subgenus', models.FloatField(blank=True, null=True)),
                ('nameaccordingto', models.TextField(blank=True, db_column='nameAccordingTo', null=True)),
                ('nomenclaturalstatus', models.TextField(blank=True, db_column='nomenclaturalStatus', null=True)),
            ],
            options={
                'db_table': 'taxon_20200618',
                'managed': False,
            },
        ),
    ]
