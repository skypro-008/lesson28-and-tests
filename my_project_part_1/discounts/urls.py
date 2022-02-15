# TODO настраиваем urls здесь
from discounts.views import DiscountDetailView, DiscountListView
from django.urls import path

urlpatterns = [
    path("discount/", DiscountListView.as_view()),
    path("discount/<int:pk>", DiscountDetailView.as_view()),
]
