from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Property
from django.db.models import Q

# Create your views here.
class PropertyListView(ListView):
    model = Property
    template_name = 'properties/property-grid.html'
    paginate_by = 6

    def get_queryset(self):
        return super().get_queryset().all()


class PropertyDetailView(DetailView):
    model = Property
    template_name = 'properties/property-detail.html'
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        property = self.get_object()
        context['property_images'] = property.property_images.all()
        context['amenities'] = property.amenity.all()
        return context


class PropertySearchView(View):
    def get(self, request):
        status = request.GET.get('status')
        keyword = request.GET.get('keyword')
        beds = request.GET.get('beds')
        garages = request.GET.get('garages')
        baths = request.GET.get('baths')


        properties = Property.objects.all()

        if status:
            properties = properties.filter(status=status)

        if keyword:
            properties = properties.filter(Q(name__icontains=keyword) | Q(description__icontains=keyword) |
                                           Q(house_address__icontains=keyword) | Q(street__icontains=keyword))

        if beds:
            properties = properties.filter(beds=beds)

        if garages:
            properties = properties.filter(garages=garages)

        if baths:
            properties = properties.filter(baths=baths)

        context = {
            'properties': properties,
        }

        return render(request, 'properties/property-search.html', context)


