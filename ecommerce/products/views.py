from django.views.generic import ListView, DetailView
from django.shortcuts import render

from carts.models import Cart 
from .models import Product

class ProductListView(ListView):
	queryset = Product.objects.all()
	template_name = "products/list.html"


def product_list_view(request):
	queryset = Product.objects.all()
	context = {
	      'object_list': queryset
	}
	return render(request, "products/list.html", context)
 


class ProductDetailView(DetailView):

	queryset = Product.objects.all()
	template_name = "products/detail.html"



	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context['cart'] = cart_obj
		return context

	def product_detail_view(request):
		queryset = Product.objects.all()
		context = {'object_list': queryset }
		return render(request, "products/detail.html", context)
    	
    	
    	
    	
    	















 


