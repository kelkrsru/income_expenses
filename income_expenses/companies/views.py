from datetime import datetime
from dadata import Dadata

from django.http import JsonResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy

from .models import Company, CompanyType
from .forms import CompanyForm, RequisitesForm


def companies_list(request):
    """Companies list."""
    template = 'companies/companies_list.html'
    companies = Company.objects.all()
    context = {
        'companies': companies
    }
    return render(request, template, context)


def company_add(request):
    """Company add."""
    template = 'companies/company_form.html'

    form_company = CompanyForm(request.POST or None)
    form_requisites = RequisitesForm(request.POST or None)

    if not all((form_requisites.is_valid(), form_company.is_valid())):
        context = {
            'form_company': form_company,
            'form_requisites': form_requisites
        }
        return render(request, template, context)

    requestes = form_requisites.save()
    company = form_company.save(commit=False)
    company.requisites = requestes
    company.save()
    return redirect(reverse('companies:companies_list'))


def company_update(request, pk):
    """Company update."""
    template = 'companies/company_form.html'

    company = get_object_or_404(Company, pk=pk)

    form_company = CompanyForm(request.POST or None, instance=company)
    form_requisites = RequisitesForm(request.POST or None,
                                     instance=company.requisites)

    if not all((form_requisites.is_valid(), form_company.is_valid())):
        context = {
            'form_company': form_company,
            'form_requisites': form_requisites
        }
        return render(request, template, context)

    form_requisites.save()
    form_company.save()
    return redirect(reverse('companies:companies_list'))


def company_type_list(request):
    """Company types list."""
    template = 'companies/company_type_list.html'
    company_types = CompanyType.objects.all()
    context = {
        'company_types': company_types,
    }
    return render(request, template, context)


class AddCompanyTypeView(CreateView):
    """Add company type."""
    model = CompanyType
    template_name = 'companies/company_type_form.html'
    success_url = reverse_lazy('companies:company_type_list')
    fields = ['name']


class UpdateCompanyTypeView(UpdateView):
    """Update company type."""
    model = CompanyType
    template_name = 'companies/company_type_form.html'
    success_url = reverse_lazy('companies:company_type_list')
    fields = ['name']


class DeleteCompanyTypeView(DeleteView):
    """Delete company type."""
    model = CompanyType
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('companies:company_type_list')


def find_by_inn(request):
    """Find company by INN in service dadata.ru."""
    inn = request.POST.get('inn')
    token = '13cc99c2be673c64fd88136dceeacd7e34c9aebd'
    dadata = Dadata(token)
    result = dadata.find_by_id('party', inn)
    if not result:
        return JsonResponse({'status': 'not_found'})
    return JsonResponse({
        'status': 'found',
        'kpp': (result[0]['data']['kpp']
                if 'kpp' in result[0]['data'] else None),
        'ogrn': result[0]['data']['ogrn'],
        'short_name': result[0]['data']['name']['short_with_opf'],
        'full_name': result[0]['data']['name']['full_with_opf'],
        'position_director': (result[0]['data']['management']['post']
                              if 'management' in result[0]['data'] else None),
        'name_director': (result[0]['data']['management']['name']
                          if 'management' in result[0]['data'] else None),
        'legal_address': result[0]['data']['address']['unrestricted_value'],
        'date_reg': datetime.utcfromtimestamp(int(str(
            result[0]['data']['ogrn_date'])[:-3])).strftime('%Y-%m-%d'),
    })
