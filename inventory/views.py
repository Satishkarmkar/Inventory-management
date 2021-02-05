from django.db.models import Q
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from datetime import date
from datetime import datetime, timedelta, time
import random

def index(request):
    return render(request, 'index.html')

def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'admin_login.html',d)


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    bcount = Brand.objects.filter(status="1").count()
    ccount = Category.objects.filter(status="1").count()
    scount = SubCategory.objects.filter(status="1").count()
    pcount = Product.objects.filter(status="1").count()
    suppcount = Supplier.objects.filter(status="1").count()
    custcount = Customer.objects.all().count()


    d = {'bcount': bcount,'ccount': ccount,'scount': scount,'pcount': pcount,'suppcount':suppcount,'custcount': custcount}
    return render(request, 'dashboard.html',d)


def Logout(request):
    logout(request)
    return redirect('admin_login')


def changepassword(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method=="POST":
        o = request.POST['currentpassword']
        n = request.POST['newpassword']
        c = request.POST['confirmpassword']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error = "yes"
        else:
            error = "not"
    d = {'error':error}
    return render(request,'changepassword.html',d)




def add_category(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method=="POST":
        cn = request.POST['category']
        st = request.POST['status']
        try:
            Category.objects.create(categoryname=cn,status=st)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'add_category.html', d)


def manage_category(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    category = Category.objects.all()
    d = {'category':category}
    return render(request, 'manage_category.html', d)


def edit_category(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    category = Category.objects.get(id=pid)

    error = ""
    if request.method == 'POST':
        cn = request.POST['category']
        if 'status'in request.POST :
            st = request.POST['status']
        else:
            st = "0"
        category.categoryname = cn
        category.status = st

        try:
            category.save()
            error = "no"
        except:
            error = "yes"
    d = {'error': error,'category':category}
    return render(request, 'edit_category.html',d)

def delete_category(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    category = Category.objects.get(id=pid)
    category.delete()
    return redirect('manage_category')


def add_subcategory(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    category = Category.objects.filter(status="1")
    if request.method=="POST":
        cn = request.POST['catid']
        scn = request.POST['subcategory']
        st = request.POST['status']
        categoryid = Category.objects.get(id=cn)
        try:
            SubCategory.objects.create(categoryid=categoryid,subcategoryname=scn,status=st)
            error = "no"
        except:
            error = "yes"
    d = {'error':error,'category':category}
    return render(request, 'add_subcategory.html', d)


def manage_subcategory(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    subcategory = SubCategory.objects.all()
    d = {'subcategory':subcategory}
    return render(request, 'manage_subcategory.html', d)


def edit_subcategory(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    category = Category.objects.filter(status="1")
    subcategory = SubCategory.objects.get(id=pid)

    error = ""
    if request.method == 'POST':
        cn = request.POST['category']
        scn = request.POST['subcat']
        categoryid = Category.objects.get(id=cn)
        if 'status'in request.POST :
            st = request.POST['status']
        else:
            st = "0"
        subcategory.categoryid = categoryid
        subcategory.subcategoryname = scn
        subcategory.status = st
        try:
            subcategory.save()
            error = "no"
        except:
            error = "yes"
    d = {'error': error,'subcategory':subcategory,'category':category}
    return render(request, 'edit_subcategory.html',d)

def delete_subcategory(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    subcategory = SubCategory.objects.get(id=pid)
    subcategory.delete()
    return redirect('manage_subcategory')

def add_brand(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method=="POST":
        bn = request.POST['brandname']
        st = request.POST['status']
        try:
            Brand.objects.create(brandname=bn,status=st)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'add_brand.html', d)


def manage_brand(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    brand = Brand.objects.all()
    d = {'brand':brand}
    return render(request, 'manage_brand.html', d)


def edit_brand(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    brand = Brand.objects.get(id=pid)

    error = ""
    if request.method == 'POST':
        bn = request.POST['brandname']
        if 'status'in request.POST :
            st = request.POST['status']
        else:
            st = "0"
        brand.brandname = bn
        brand.status = st

        try:
            brand.save()
            error = "no"
        except:
            error = "yes"
    d = {'error': error,'brand':brand}
    return render(request, 'edit_brand.html',d)

def delete_brand(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    brand = Brand.objects.get(id=pid)
    brand.delete()
    return redirect('manage_brand')


def add_product(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    category = Category.objects.filter(status="1")
    brand = Brand.objects.filter(status="1")
    if request.method=="POST":
        pn = request.POST['pname']
        cn = request.POST['category']
        scn = request.POST['subcategory']
        bn = request.POST['bname']
        mn = request.POST['modelno']
        stock = request.POST['stock']
        pr = request.POST['price']
        st = request.POST['status']
        rem = stock
        categoryid = Category.objects.get(id=cn)
        subcategoryid = SubCategory.objects.get(id=scn)
        brandid = Brand.objects.get(id=bn)
        try:
            Product.objects.create(productname=pn,categoryid=categoryid,subcategoryid=subcategoryid,brandid=brandid,modelnumber=mn,stock=stock,price=pr,status=st,rem=rem,creationdate=date.today())
            error = "no"
        except:
            error = "yes"
    d = {'error':error,'category':category,'brand':brand}
    return render(request, 'add_product.html', d)


def manage_product(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    product = Product.objects.all()
    d = {'product':product}
    return render(request, 'manage_product.html', d)


def edit_product(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    category = Category.objects.filter(status="1")
    brand = Brand.objects.filter(status="1")
    product = Product.objects.get(id=pid)

    error = ""
    if request.method == 'POST':
        pn = request.POST['pname']
        cn = request.POST['category']
        scn = request.POST['subcategory']
        bn = request.POST['bname']
        mn = request.POST['modelno']
        stock = request.POST['stock']
        pr = request.POST['price']
        categoryid = Category.objects.get(id=cn)
        subcategoryid = SubCategory.objects.get(id=scn)
        brandid = Brand.objects.get(id=bn)
        if 'status' in request.POST :
            st = request.POST['status']
        else:
            st = "0"
        product.productname = pn
        product.categoryid = categoryid
        product.subcategoryid = subcategoryid
        product.brandid = brandid
        product.modelnumber = mn
        product.stock = stock
        product.price = pr
        product.status = st
        try:
            product.save()
            error = "no"
        except:
            error = "yes"
    d = {'error': error,'product':product,'category':category,'brand':brand}
    return render(request, 'edit_product.html',d)

def delete_product(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    product = Product.objects.get(id=pid)
    product.delete()
    return redirect('manage_product')



def load_subcategory(request):
    categoryid = request.GET.get('category')
    subcategory = SubCategory.objects.filter(categoryid=categoryid,status="1").order_by('subcategoryname')
    return render(request, 'subcategory_dropdown_list_options.html', {'subcategory': subcategory})

def add_supplier(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    category = Category.objects.filter(status="1")
    # brand = Brand.objects.filter(status="1")
    if request.method=="POST":
        sn = request.POST['suppname']
        smob = request.POST['suppmob']
        saddr = request.POST['suppaddr']
        semail = request.POST['suppemail']
        cn = request.POST['category']
        scn = request.POST['subcategory']
        # bn = request.POST['bname']
        st = request.POST['status']
        categoryid = Category.objects.get(id=cn)
        subcategoryid = SubCategory.objects.get(id=scn)
        # brandid = Brand.objects.get(id=bn)
        try:
            Supplier.objects.create(suppliername=sn,suppliermob=smob,supplieraddr=saddr,supplieremail=semail,categoryid=categoryid,subcategoryid=subcategoryid,status=st)
            error = "no"
        except:
            error = "yes"
    d = {'error':error,'category':category}
    return render(request, 'add_supplier.html', d)

def manage_supplier(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    supplier = Supplier.objects.all()
    d = {'supplier':supplier}
    return render(request, 'manage_supplier.html', d)

def edit_supplier(request,suppid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    category = Category.objects.filter(status="1")
    # brand = Brand.objects.filter(status="1")
    supplier = Supplier.objects.get(id=suppid)

    error = ""
    if request.method == 'POST':
        sn = request.POST['suppname']
        smob = request.POST['suppmob']
        saddr = request.POST['suppaddr']
        semail = request.POST['suppemail']
        cn = request.POST['category']
        scn = request.POST['subcategory']
        # bn = request.POST['bname']
        st = request.POST['status']
        categoryid = Category.objects.get(id=cn)
        subcategoryid = SubCategory.objects.get(id=scn)
        # brandid = Brand.objects.get(id=bn)
        if 'status' in request.POST :
            st = request.POST['status']
        else:
            st = "0"
        supplier.suppliername = sn
        supplier.suppliermob = smob
        supplier.supplieraddr = saddr
        supplier.supplieremail = semail
        supplier.categoryid = categoryid
        supplier.subcategoryid = subcategoryid
        # product.brandid = brandid
        supplier.status = st
        try:
            supplier.save()
            error = "no"
        except:
            error = "yes"
    d = {'error': error,'supplier':supplier,'category':category}
    return render(request, 'edit_supplier.html',d)

def delete_supplier(request,suppid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    supplier = Supplier.objects.get(id=suppid)
    supplier.delete()
    return redirect('manage_supplier')


def inventory(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    product = Product.objects.all()
    d = {'product':product}
    return render(request, 'inventory.html', d)


def search(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    productcount = 0
    product=""
    sd=""
    click="no"
    error = ""
    if request.method == 'POST':
        try:

            pid = request.POST['pid']
            pqty = request.POST['pqty']
            ischeckout = "no"
            productid = Product.objects.get(id=pid)
            try:
                Cart.objects.create(productid=productid,productqty=pqty, ischeckout=ischeckout,cartdate=date.today(),
                                    billingid="")
                error = "no"
            except:
                error = "no"
        except:
            click = "yes"
            sd = request.POST['pname']
            product = Product.objects.get(productname=sd)
            productcount = Product.objects.filter(productname=sd).count()

    d = {'product':product,'productcount':productcount,'sd':sd,'click':click,'error':error}
    return render(request,'search.html',d)


def cart(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    cart = Cart.objects.filter(ischeckout="no")
    total = 0
    bn = ""
    for i in cart:
        total+= int(i.productqty) * int(i.productid.price)
    cartcount = Cart.objects.filter(ischeckout="no").count()
    error = ""
    if request.method=="POST":
        cn = request.POST['customername']
        mn = request.POST['mobilenumber']
        mp = request.POST['modepayment']
        bn = str(random.randint(10000000, 99999999))
        try:
            for c in cart:
                c.billingid = bn
                c.ischeckout = "yes"
                c.save()
            Customer.objects.create(billingid=bn,customername=cn,mobileno=mn,modeofpayment=mp,billingdate=date.today())
            error = "no"
        except:
            error = "yes"
    d = {'cart':cart,'cartcount':cartcount,'total':total,'error':error,'bn':bn}
    return render(request, 'cart.html', d)


def invoice_search(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    total = 0
    sd = ""
    cart = ""
    customer = ""
    cartcount = ""
    if request.method=="POST":
        sd = request.POST['searchdata']
        customer = Customer.objects.get(billingid=sd)
        cart = Cart.objects.filter(billingid=sd)
        cartcount = Cart.objects.filter(billingid=sd).count()
        for i in cart:
            total += int(i.productqty) * int(i.productid.price)
    d = {'cart':cart,'cartcount':cartcount,'total':total,'customer':customer,'sd':sd}
    return render(request, 'invoice_search.html', d)


def customer_detail(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    customer = Customer.objects.all()
    d = {'customer':customer}
    return render(request, 'customer_detail.html', d)


def stock_reportdetails(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'stock_reportdetails.html')



def stock_report(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    if request.method == "POST":
        fd = request.POST['fromdate']
        td = request.POST['todate']
        product = Product.objects.filter(Q(creationdate__gte=fd) & Q(creationdate__lte=td))
        productcount = Product.objects.filter(Q(creationdate__gte=fd) & Q(creationdate__lte=td)).count()
        d = {'product': product,'fd':fd,'td':td,'productcount':productcount}
        return render(request, 'stock_reportdetails.html', d)
    return render(request, 'stock_report.html')


def invoice(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    total = 0

    customer = Customer.objects.get(billingid=pid)
    cart = Cart.objects.filter(billingid=pid)
    cartcount = Cart.objects.filter(billingid=pid).count()
    for i in cart:
        total += int(i.productqty) * int(i.productid.price)
    d = {'cart':cart,'cartcount':cartcount,'total':total,'customer':customer,'pid':pid}
    return render(request, 'invoice.html', d)

def delete_cart(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    cart = Cart.objects.get(id=pid)
    cart.delete()
    return redirect('cart')
