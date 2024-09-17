from django.db import models
from django.db.models import Q


class Breed(models.Model):
    id_breed = models.AutoField(primary_key=True)
    breed_name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "tbl_breeds"
        verbose_name = "Breed"
        verbose_name_plural = "Breeds"

    def __str__(self):
        return self.breed_name


class Customer(models.Model):
    id_customer = models.AutoField(primary_key=True)
    identification = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True, default=None  )
    phone_number = models.CharField(max_length=15, unique=True)

    class Meta:
        db_table = "tbl_customers"
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'], name='unique_customer_name')
        ]
        indexes = [
            models.Index(fields=['identification']),
        ]

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Feeding(models.Model):
    id_feeding = models.AutoField(primary_key=True)
    description = models.CharField(max_length=255, unique=True)
    dosage = models.FloatField()

    class Meta:
        db_table = 'tbl_feeding'
        verbose_name = "Feeding"
        constraints = [
            models.CheckConstraint(condition=Q(dosage__gt=0), name='dosage_gt_zero')
        ]

    def __str__(self):
        return self.description


class Porcine(models.Model):
    id_porcine = models.AutoField(primary_key=True)
    identification = models.CharField(max_length=100, unique=True)
    breed = models.ForeignKey(Breed, null=True, blank=True, on_delete=models.SET_NULL)
    age = models.IntegerField()
    weight = models.FloatField()
    feeding = models.ForeignKey(Feeding, null=True, blank=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        db_table = "tbl_porcines"
        verbose_name = "Porcine"
        verbose_name_plural = "Porcines"
        constraints = [
            models.CheckConstraint(check=Q(age__gt=0), name='age_gt_zero'),
            models.CheckConstraint(check=Q(weight__gt=0), name='weight_gt_zero'),
        ]
        indexes = [
            models.Index(fields=['identification']),
        ]

    def __str__(self):
        return f'{self.identification} - {self.customer}'
