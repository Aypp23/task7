from .hospital.models import Product

#insert a new record into the Product model
p = Product(name='Apple', price=30.0)
p.save()

#get all the records in the Product table
all_products = Product.objects.all()

#filter products by their name
apple = Product.objects.filter(name='Apple')

#Get a single record from the product table
one_record = Product.objects.get(pk=1)

#change a product price
apple = Product.objects.get(name='Apple')
apple.price = 50.0
apple.save()
