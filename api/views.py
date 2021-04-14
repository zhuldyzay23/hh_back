from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Company, Vacancy

def show_companies(request):
    companies = list(Company.objects.values())
    return JsonResponse(companies, safe=False)

def show_company(request, company_id):
    company = list(Company.objects.filter(id=company_id).values())
    return JsonResponse(company, safe=False)

def show_company_vacancies(request, company_id):
    vacancies = list(Vacancy.objects.filter(id = company_id).values())
    return JsonResponse(vacancies, safe=False)

def show_vacancies(request):
    vacancies = list(Vacancy.objects.values())
    return JsonResponse(vacancies, safe=False)

def show_vacancy(request, vacancy_id):
    vacancy = list(Vacancy.objects.filter(id=vacancy_id).values())
    return JsonResponse(vacancy, safe=False)

def show_top_ten(request):
    vacancies = list(Vacancy.objects.order_by('-salary')[:10].values())
    return JsonResponse(vacancies, safe=False)
