from rest_framework import serializers

from crud.models import *


class EmployeeEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeEducation
        fields = (
            'id',
            'employee',
            'high_school',
            'intermediate',
            'bachelor',
            'master',
        )


class EmployeeSerializer(serializers.ModelSerializer):
    employee = EmployeeEducationSerializer(many=True)

    class Meta:
        model = Employee
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'address',
            'employee',
        )

    def create(self, validated_data):
        employee_data = validated_data.pop('employee')
        employee = Employee.objects.create(**validated_data)
        for emp in employee_data:
            EmployeeEducation.objects.create(employee=employee, **emp)
        return employee

    def update(self, instance, validated_data):
        employee_data = validated_data.pop('employee')
        employee = instance.employee.all()
        employee = list(employee)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.address = validated_data.get('address', instance.address)

        instance.save()

        for emp in employee_data:
            employee = employee.pop(0)
            employee.high_school = emp.get('high_school', employee.high_school)
            employee.intermediate = emp.get('intermediate', employee.intermediate)
            employee.bachelor = emp.get('bachelor', employee.bachelor)
            employee.master = emp.get('master', employee.master)

            employee.save()
        return instance
