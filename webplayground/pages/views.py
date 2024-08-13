from ast import arg
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from .models import Page
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from .forms import PageForm
# Create your views here.


# class StaffRequiredMixin(object):
#     """Este Mixin requerirá que el usuario sea miembro del Staff"""
#     @method_decorator(staff_member_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs) # type: ignore


class PageListView(ListView):
    model = Page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


class PageDetailView(DetailView):
    model = Page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


# CRUD methods
@method_decorator(staff_member_required, name='dispatch')
class PageCreateView(CreateView):
    model = Page
    form_class = PageForm
    # fields = ['title', 'content', 'order']
    success_url = reverse_lazy('pages:pages')


@method_decorator(staff_member_required, name='dispatch')
class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    # fields = ['title', 'content', 'order']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        # type: ignore
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok' # type: ignore


@method_decorator(staff_member_required, name='dispatch')
class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')
