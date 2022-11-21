from rest_framework import serializers
from kilimodata.models import *

class SectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubSector 
        fields = "__all__"

class DomainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Domain 
        fields = "__all__"

class DomainElementSerializer(serializers.ModelSerializer):

    class Meta:
        model = DomainElement 
        fields = "__all__"

class CountySerializer(serializers.ModelSerializer):

    class Meta:
        model = County 
        fields = "__all__"

class ElementItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ElementItem 
        fields = "__all__"


class ItemCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemCategory 
        fields = "__all__"


class ItemSpecifySerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemSpecify 
        fields = "__all__"

class UoMSerializer(serializers.ModelSerializer):

    class Meta:
        model = UoM 
        fields = "__all__"


class FlagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flags 
        fields = "__all__"


class DataSerializer(serializers.ModelSerializer):
    #sector=SectorSerializer(read_only=True, many=True)
    #subdomain=SubdomainSerializer(read_only=True, many=True)
    #county=CountySerializer(read_only=True, many=True)
    #elements=ElementsSerializer(read_only=True, many=True)
    #itemspecify=ItemSpecifySerializer(read_only=True, many=True)
    #unit=UnitSerializer(read_only=True, many=True)

    class Meta:
        model = KilimoData 
        fields = "__all__"
        depth = 1