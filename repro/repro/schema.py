from graphene_django import DjangoObjectType
import graphene
from .models import Test

class Test(DjangoObjectType):
    class Meta:
        model = Test

class Query(graphene.ObjectType):
    tests = graphene.List(Test)

    def resolve_tests(self, info):
        return Test.objects.all()
    
schema = graphene.Schema(query=Query)
