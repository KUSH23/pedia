from django.db import models

from customergroups.models import CustomerGroup

class Jobs(models.Model):
    group      = models.ForeignKey(CustomerGroup, on_delete=models.CASCADE)
    job_title   = models.CharField(max_length = 20)
    print_l     = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    print_b     = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    paper_l     = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    paper_b     = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    sheet_count = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    gsm         = models.DecimalField(max_digits=19, decimal_places=2, null=True, blank=True)
    print_opt   = models.CharField(max_length = 20, null=True, blank=True)
    color_opt   = models.CharField(max_length = 20, null=True, blank=True)
    status      = models.CharField(max_length=30, null=True, blank=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.job_title)

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
