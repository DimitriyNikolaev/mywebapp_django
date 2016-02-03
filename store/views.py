from django.shortcuts import render, render_to_response
from store.models import Good,Group
from django.core.paginator import Paginator


# Create your views here.
def main_page(request):
    args = {}
    all_good = Good.objects.all()
    args["current_group"] = None
    page = request.GET.get('p')
    filtered_goods = Paginator(all_good,6)
    args["goods"] = filtered_goods.page(page if page != None else 1)
    args["groups"] = Group.objects.all()

    return render_to_response('main.html',args)

def about_page(request):
    return render_to_response('about.html')

def main_page_filtered(request, group = 0):
    args = {}
    all_good = Good.objects.filter(good_group_id=group)
    args["current_group"] = Group.objects.get(id=group)
    page = request.GET.get('p')
    filtered_goods = Paginator(all_good,6)
    args["goods"] = filtered_goods.page(page if page != None else 1)
    args["groups"] = Group.objects.all()

    return render_to_response('main.html',args)