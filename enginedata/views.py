from django.shortcuts import render

from enginedata.models import Technicaldata, ModuleVersion

from django.views import generic

from django.utils import translation

def index(request):
	"""View function for home page of site"""

	num_modules = ModuleVersion.objects.all().count()

	num_TS = Technicaldata.objects.all().count()

	num_visits = request.session.get('num_visits',0)
	request.session['num_visits'] = num_visits + 1

	context = {

		'num_modules':num_modules,

		'num_TS':num_TS,

		'num_visits':num_visits,

	}

	return render(request,'index.html',context=context)


class ModuleListView(generic.ListView):
	model = ModuleVersion
	paginate_by = 15


class ModuleDetailView(generic.DetailView):
	model = ModuleVersion

class TSListView(generic.ListView):
	model = Technicaldata
	paginate_by = 15

class TSDetailView(generic.DetailView):
	model = Technicaldata