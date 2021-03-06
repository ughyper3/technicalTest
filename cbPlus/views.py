from django.http import HttpResponse
from .models import Product
from django.template import loader
from .form import productForm
from django.shortcuts import redirect

def index(request):

    if request.method == "POST":
        form = productForm(request.POST).save()
        return redirect('/cbPlus')
    else :
        form = productForm()

    template = loader.get_template('cbPlus/index.html')
    product = Product.objects.order_by('expiryDate')
    context = {
        'product' : product,
        'form' : form
    }
    return HttpResponse(template.render(context, request=request))
