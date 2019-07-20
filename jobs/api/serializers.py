from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from accounts.api.serializers import UserPublicSerializer

from jobs.models import Jobs
from customergroups.api.serializers import CustomerReadGroupSerializer

class JobsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jobs
        fields=[
            'id',
            'group',
            'job_title',
            'print_l',
            'print_b',
            'paper_l',
            'paper_b',
            'sheet_count',
            'gsm',
            'print_opt',
            'color_opt',
            'status',
            'updated',
            'timestamp',
        ]

class JobsReadSerializer(serializers.ModelSerializer):

    group  = CustomerReadGroupSerializer(read_only=True)
    class Meta:
        model = Jobs
        fields=[
            'id',
            'group',
            'job_title',
            'print_l',
            'print_b',
            'paper_l',
            'paper_b',
            'sheet_count',
            'gsm',
            'print_opt',
            'color_opt',
            'status',
            'updated',
            'timestamp',
        ]