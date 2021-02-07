from django.utils import timezone
from django.shortcuts import render
from django.views.generic import ListView
# from django.shortcuts import render, redirect
# from django.core.paginator import Paginator, EmptyPage
from . import models


class HomeView(ListView):

    """ Home View """
   
    model = models.Room
    paginate_by = 10
    ordering = 'created'
    paginate_orphans = 5
    context_object_name = 'rooms'


def room_detail(request, pk):
    return render(request, "rooms/detail.html")

# def all_rooms(req):
#     page = req.GET.get("page", 1)
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 10, orphans=5)
#     try:
#         rooms = paginator.page(int(page))
#         return render(
#             req,
#             "rooms/home.html",
#             {"page": rooms},
#         )
#     except EmptyPage:
#         #rooms = paginator.page(1)
#         return redirect("/")
#     # rooms = paginator.get_page(page)
