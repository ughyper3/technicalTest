import datetime

from django.http import HttpResponse
from django.template import loader
from .models import Product
from .form import productForm
from django.shortcuts import redirect


def index(request):

# check if we should create a new product or update existing product

    if request.method == "POST":

        if not Product.objects.filter(GTIN=request.POST['GTIN']).exists(): # create a new product

            form = productForm(request.POST).save()
            return redirect('/cbPlus')

        else: # update existing product / doesn't work / problem of data type ?

            update_product = Product.objects.filter(GTIN=request.POST['GTIN'])
            requestDateTime = datetime.datetime.strptime(request.POST['expiryDate'], '%Y-%m-%d') # str to datetime
            update_product.expiryDate = requestDateTime # datetime
            form = update_product.update() # ?
            return redirect('/cbPlus')

    else:
        form = productForm() # generate form

    template = loader.get_template('cbPlus/index.html')
    product = Product.objects.order_by('expiryDate')
    context = {
        'product': product,
        'form': form
    }
    return HttpResponse(template.render(context, request=request))

