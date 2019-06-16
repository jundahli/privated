from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,permission_required
from django.views.decorators.cache import cache_page
from django.contrib import messages
from django.template import RequestContext
from index.models import *
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

@login_required(login_url='/user/login.html')
@permission_required(perm='index.visit_Product',login_url='/user/login.html')
def index(request):
	product  = request.GET.get('product','')
	price = request.GET.get('price','')
	if product:
		product_list = request.session.get('product_info',[])
		if not product in product_list:
			product_list.append({'price':price,'product':product})
		request.session['product_info'] = product_list
		return redirect('/')
	return render(request,'index.html',locals())

@cache_page(timeout=10,cache='MyDjango',key_prefix='MyDjangoView')
@login_required(login_url='/user/login.html')
def ShoppingCarView(request):
	product_list = request.session.get('product_info',[])
	del_product = request.GET.get('product','')
	if del_product:
		for i in product_list:
			if i['product'] == del_product:
				product_list.remove(i)
		request.session['product_info'] = product_list
		return redirect('/ShoppingCar.html')
	return render(request,'ShoppingCar.html',locals())

def messageView(request):
	messages.info(request,'信息提示')
	messages.success(request,'信息正确')
	messages.warning(request,'信息警告')
	messages.error(request,'信息错误')
	messages.add_message(request,messages.INFO,'信息提示')
	return render(request,'message.html',locals(),RequestContext(request))

def paginationView(request,page):
	Product_list = Product.objects.all()
	paginator = Paginator(Product_list,3)

	try:
		pageInfo = paginator.page(page)
	except PageNotAnInteger:
		pageInfo = paginator.page(1)
	except EmptyPage:
		pageInfo = paginator.page(paginator.num_pages)
	return render(request,'pagination.html',locals())