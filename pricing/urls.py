from django.urls import path

from pricing.views import (
    HomePageView,
    HousePriceEstimationUsingFloorAreaView,
    HousePriceEstimationUsingFloorAreaAndTownView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('house-pricing/floor-area/', HousePriceEstimationUsingFloorAreaView.as_view(), name='floor-area-pricing'),

    path(
        'house-pricing/floor-area-and-town/',
        HousePriceEstimationUsingFloorAreaAndTownView.as_view(),
        name='floor-area-and-town-pricing'
    ),
]