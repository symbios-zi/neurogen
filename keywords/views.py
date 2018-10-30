from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.urls import reverse

from keywords.forms import KeywordForm
from keywords.models import Keywords


def list(request):
    keywords_list = Keywords.objects.all()
    paginator = Paginator(keywords_list, 25)
    page = request.GET.get('page')
    keywords = paginator.get_page(page)

    return render(request, 'list.html', {'keywords': keywords})


def create(request):
    if request.POST:
        form = KeywordForm(request.POST)
    else:
        form = KeywordForm()
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('create'))
    return render(request, 'create.html', {'form': form})


def update(request, id):
    instance = Keywords.objects.get(pk=id)
    form = KeywordForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('list'))
    return render(request, 'update.html', {'form': form, 'id':id})


def parse(request, id):
    instance = Keywords.objects.get(pk=id)
    instance.parse()
    return HttpResponseRedirect(reverse('list'))

