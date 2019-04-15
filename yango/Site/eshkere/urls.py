from django.contrib import admin
from django.urls import path, include
from .views import (tableView,

					tableDetailCity,
					tableCreateCity,
					tableUpdateCity,
					tableDeleteCity,

					tableDetailStation,
					tableCreateStation,
					tableUpdateStation,
					tableDeleteStation,

					tableDetailTrain,
					tableCreateTrain,
					tableUpdateTrain,
					tableDeleteTrain,

					tableDetailRoute,
					tableCreateRoute,
					tableUpdateRoute,
					tableDeleteRoute,

					tableDetailPosition,
					tableCreatePosition,
					tableUpdatePosition,
					tableDeletePosition,

					tableDetailStaff,
					tableCreateStaff,
					tableUpdateStaff,
					tableDeleteStaff,

					tableDetailCrew,
					tableCreateCrew,
					tableUpdateCrew,
					tableDeleteCrew,

					tableDetailS_Station,
					tableCreateS_Station,
					tableUpdateS_Station,
					tableDeleteS_Station
					)

urlpatterns = [
	path('', tableView.as_view(), name = 'view'),

	path('<int:pk>/', tableDetailCity.as_view(), name='city'),
	path('newcity/', tableCreateCity.as_view(), name='newcity'),
	path('updatecity/<int:pk>', tableUpdateCity.as_view(), name='updatecity'),
	path('deletecity/<int:pk>', tableDeleteCity.as_view(), name='deletecity'),

	path('s/<int:pk>/', tableDetailStation.as_view(), name='station'),
	path('newstation/', tableCreateStation.as_view(), name='newstation'),
	path('updatestation/<int:pk>', tableUpdateStation.as_view(), name='updatestation'),
	path('deletestation/<int:pk>', tableDeleteStation.as_view(), name='deletestation'),

	path('r/<int:pk>/', tableDetailRoute.as_view(), name='route'),
	path('newroute/', tableCreateRoute.as_view(), name='newroute'),
	path('updateroute/<int:pk>', tableUpdateRoute.as_view(), name='updateroute'),
	path('deleteroute/<int:pk>', tableDeleteRoute.as_view(), name='deleteroute'),

	path('t/<int:pk>/', tableDetailTrain.as_view(), name='train'),
	path('newtrain/', tableCreateTrain.as_view(), name='newtrain'),
	path('updatetrain/<int:pk>', tableUpdateTrain.as_view(), name='updatetrain'),
	path('deletetrain/<int:pk>', tableDeleteTrain.as_view(), name='deletetrain'),

	path('c/<int:pk>/', tableDetailCrew.as_view(), name='crew'),
	path('newcrew/', tableCreateCrew.as_view(), name='newcrew'),
	path('updatecrew/<int:pk>', tableUpdateCrew.as_view(), name='updatecrew'),
	path('deletecrew/<int:pk>', tableDeleteCrew.as_view(), name='deletecrew'),

	path('st/<int:pk>/', tableDetailStaff.as_view(), name='staff'),
	path('newstaff/', tableCreateStaff.as_view(), name='newstaff'),
	path('updatestaff/<int:pk>', tableUpdateStaff.as_view(), name='updatestaff'),
	path('deletestaff/<int:pk>', tableDeleteStaff.as_view(), name='deletestaff'),

	path('p/<int:pk>/', tableDetailPosition.as_view(), name='position'),
	path('newposition/', tableCreatePosition.as_view(), name='newposition'),
	path('updateposition/<int:pk>', tableUpdatePosition.as_view(), name='updateposition'),
	path('deleteposition/<int:pk>', tableDeletePosition.as_view(), name='deleteposition'),

	path('ss/<int:pk>/', tableDetailS_Station.as_view(), name='s_station'),
	path('news_station/', tableCreateS_Station.as_view(), name='news_station'),
	path('updates_station/<int:pk>', tableUpdateS_Station.as_view(), name='updates_station'),
	path('deletes_station/<int:pk>', tableDeleteS_Station.as_view(), name='deletes_station'),
]
