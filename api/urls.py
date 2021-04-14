from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('companies', views.show_companies),
    path('companies/<int:company_id>', views.show_company),
    path('companies/<int:company_id>/vacancies', views.show_company_vacancies),
    path('vacancies', views.show_vacancies),
    path('vacancies/<int:vacancy_id>', views.show_vacancy),
    path('vacancies/top_ten', views.show_top_ten),

]
