# from django.utils import timezone
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, View
# from django.http import Http404
# from django.shortcuts import render, redirect
# from django_countries import countries
from . import models, forms

# from django.core.paginator import Paginator, EmptyPage


class HomeView(ListView):

    """ Home View """
   
    model = models.Room
    paginate_by = 12
    ordering = 'created'
    paginate_orphans = 5
    context_object_name = 'rooms'


class RoomDetail(DetailView):

    """ Room Detail """

    model = models.Room
    pk_url_kwarg = 'pk'


class SearchView(View):
    """Search view"""

    def get(self, req):
        country = req.GET.get('country')

        if country:
            form = forms.SearchForm(req.GET)

            if form.is_valid():
                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if room_type is not None:
                    filter_args["room_type"] = room_type

                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms

                if beds is not None:
                    filter_args["beds__gte"] = beds

                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True

                if superhost is True:
                    filter_args["host__superhost"] = True

                for amenity in amenities:
                    filter_args["amenities"] = amenity

                for facility in facilities:
                    filter_args["facilities"] = facility

                qs = models.Room.objects.filter(**filter_args).order_by("-created")
                paginator = Paginator(qs, 10, orphans=5)
                page = req.GET.get('page', 1)
                rooms = paginator.get_page(page)
                return render(req, "rooms/search.html", {"form": form, "rooms": rooms})
        else:
            rooms = models.Room.objects.filter(**filter_args)

        return render(req, "rooms/search.html", {"form": form})


# def search(req):
#     form = forms.SearchForm()
#     return render(req, "rooms/search.html", {"form":form})

# def search(req):
#     city = req.GET.get('city', 'Anywhere')
#     city = str.capitalize(city)
#     country = req.GET.get('country', 'KR')
#     room_type = int(req.GET.get('room_type', 0))
#     price = int(req.GET.get("price", 0))
#     guests = int(req.GET.get("guests", 0))
#     bedrooms = int(req.GET.get("bedrooms", 0))
#     beds = int(req.GET.get("beds", 0))
#     baths = int(req.GET.get("baths", 0))
#     s_amenities = req.GET.getlist("amenities")
#     s_facilities = req.GET.getlist("facilities")
#     instant = bool(req.GET.get('instant', False))
#     superhost = bool(req.GET.get('superhost', False))

#     room_types = models.RoomType.objects.all()
#     amenities = models.Amenity.objects.all()
#     facilities = models.Facility.objects.all()
    
#     form = {
#         "city": city,
#         "s_room_type": room_type,
#         "s_country": country,
#         "price": price,
#         "guests": guests,
#         "bedrooms": bedrooms,
#         "beds": beds,
#         "baths": baths,
#         "s_amenities": s_amenities,
#         "s_facilities": s_facilities,
#         "instant": instant,
#         "superhost": superhost,
#     }

#     choices = {
#         "countries": countries, 
#         "room_types": room_types,
#         "amenities": amenities,
#         "facilities": facilities,
#     }

#     filter_args = {}

#     if city != "Anywhere":
#         filter_args['city__startswith'] = city

#     filter_args['country'] = country

#     if room_types != 0:
#         filter_args['room_type__pk'] = room_type

#     if price != 0:
#         filter_args["price__lte"] = price

#     if guests != 0:
#         filter_args["guests__gte"] = guests

#     if bedrooms != 0:
#         filter_args["bedrooms__gte"] = bedrooms

#     if beds != 0:
#         filter_args["beds__gte"] = beds

#     if baths != 0:
#         filter_args["baths__gte"] = baths

#     if instant is True:
#         filter_args["instant_book"] = True

#     if superhost is True:
#         filter_args["host__superhost"] = True

#     if len(s_amenities) > 0:
#         for s_amenity in s_amenities:
#             filter_args["amenities__pk"] = int(s_amenity)

#     if len(s_facilities) > 0:
#         for s_facility in s_facilities:
#             filter_args["facilities__pk"] = int(s_facility)

#     rooms = models.Room.objects.filter(**filter_args)

#     return render(
#         req,
#         "rooms/search.html",
#         {**form, **choices, "rooms": rooms}
#     )

# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {"room": room})
#     except models.Room.DoesNotExist:
#         raise Http404()


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
