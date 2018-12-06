from django.urls import path
from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('modules/',views.ModuleListView.as_view(),name='modules'),
	path('ts/',views.TSListView.as_view(),name='TS'),
	path('module/<int:pk>', views.ModuleDetailView.as_view(), name='module-detail'),
	path('ts/<int:pk>', views.TSDetailView.as_view(), name='ts-detail'),
]

