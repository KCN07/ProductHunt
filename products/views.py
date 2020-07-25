from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product

def home(request):
    products=Product.objects
    return render(request,'products/home.html', {'products':products})

@login_required(login_url="/accounts/signup")
def create(request):
    if request.method=='POST':

        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:

            product = Product()
            product.title=request.POST['title']
            product.body=request.POST['body']

            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url=request.POST['url']
            else:
                product.url='http://' + request.POST['url']

            product.icon=request.FILES['icon']
            product.image=request.FILES['image']
            product.hunter=request.user
            product.save()
            return redirect('/products/'+ str(product.id))


        else:
            return render(request,'products/create.html',{'error':'All fields are required'})

    else:
        return render(request,'products/create.html')


def detail(request, product_id):
    detailproduct = get_object_or_404(Product, pk=product_id)
    print(str(detailproduct.body))
    return render(request,'products/detail.html', {'product':detailproduct})

@login_required(login_url="/accounts/signup")
def upvote(request, product_id):
    if request.method=='POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total +=1
        product.save()
        return redirect('/products/'+ str(product.id))