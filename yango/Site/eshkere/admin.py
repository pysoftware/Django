from django.contrib import admin
from . import models
from .views import (City,Station,Route,
					Train,Crew,Staff,Position,S_Station)
# City
# Station
# Route
# Train
# Crew
# Staff
# Position
# S_Station
class Cityv(admin.ModelAdmin):
	list_display = [field.name for field in models.City._meta.fields]

	class Meta:
		model = models.City
class Stationv(admin.ModelAdmin):
	list_display = [field.name for field in models.Station._meta.fields]

	class Meta:
		model = models.Station	
class Routev(admin.ModelAdmin):
	list_display = [field.name for field in models.Route._meta.fields]

	class Meta:
		model = models.Route
class Trainv(admin.ModelAdmin):
	list_display = [field.name for field in models.Train._meta.fields]

	class Meta:
		model = models.Train
class Crewv(admin.ModelAdmin):
	list_display = [field.name for field in models.Crew._meta.fields]

	class Meta:
		model = models.Crew		
class Staffv(admin.ModelAdmin):
	list_display = [field.name for field in models.Staff._meta.fields]

	class Meta:
		model = models.Staff
class Positionv(admin.ModelAdmin):
	list_display = [field.name for field in models.Position._meta.fields]

	class Meta:
		model = models.Position
class S_Stationv(admin.ModelAdmin):
	list_display = [field.name for field in models.S_Station._meta.fields]

	class Meta:
		model = models.S_Station
admin.site.register(City, Cityv)
admin.site.register(Station, Stationv)
admin.site.register(Route, Routev)
admin.site.register(Staff, Staffv)
admin.site.register(Position, Positionv)
admin.site.register(S_Station, S_Stationv)
admin.site.register(Crew, Crewv)
admin.site.register(Train, Trainv)