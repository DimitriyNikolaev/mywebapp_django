from django.shortcuts import render, render_to_response
from store.models import Good,Group
from django.core.paginator import Paginator


# Create your views here.
def main_page(request, group = 0, page = 1):
    args = {}
    if group != 0 and group != '0':
        all_good = Good.objects.filter(good_group_id=group)
        args["current_group"] = Group.objects.get(id=group)
    else:
        all_good = Good.objects.all()
        args["current_group"] = group

    filtered_goods = Paginator(all_good,6)
    args["goods"] = filtered_goods.page(page)
    args["groups"] = Group.objects.all()

    return render_to_response('main.html',args)

def about_page(request):
    return render_to_response('about.html')