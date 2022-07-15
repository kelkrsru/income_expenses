from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import GroupProduct, Product, Unit


class ListProductsView(ListView):
    """Products list."""
    model = Product
    template_name = 'catalog/products_list.html'

    def get_queryset(self):
        if not self.request.GET.get('group'):
            return Product.objects.all()
        return Product.objects.filter(group=self.request.GET.get('group'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ListProductsView, self).get_context_data(**kwargs)
        context['groups'] = GroupProduct.objects.all()
        return context


class AddProductView(CreateView):
    """Add product."""
    model = Product
    fields = '__all__'
    template_name = 'catalog/products_form.html'
    success_url = reverse_lazy('catalog:products_list')


class UpdateProductView(UpdateView):
    """Update product."""
    model = Product
    fields = '__all__'
    template_name = 'catalog/products_form.html'
    success_url = reverse_lazy('catalog:products_list')


class DeleteProductView(DeleteView):
    """Delete product."""
    model = Product
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('catalog:products_list')


class ListUnitView(ListView):
    """Units list."""
    model = Unit
    template_name = 'catalog/units_list.html'


class AddUnitView(CreateView):
    """Add unit."""
    model = Unit
    fields = '__all__'
    template_name = 'catalog/units_form.html'
    success_url = reverse_lazy('catalog:units_list')


class UpdateUnitView(UpdateView):
    """Update unit."""
    model = Unit
    fields = '__all__'
    template_name = 'catalog/units_form.html'
    success_url = reverse_lazy('catalog:units_list')


class DeleteUnitView(DeleteView):
    """Delete unit."""
    model = Unit
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('catalog:units_list')


class ListGroupsView(ListView):
    """Groups list."""
    model = GroupProduct
    template_name = 'catalog/groups_list.html'


class AddGroupView(CreateView):
    """Add group."""
    model = GroupProduct
    fields = '__all__'
    template_name = 'catalog/groups_form.html'
    success_url = reverse_lazy('catalog:groups_list')


class UpdateGroupView(UpdateView):
    """Update group."""
    model = GroupProduct
    fields = '__all__'
    template_name = 'catalog/groups_form.html'
    success_url = reverse_lazy('catalog:groups_list')


class DeleteGroupView(DeleteView):
    """Delete group."""
    model = GroupProduct
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('catalog:groups_list')
