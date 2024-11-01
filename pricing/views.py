from django.views.generic import TemplateView
from django.shortcuts import render

from pricing.utils import estimate_house_price_using_floor_area, estimate_house_price_using_floor_area_and_location


class HomePageView(TemplateView):
    template_name = 'pricing/index.html'


class HousePriceEstimationUsingFloorAreaView(TemplateView):
    template_name = 'pricing/floor-area-pricing.html'

    def post(self, request, *args, **kwargs):
        floor_area = request.POST.get('area')
        price = estimate_house_price_using_floor_area(floor_area)

        return render(request, self.template_name, {'price': price, 'area': floor_area})


class HousePriceEstimationUsingFloorAreaAndTownView(TemplateView):
    template_name = 'pricing/floor-area-and-town-pricing.html'

    def post(self, request, *args, **kwargs):
        floor_area = request.POST.get('area')
        location = request.POST.get('location')
        price = estimate_house_price_using_floor_area_and_location(floor_area, location)

        return render(request, self.template_name, {'price': price, 'area': floor_area, 'location': location.title()})
