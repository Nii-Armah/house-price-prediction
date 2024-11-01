from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pricing/index.html'


class HousePriceEstimationUsingFloorAreaView(TemplateView):
    template_name = 'pricing/floor-area-pricing.html'


class HousePriceEstimationUsingFloorAreaAndTownView(TemplateView):
    template_name = 'pricing/floor-area-and-town-pricing.html'

