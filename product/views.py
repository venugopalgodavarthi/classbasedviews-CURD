from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from product.models import productmodel
# Create your views here.
def home(request):
    return render(request,"home.html")

class viewlist(ListView):
    model= productmodel
    template_name="list.html"
    context_object_name='form1'

class viewcreate(CreateView):
    model= productmodel
    fields='__all__'
    template_name="create.html"
    context_object_name='form1'
    success_url=reverse_lazy('home')


class viewupdate(UpdateView):
    model= productmodel
    fields='__all__'
    template_name="update.html"
    context_object_name='form1'
    success_url=reverse_lazy('details')

class viewdelete(DeleteView):
    model= productmodel
    template_name="delete.html"
    success_url=reverse_lazy('details')