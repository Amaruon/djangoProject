from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('report-page/', views.report_page, name='report-page'),
    path('report/<str:pk>', views.report, name='report'),
    path('expenses/', views.expense, name='expense')
]
