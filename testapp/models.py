from django.db import models

class product(models.Model):
    pName=models.CharField(max_length=250, blank=False,null=False)
    pDescription=models.TextField(blank=True,null=True)
    pPrice=models.DecimalField(blank=False,null=False, max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.pName}'
