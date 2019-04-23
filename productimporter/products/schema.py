import graphene
from graphene_django import DjangoObjectType
from .models import Products
from django.db.models import Q

class ProductsType(DjangoObjectType):
    class Meta:
        model = Products

# Query to get data from the server, query with products name
class Query(graphene.ObjectType):
    products = graphene.List(ProductsType,
                           search=graphene.String(),
                           first=graphene.Int(),
                           skip=graphene.Int(),
                           last=graphene.Int(),
                           find=graphene.String()
                           )

    def resolve_products(self, info, search=None, first=None, skip=None, last=None,find=None, **kwargs):
        qs = Products.objects.all()

        # Search records which partially matches name and url
        if search:
            filter = (
                Q(name__icontains=search) |
                Q(sku__icontains=search)  |
                Q(description__icontains=search)|
                Q(flag__icontains=search)
            )
            qs = qs.filter(filter)
        #filter the records            
        if find:
            query=eval(find)
            name=query.get('name','')
            sku=query.get('sku','')
            description=query.get('description','')
            qs=Products.objects.filter(name__iexact=name, sku__icontains= sku,description__icontains= description)
        # Skip n records
        if skip:
            qs = qs[skip::]

        # Get the first n records
        if first:
            qs = qs[:first]

        # Get the last n records
        if last:
            last_n = qs.order_by('-id')[:last]
            qs = reversed(last_n)
        
        return qs


# Create new Event
class ProductMutation(graphene.Mutation):
    id = graphene.Int()
    name = graphene.String()
    sku = graphene.String()
    description = graphene.String()
    flag = graphene.String()

    class Arguments:
        name = graphene.String()
        sku = graphene.String()
        description = graphene.String()
        flag = graphene.String()


    def mutate(self, info, name, sku, description, flag):
        product = Products(name=name, sku=sku, description = description, flag=flag)
        product.save()

        return ProductMutation(
            id=product.id,
            name=product.name,
            sku = product.sku,
            description = product.description,
            flag = product.flag
        )


# Create event to the server
class Mutation(graphene.ObjectType):
    create_product = ProductMutation.Field()