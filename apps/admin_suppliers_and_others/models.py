
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import User

import datetime
import random

def upload_file(instance,file_name):
    name=file_name.split('.')[0]
    ext=file_name.split('.')[-1]
    current_date=datetime.datetime.utcnow().strftime('%H%M%S%f')
    return f'pdf/{instance.company}/{name}-{current_date}.{ext}'



class Supplier_model(models.Model):

    company=models.CharField(max_length=50,verbose_name='Company Name')
    fullname=models.CharField(max_length=30,verbose_name='Person In Charge')
    mobile=models.CharField(max_length=15,verbose_name='Mobile')
    office=models.CharField(max_length=15,verbose_name='Office Phone',null=True,blank=True)
    email=models.EmailField(max_length=100,verbose_name='Email Address')
    email2=models.EmailField(max_length=100,verbose_name='Second Email',null=True,blank=True)
    no=models.CharField(max_length=10,verbose_name='Plate Number',null=True,blank=True)
    level=models.CharField(max_length=10,verbose_name='Floor Number',null=True,blank=True)
    street=models.CharField(max_length=100,verbose_name='Street',null=True,blank=True)
    city=models.CharField(max_length=30,verbose_name='City',null=True,blank=True)
    Country=models.CharField(max_length=30,verbose_name='Country',null=True,blank=True)
    CHOICES=[('Poultry','Poultry'),('Meat','Meat'),('Seafood','Seafood'),('Greens','Greens'),('Others','Others')]
    field=models.CharField(max_length=20,choices=CHOICES)
    others=models.CharField(max_length=20,verbose_name='Other Fields',null=True,blank=True)
    url=models.URLField(max_length=100,verbose_name='Website',null=True,blank=True,)
    active=models.BooleanField(default=False,verbose_name='Is Supplier Active?')
    register=models.DateTimeField(auto_now_add=True,verbose_name='Registered Date')
    info_update=models.DateTimeField(auto_now=True,verbose_name='Updated Date')
    user_register=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='User Registered Supplier')
    file_upload=models.FileField(upload_to=upload_file,default='no file available',verbose_name='Product pdf')
    comment=models.TextField(verbose_name='Admin Comments')

    def __str__(self):
        return f"{self.company} {self.field} {self.others}"
    
    class Meta:
        verbose_name='Vendor'
        verbose_name_plural='Vendors'
        db_table='Supplier Profile'

# ------------------------------------------------
class Client_Profile_model(models.Model):
    company=models.CharField(max_length=50,verbose_name='Company Name')
    fullname=models.CharField(max_length=30,verbose_name='Person In Charge')
    mobile=models.CharField(max_length=15,verbose_name='Mobile')
    office=models.CharField(max_length=15,verbose_name='Office Phone',null=True,blank=True)
    email=models.EmailField(max_length=100,verbose_name='Email Address')
    url=models.URLField(max_length=100,verbose_name='Website',null=True,blank=True,)
    active=models.BooleanField(default=False,verbose_name='Is Supplier Active?')
    register=models.DateTimeField(auto_now_add=True,verbose_name='Registered Date')
    info_update=models.DateTimeField(auto_now=True,verbose_name='Updated Date')
    user_register=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='User Registered Supplier')
    file_upload=models.FileField(upload_to=upload_file,default='no file available',verbose_name='Client documetn')
    comment=models.TextField(verbose_name='Admin Comments')

    def __str__(self):
        return f'{self.company}'
    class Meta:
        verbose_name='Client Profile'
        verbose_name_plural='Clients Profile'
        db_table='Client_Profile'
# ----------------------------------------


def emp_upload_file(instance,file_name):
    name=file_name.split('.')[0]
    ext=file_name.split('.')[-1]
    current_date=datetime.datetime.utcnow().strftime('%H%M%S%f')
    return f'emp_doc/{instance.lastname}/{name}-{current_date}.{ext}'

def emp_code():
    
    code=random.randint(10000000,99999999)
    return str(code)

