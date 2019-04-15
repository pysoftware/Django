from django.shortcuts import render
from django.views.generic import (ListView,
								  DetailView,
								  CreateView,
								  UpdateView, 
								  DeleteView
								 )
from .models import (City,Station,Route,
					Train,Crew,Staff,Position,S_Station)

class tableView(ListView):
	template_name = 'index.html'
	def get(self, request):
		all_cities = City.objects.all()
		all_stations = Station.objects.all()
		all_routes = Route.objects.all()
		all_trains = Train.objects.all()
		all_crews = Crew.objects.all()
		all_staff = Staff.objects.all()
		all_positions = Position.objects.all()
		all_s_stations = S_Station.objects.all()

		ctx = {
			'all_cities':all_cities,
			'all_stations':all_stations,
			'all_routes':all_routes,
			'all_trains':all_trains,
			'all_crews':all_crews,
			'all_staff':all_staff,
			'all_positions':all_positions,
			'all_s_stations':all_s_stations
		}
		return render(request, self.template_name, ctx)
# ---------------------------------------------------
class tableDetailCity(DetailView):
	template_name = 'city_detail.html'
	model = City
class tableCreateCity(CreateView):
	template_name = 'emp_forms.html'
	fields = ['name_of_city']
	model = City
class tableUpdateCity(UpdateView):
	template_name = 'emp_forms.html'
	fields = ['name_of_city']
	model = City
class tableDeleteCity(DeleteView):
	template_name = 'emp_confirm_delete.html'
	model = City
	success_url = '/'
# -----------------------------------------------
class tableDetailStation(DetailView):
	template_name = 'station_detail.html'
	model = Station
class tableCreateStation(CreateView):
	template_name = 'emp_forms.html'
	fields = ['name_of_station','code_of_city']
	model = Station
class tableUpdateStation(UpdateView):
	template_name = 'emp_forms.html'
	fields = ['name_of_station','code_of_city']
	model = Station
class tableDeleteStation(DeleteView):
	template_name = 'emp_confirm_delete.html'
	model = Station
	success_url = '/'
# ----------------------------------------------------
class tableDetailTrain(DetailView):
	template_name = 'train_detail.html'
	model = Train
class tableCreateTrain(CreateView):
	template_name = 'emp_forms.html'
	fields = ['type_of_train']
	model = Train
class tableUpdateTrain(UpdateView):
	template_name = 'emp_forms.html'
	fields = ['type_of_train']
	model = Train
class tableDeleteTrain(DeleteView):
	template_name = 'emp_confirm_delete.html'
	model = Train
	success_url = '/'
# ---------------------------------------------
class tableDetailRoute(DetailView):
	template_name = 'route_detail.html'
	model = Route
class tableCreateRoute(CreateView):
	template_name = 'emp_forms.html'
	fields = ['number_of_train','d_departure','d_arrival','point_of_departure','point_of_arrival']
	model = Route
class tableUpdateRoute(UpdateView):
	template_name = 'emp_forms.html'
	fields = ['number_of_train','d_departure','d_arrival','point_of_departure','point_of_arrival']
	model = Route
class tableDeleteRoute(DeleteView):
	template_name = 'emp_confirm_delete.html'
	model = Route
	success_url = '/'
# -----------------------------------------------------
class tableDetailPosition(DetailView):
	template_name = 'position_detail.html'
	model = Position
class tableCreatePosition(CreateView):
	template_name = 'emp_forms.html'
	fields = ['name_of_position']
	model = Position
class tableUpdatePosition(UpdateView):
	template_name = 'emp_forms.html'
	fields = ['name_of_position']
	model = Position
class tableDeletePosition(DeleteView):
	template_name = 'emp_confirm_delete.html'
	model = Position
	success_url = '/'
# ---------------------------------------------------
class tableDetailStaff(DetailView):
	template_name = 'staff_detail.html'
	model = Staff
class tableCreateStaff(CreateView):
	template_name = 'emp_forms.html'
	fields = ['name', 'code_of_passport','code_of_position','special_sign', 'm_e_data']
	model = Staff
class tableUpdateStaff(UpdateView):
	template_name = 'emp_forms.html'
	fields = ['name', 'code_of_passport','code_of_position','special_sign', 'm_e_data']
	model = Staff
class tableDeleteStaff(DeleteView):
	template_name = 'emp_confirm_delete.html'
	model = Staff
	success_url = '/'
# --------------------------------------------------------------
class tableDetailCrew(DetailView):
	template_name = 'crew_detail.html'
	model = Crew
class tableCreateCrew(CreateView):
	template_name = 'emp_forms.html'
	fields = ['number_of_train','number_of_rcar','code_of_staff']
	model = Crew
class tableUpdateCrew(UpdateView):
	template_name = 'emp_forms.html'
	fields = ['number_of_train','number_of_rcar','code_of_staff']
	model = Crew
class tableDeleteCrew(DeleteView):
	template_name = 'emp_confirm_delete.html'
	model = Crew
	success_url = '/'
# ---------------------------------------------------------------
class tableDetailS_Station(DetailView):
	template_name = 's_station_detail.html'
	model = S_Station
class tableCreateS_Station(CreateView):
	template_name = 'emp_forms.html'
	fields = ['code_of_route','code_of_station']
	model = S_Station
class tableUpdateS_Station(UpdateView):
	template_name = 'emp_forms.html'
	fields = ['code_of_route','code_of_station']
	model = S_Station
class tableDeleteS_Station(DeleteView):
	template_name = 'emp_confirm_delete.html'
	model = S_Station
	success_url = '/'