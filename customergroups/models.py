from django.db import models

# Create your models here.
from place.models import Country, State, District, City

class CustomerGroup(models.Model): 
    group_name   = models.CharField(max_length = 30, unique=True)
    group_prefix = models.CharField(max_length = 30,unique=True, null=True, blank=True)
    country     = models.ForeignKey(Country, on_delete=models.CASCADE)
    state       = models.ForeignKey(State, on_delete=models.CASCADE)
    district    = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)
    city        = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    address     = models.CharField(max_length = 50, null=True, blank=True)
    # updated     = models.DateTimeField(auto_now=True)
    # timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.group_name)

    class Meta:
        verbose_name = 'Customer Group'
        verbose_name_plural = 'Customer Groups'