class Employee_Model(models.Model):

    firstname=models.CharField(max_length=30,verbose_name='First Name')
    lastname=models.CharField(max_length=50,verbose_name='Last Name')
    phone=models.CharField(max_length=15,verbose_name='Phone',null=True)
    phone2=models.CharField(max_length=15,verbose_name='2nd Phone',null=True,blank=True)
    email=models.EmailField(max_length=100,verbose_name='Email',null=True)
    address=models.TextField(verbose_name='Address',null=True)
    employment_period=models.DateField()
    reference_info=models.CharField(max_length=200,null=True,blank=True)
    CHOICES=[('Entry Level','Entry Level'),('Supervisor','Supervisor'),('Assistant Manager','Assistant Manager'),('Manager','Manager'),('Director','Director')]
    level=models.CharField(choices=CHOICES,max_length=20)
    employed=models.BooleanField(default=False)
    register=models.DateTimeField(auto_now_add=True,verbose_name='Registered Date')
    info_update=models.DateTimeField(auto_now=True,verbose_name='Updated Date')
    user_register=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='User Registered Supplier')
    file_upload1=models.FileField(upload_to=emp_upload_file,default='no documents available',verbose_name='Employee Passport')
    file_upload2=models.FileField(upload_to=emp_upload_file,default='no documents available',verbose_name='Employee cv')
    file_upload3=models.FileField(upload_to=emp_upload_file,default='no documents available',verbose_name='Employee Image')
    file_upload4=models.FileField(upload_to=emp_upload_file,default='no documents available',verbose_name='Employee Contract')
    file_upload5=models.FileField(upload_to=emp_upload_file,default='no documents available',verbose_name='other documents')
    emp_code=models.CharField(max_length=30,verbose_name='Employee Code',default=emp_code)
    comment=models.TextField(verbose_name='Admin Comments',null=True,blank=True)

    def __str__(self):
        return f" Name: {self.firstname}  {self.lastname}, Emp Code: {self.emp_code}"
    
    class Meta:
        verbose_name='Employee'
        verbose_name_plural='Employees'
        db_table='Employee Profile'
# -----------------------------------------

class Employee_payroll_model(models.Model):

    position=models.CharField(max_length=30,verbose_name='Employee Position')
    basic=models.PositiveIntegerField(verbose_name='Basic Salary')
    up_sell=models.PositiveIntegerField(default=0,verbose_name='Product Up Sell')
    allowance=models.PositiveIntegerField(default=0,verbose_name='Allowance')
    child_no=models.PositiveIntegerField(default=0,verbose_name='No Of Child')
    child_allowance=models.PositiveIntegerField(default=0,verbose_name='Child Allowance')
    insurance_carried_company=models.PositiveIntegerField(verbose_name=' Insurance Carried Company')
    insurance_carried_employee=models.PositiveIntegerField(verbose_name=' Insurance Carried Employee')
    retirement=models.PositiveIntegerField(verbose_name='Retirement')
    unclaimed_vacation_days=models.PositiveIntegerField(default=0,verbose_name='Unclaimed Vacation Days')
    unclaimed_vacation=models.PositiveIntegerField(default=0,verbose_name='Unclaimed Vacation')
    deduction_tax=models.PositiveIntegerField(verbose_name='Deduction Tax',default=0)
    absense_days=models.PositiveIntegerField(default=0,verbose_name='Absense Days')
    deduction_absense=models.PositiveIntegerField(default=0,verbose_name='Deduction Absense')
    cash_in_hand=models.PositiveIntegerField(default=0,verbose_name='Cash In Hand')
    employee=models.ForeignKey(Employee_Model,on_delete=models.CASCADE,default='')
    month_end=models.DateField(verbose_name='Choose Month End',default=datetime.datetime.now())
    register=models.DateTimeField(auto_now_add=True,verbose_name='Registered Date')
    info_update=models.DateTimeField(auto_now=True,verbose_name='Updated Date')
    user_register=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='User Registered Supplier')
    net_salary=models.PositiveIntegerField(verbose_name='Net Salary',default=0)

    def __str__(self):
        return f'{self.employee}'
    class Meta:
        verbose_name='Employee Payroll'
        verbose_name_plural='Employees payroll'
        db_table='Employee Payroll'
    


    

