from django.db import models
from django.utils import timezone
from django.urls import reverse

class City(models.Model):
	code_of_city = models.AutoField(primary_key=True, verbose_name='КОД ГОРОДА')
	name_of_city = models.CharField(max_length=255, verbose_name='НАЗВАНИЕ ГОРОДА')

	def __str__(self):
		return "%s" % (self.name_of_city)
	class Meta:
		verbose_name = 'Список городов'
		verbose_name_plural = 'Список городов'
	def get_absolute_url(self):
		return reverse('view')

class Station(models.Model):
	code_of_station = models.AutoField(primary_key=True, verbose_name='КОД СТАНЦИИ')
	name_of_station = models.CharField(max_length=255, verbose_name='НАЗВАНИЕ СТАНЦИИ')
	code_of_city = models.ForeignKey(City, on_delete = models.CASCADE, verbose_name = 'КОД ГОРОДА')

	def __str__(self):
		return "%s" % (self.name_of_station)
	class Meta:
		verbose_name = 'Список станций'
		verbose_name_plural = 'Список станций'
	def get_absolute_url(self):
		return reverse('view')

class Train(models.Model):
	number_of_train = models.AutoField(primary_key=True, verbose_name='НОМЕР ПОЕЗДА')
	type_of_train = models.CharField(max_length=255, verbose_name='ТИП ПОЕЗДА')

	def __str__(self):
		return '%s' % (self.type_of_train)
	class Meta:
		verbose_name = 'Список поездов'
		verbose_name_plural = 'Список поездов'
	def get_absolute_url(self):
		return reverse('view')

class Route(models.Model):
	code_of_route = models.AutoField(primary_key=True, verbose_name = 'КОД МАРШРУТА')
	number_of_train = models.ForeignKey(Train, on_delete=models.CASCADE, verbose_name='НОМЕР ПОЕЗДА')
	d_departure = models.CharField(max_length=255, verbose_name='ДВ ОТПРАВЛЕНИЯ')
	d_arrival = models.CharField(max_length=255, verbose_name='ДВ ПРИБЫТИЯ')
	# Пункт отправления
	point_of_departure = models.ForeignKey(Station, related_name = 'p_d',on_delete=models.CASCADE, verbose_name='ПУНКТ ОТПРАВЛЕНИЯ')
	# Пункт прибытия
	point_of_arrival = models.ForeignKey(Station,related_name = 'p_a', on_delete=models.CASCADE, verbose_name='ПУНКТ ПРИБЫТИЯ')

	def __str__(self):
		return "%s %s" % (self.d_departure, self.d_arrival)
	class Meta:
		verbose_name = 'Список маршрутов'
		verbose_name_plural = 'Список маршрутов'
	def get_absolute_url(self):
		return reverse('view')

class Position(models.Model):
	code_of_position = models.AutoField(primary_key=True, verbose_name='КОД ДОЛЖНОСТИ')
	name_of_position = models.CharField(max_length=255, verbose_name='НАЗВАНИЕ ДОЛЖНОСТИ')

	def __str__(self):
		return '%s'%self.name_of_position
	class Meta:
		verbose_name = 'Список должностей'
		verbose_name_plural= 'Список должностей'
	def get_absolute_url(self):
		return reverse('view')

class Staff(models.Model):
	code_of_staff = models.AutoField(primary_key=True, verbose_name='КОД СОТРУДНИКА')
	name = models.CharField(max_length=255, verbose_name='ФИО СОТРУДНИКА')
	birthdate_of_staff = models.DateField(auto_now = True, verbose_name='ДАТА РОЖДЕНИЯ СОТРУДНИКА')
	code_of_passport = models.CharField(max_length=255, verbose_name='ПАСПОРТНЫЕ ДАННЫЕ')
	code_of_position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='КОД ДОЛЖНОСТИ')
	special_sign = models.CharField(max_length=255, verbose_name='ОСОБЫЕ ПРИМЕТЫ')
	m_e_data = models.CharField(max_length=255, verbose_name='ДАННЫЕ МЕДОСМОТРА')

	def __str__(self):
		return '%s' % self.name
	class Meta:
		verbose_name='Список сотрудников'
		verbose_name_plural='Список сотрудников'
	def get_absolute_url(self):
		return reverse('view')

class Crew(models.Model):
	code_of_crew = models.AutoField(primary_key=True, verbose_name='КОД ЭКИПАЖА')
	number_of_train = models.ForeignKey(Train, on_delete=models.CASCADE, verbose_name='НОМЕР ПОЕЗДА')
	number_of_rcar = models.CharField(max_length=255, verbose_name='НОМЕР ВАГОНА')
	code_of_staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name='КОД СОТРУДНИКА')

	def __str__(self):
		return "%s"%self.code_of_crew
	class Meta:
		verbose_name = 'Список экипажа'
		verbose_name_plural = 'Список экипажа'
	def get_absolute_url(self):
		return reverse('view')

class S_Station(models.Model):
	code_of_s_station = models.AutoField(primary_key=True, verbose_name='КОД ДОПОЛНИТЕЛЬНОЙ СТАНЦИИ')
	code_of_route = models.ForeignKey(Route, on_delete=models.CASCADE, verbose_name='КОД МАРШРУТА')
	time_of_arrive = models.DateField(auto_now=True, verbose_name='ВРЕМЯ ПРИБЫТИЯ')
	time_of_stop = models.DateField(auto_now=True, verbose_name='ВРЕМЯ СТОЯНКИ')
	code_of_station = models.ForeignKey(Station, on_delete=models.CASCADE, verbose_name='КОД СТАНЦИИ')

	def __str__(self):
		return '%s'%self.code_of_s_station
	class Meta:
		verbose_name = 'Список дополнительных станций'
		verbose_name_plural = 'Список дополнительных станций'
	def get_absolute_url(self):
		return reverse('view')