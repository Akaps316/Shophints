from django.db import models

from ecommerce.utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

# Create your models here.
class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()
	price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
	image = models.ImageField(upload_to='products/', null=True, blank=True)
	#featured = models.BooleanField(default=False)
	slug = models.SlugField(blank=True, unique = True)
	timestamp = models.DateTimeField(auto_now_add=True)



	def get_absolute_url(self):
		return "/products/{slug}/".format(slug=self.slug)

	def __str__(self):
		return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)

