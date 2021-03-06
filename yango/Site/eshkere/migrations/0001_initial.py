# Generated by Django 2.2 on 2019-04-14 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('code_of_city', models.AutoField(primary_key=True, serialize=False, verbose_name='КОД ГОРОДА')),
                ('name_of_city', models.CharField(max_length=255, verbose_name='НАЗВАНИЕ ГОРОДА')),
            ],
            options={
                'verbose_name': 'Список городов',
                'verbose_name_plural': 'Список городов',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('code_of_position', models.AutoField(primary_key=True, serialize=False, verbose_name='КОД ДОЛЖНОСТИ')),
                ('name_of_position', models.CharField(max_length=255, verbose_name='НАЗВАНИЕ ДОЛЖНОСТИ')),
            ],
            options={
                'verbose_name': 'Список должностей',
                'verbose_name_plural': 'Список должностей',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('code_of_route', models.AutoField(primary_key=True, serialize=False, verbose_name='КОД МАРШРУТА')),
                ('d_departure', models.CharField(max_length=255, verbose_name='ДВ ОТПРАВЛЕНИЯ')),
                ('d_arrival', models.CharField(max_length=255, verbose_name='ДВ ПРИБЫТИЯ')),
            ],
            options={
                'verbose_name': 'Список маршрутов',
                'verbose_name_plural': 'Список маршрутов',
            },
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('number_of_train', models.AutoField(primary_key=True, serialize=False, verbose_name='НОМЕР ПОЕЗДА')),
                ('type_of_train', models.CharField(max_length=255, verbose_name='ТИП ПОЕЗДА')),
            ],
            options={
                'verbose_name': 'Список поездов',
                'verbose_name_plural': 'Список поездов',
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('code_of_station', models.AutoField(primary_key=True, serialize=False, verbose_name='КОД СТАНЦИИ')),
                ('name_of_station', models.CharField(max_length=255, verbose_name='НАЗВАНИЕ СТАНЦИИ')),
                ('code_of_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshkere.City', verbose_name='КОД ГОРОДА')),
            ],
            options={
                'verbose_name': 'Список станций',
                'verbose_name_plural': 'Список станций',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('code_of_staff', models.AutoField(primary_key=True, serialize=False, verbose_name='КОД СОТРУДНИКА')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО СОТРУДНИКА')),
                ('birthdate_of_staff', models.DateField(auto_now=True, verbose_name='ДАТА РОЖДЕНИЯ СОТРУДНИКА')),
                ('code_of_passport', models.CharField(max_length=255, verbose_name='ПАСПОРТНЫЕ ДАННЫЕ')),
                ('special_sign', models.CharField(max_length=255, verbose_name='ОСОБЫЕ ПРИМЕТЫ')),
                ('m_e_data', models.CharField(max_length=255, verbose_name='ДАННЫЕ МЕДОСМОТРА')),
                ('code_of_position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshkere.Position', verbose_name='КОД ДОЛЖНОСТИ')),
            ],
            options={
                'verbose_name': 'Список сотрудников',
                'verbose_name_plural': 'Список сотрудников',
            },
        ),
        migrations.CreateModel(
            name='S_Station',
            fields=[
                ('code_of_s_station', models.AutoField(primary_key=True, serialize=False, verbose_name='КОД ДОПОЛНИТЕЛЬНОЙ СТАНЦИИ')),
                ('time_of_arrive', models.DateField(auto_now=True, verbose_name='ВРЕМЯ ПРИБЫТИЯ')),
                ('time_of_stop', models.DateField(auto_now=True, verbose_name='ВРЕМЯ СТОЯНКИ')),
                ('code_of_route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshkere.Route', verbose_name='КОД МАРШРУТА')),
                ('code_of_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshkere.Station', verbose_name='КОД СТАНЦИИ')),
            ],
            options={
                'verbose_name': 'Список дополнительных станций',
                'verbose_name_plural': 'Список дополнительных станций',
            },
        ),
        migrations.AddField(
            model_name='route',
            name='number_of_train',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshkere.Train', verbose_name='НОМЕР ПОЕЗДА'),
        ),
        migrations.AddField(
            model_name='route',
            name='point_of_arrival',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_a', to='eshkere.Station', verbose_name='ПУНКТ ПРИБЫТИЯ'),
        ),
        migrations.AddField(
            model_name='route',
            name='point_of_departure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='p_d', to='eshkere.Station', verbose_name='ПУНКТ ОТПРАВЛЕНИЯ'),
        ),
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('code_of_crew', models.AutoField(primary_key=True, serialize=False, verbose_name='КОД ЭКИПАЖА')),
                ('number_of_rcar', models.CharField(max_length=255, verbose_name='НОМЕР ВАГОНА')),
                ('code_of_staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshkere.Staff', verbose_name='КОД СОТРУДНИКА')),
                ('number_of_train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshkere.Train', verbose_name='НОМЕР ПОЕЗДА')),
            ],
            options={
                'verbose_name': 'Список экипажа',
                'verbose_name_plural': 'Список экипажа',
            },
        ),
    ]
