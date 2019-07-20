from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from customergroups.models import CustomerGroup

from place.api.serializers import CountrySerializer, StateSerializer, DistrictSerializer, CitySerializer

class CustomerGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerGroup
        fields=[
            'id',
            'group_name',
            'group_prefix',
            'country',
            'state',
            'district',
            'city',
            'address',
        ]


class CustomerReadGroupSerializer(serializers.ModelSerializer):
    country  = CountrySerializer(read_only=True)
    state  = StateSerializer(read_only=True)
    district  = DistrictSerializer(read_only=True)
    city  = CitySerializer(read_only=True)
    class Meta:
        model = CustomerGroup
        fields=[
            'id',
            'group_name',
            'group_prefix',
            'country',
            'state',
            'district',
            'city',
            'address',
        ]
