from django.urls import path
from . import views

app_name = "client"
urlpatterns = [
    path('', views.index, name="Index"),
    path('shop', views.shop, name="Shop"),
    path('about', views.about, name="About"),
    path('services', views.services, name="Services"),
    path('blog', views.blog, name="Blog"),
    path('contact', views.contact, name="Contact"),
    path('cart', views.cart, name="Cart"),
    path('checkout', views.checkout, name="Checkout"),
    path('thankyou', views.thankyou, name="Thankyou")

]
