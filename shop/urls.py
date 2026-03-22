from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="shoppage"),
    path('about/',views.about,name="aboutus"),
    path('contact/',views.contact,name="contact"),
    path('tracker/',views.tracker,name="tracker"),
    path('search/',views.search,name="search"),
    path('productview/',views.productview,name="product"),
    path('checkout/',views.checkout,name="checkout"),
    # path('cart',views.index,name="cart")

]
