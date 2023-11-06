from django.shortcuts import render
from .models import Product, Testimonial, Blog
from django.core.paginator import Paginator

def index(request):
    testimonial = Testimonial.objects.all()
    paginate_blog = Paginator(Blog.objects.all().order_by('name'), 3)
    page = request.GET.get('page')
    blogs = paginate_blog.get_page(page)

    paginate_product = Paginator(Product.objects.all().order_by('name'), 3)
    page_product = request.GET.get('page')
    product = paginate_product.get_page(page_product)
    return render(request, 'index.html', {'navbar': 'index', 'testimonial': testimonial, 'blogs':blogs, 'product': product})


def shop(request):
    product = Product.objects.all()
    return render(request, 'shop.html', {'navbar': 'shop', 'product': product})


def about(request):
    testimonial = Testimonial.objects.all()
    return render(request, 'about.html', {'navbar': 'about', 'testimonial': testimonial})


def services(request):
    testimonial = Testimonial.objects.all()

    paginate_product = Paginator(Product.objects.all().order_by('name'), 3)
    page_product = request.GET.get('page')
    product = paginate_product.get_page(page_product)
    return render(request, 'services.html', {'navbar': 'services', 'testimonial': testimonial, 'product': product})


def blog(request):
    testimonial = Testimonial.objects.all()
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'navbar': 'blog', 'testimonial': testimonial, 'blogs': blogs})


def contact(request):
    return render(request, 'contact.html', {'navbar': 'contact'})


def cart(request):
    return render(request, 'cart.html', {'navbar': 'cart'})


def checkout(request):
    return render(request, 'checkout.html', {'navbar': 'checkout'})


def thankyou(request):
    return render(request, 'thankyou.html')
