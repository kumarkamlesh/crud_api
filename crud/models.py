from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=222)
    last_name = models.CharField(max_length=222)
    email = models.CharField(max_length=222)
    address = models.CharField(max_length=222)

    def __str__(self):
        return self.first_name


class EmployeeEducation(models.Model):
    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE,
        related_name='employee', null=True, blank=True
    )
    high_school = models.CharField(max_length=222)
    intermediate = models.CharField(max_length=22)
    bachelor = models.CharField(max_length=22)
    master = models.CharField(max_length=22)

    def __str__(self):
        return self.employee.first_name

