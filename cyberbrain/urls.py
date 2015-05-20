import datetime
from random import randint
from django.conf.urls import include, url
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin
from leaves.models import Leaf
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response


# Serializers define the API representation.
class LeafSerializer(serializers.HyperlinkedModelSerializer):

        @csrf_exempt
        def create(self, validated_data):
                leaf, created = Leaf.objects.update_or_create(**validated_data)
                return leaf

        class Meta:
                model = Leaf
                fields = ('mac_address', 'last_seen_date')

# ViewSets define the view behavior.
class LeafViewSet(viewsets.ModelViewSet):
	#report random # of leaves for testing
	#num = slice(1, randint(2,10))
	#queryset = Leaf.objects.all().order_by('?')[num]
	#queryset = Leaf.objects.all()[num]
        queryset = Leaf.objects.all()
        serializer_class = LeafSerializer

        @csrf_exempt
        def list(self, request):
                queryset = Leaf.objects.filter(last_seen_date__gte=(datetime.datetime.now() - datetime.timedelta(minutes=3)))
                serializer = LeafSerializer(queryset, many=True)
                return Response(serializer.data)

                
        @csrf_exempt
        def retrieve(self, request):
                queryset = Leaf.objects.filter(last_seen_date__gte=(datetime.datetime.now() - datetime.timedelta(minutes=3)))
                serializer = LeafSerializer(queryset, many=True)
                return Response(serializer.data)




# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r't4tree/leaves', LeafViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^tree/', include('tree.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),


]
