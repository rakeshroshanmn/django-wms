from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField('Company Name', max_length = 100 )
    address = models.CharField('Address', max_length = 100 )
    mobile_no = models.CharField('Number', max_length = 12)
    email = models.EmailField('Email')


class Asrusagereport(models.Model):
    fromdate = models.DateTimeField('From Date',  blank = False )
    todate = models.DateTimeField('To Date', blank = False )
    report_type =(
        
        ('Summary', 'Summary'),
        (' Detail', ' Detail'),
        
        )

    typeofreport = models.CharField(max_length = 30, choices = report_type, default='Select')


class Shifts(models.Model):
    no_of_shifts = (

        ('2','2'),
        ('3','3'),

    )

    no_of_shifts = models.CharField(max_length=30,choices=no_of_shifts, default='Select')
    
    shift_1_hour = (

        ('00','00'),
        ('01','01'),
        ('02','02'),
        ('03','03'),
        ('04','04'),
        ('05','05'),
        ('06','06'),
        ('07','07'),
        ('08','08'),
        ('09','09'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
        ('13','13'),

    )
    
    shift_1_hour = models.CharField(max_length=30,choices=shift_1_hour, default='Select')

    shift_1_min = (

        ('00','00'),
        ('01','01'),
        ('02','02'),
        ('03','03'),
        ('04','04'),
        ('05','05'),
        ('06','06'),
        ('07','07'),
        ('08','08'),
        ('09','09'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
        ('13','13'),

    )
    
    shift_1_min = models.CharField(max_length=30,choices=shift_1_min, default='Select')

    shift_2_hour = (

        ('00','00'),
        ('01','01'),
        ('02','02'),
        ('03','03'),
        ('04','04'),
        ('05','05'),
        ('06','06'),
        ('07','07'),
        ('08','08'),
        ('09','09'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
        ('13','13'),

    )
    
    shift_2_hour = models.CharField(max_length=30,choices=shift_2_hour , default='Select')

    shift_2_min = (

        ('00','00'),
        ('01','01'),
        ('02','02'),
        ('03','03'),
        ('04','04'),
        ('05','05'),
        ('06','06'),
        ('07','07'),
        ('08','08'),
        ('09','09'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
        ('13','13'),

    )
    
    shift_2_min = models.CharField(max_length=30,choices=shift_2_min, default='Select')

    
    shift_3_hour = (

        ('00','00'),
        ('01','01'),
        ('02','02'),
        ('03','03'),
        ('04','04'),
        ('05','05'),
        ('06','06'),
        ('07','07'),
        ('08','08'),
        ('09','09'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
        ('13','13'),

    )
    
    shift_3_hour = models.CharField(max_length=30,choices=shift_3_hour, default='Select')

    
    shift_3_min = (

        ('00','00'),
        ('01','01'),
        ('02','02'),
        ('03','03'),
        ('04','04'),
        ('05','05'),
        ('06','06'),
        ('07','07'),
        ('08','08'),
        ('09','09'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
        ('13','13'),

    )
    
    shift_3_min = models.CharField(max_length=30,choices=shift_3_min, default='Select')


class Employee(models.Model):
    employee_type =(
        
        ('Operator', 'Operator'), 
        ('Supervisor', 'Supervisor'),
        (' Mechanical', ' Mechanical'),
        (' Electrical', ' Electrical'),
        (' Production', ' Production'),
        (' Management', ' Management'),

        )
    user = models.CharField(max_length=30,choices=employee_type, default='Select')

    employee_code = models.CharField('User Code', max_length = 100 )
    employee_name = models.CharField('User Name', max_length = 100 )
    email = models.EmailField('Email')
    mobile_no = models.CharField('Mobile Number', max_length = 12 )
    is_login = models.BooleanField(default = False)
    ip_address = models.CharField('Mobile Number', max_length = 100, blank = True )


class Toleranceweight(models.Model):
    main_weight_tolerance_plus = models.CharField('Tolerance Weight+', max_length = 100 )
    main_weight_tolerance_minus = models.CharField('Tolerance Weight-', max_length = 100 )


class Pallet(models.Model):
    palletid = models.CharField('Pallet Id', max_length = 100 )
    palletcolor = models.CharField('Pallet Color', max_length = 100 )
    palletweight = models.CharField('Pallet Weight', max_length = 100 )
    Toleranceweight = models.ForeignKey(Toleranceweight, on_delete = models.CASCADE)
    palletsuplier = models.CharField('Pallet Suplier', max_length = 100 )


class Qstatus(models.Model):
    q_status_code = models.CharField('Q Status Code', max_length = 100 )
    q_status_name = models.CharField('Q Status Name', max_length = 100 )


class Materialinward(models.Model):
    grn = models.CharField('GRN', max_length = 100 )
    ordernumber = models.CharField('ORDERNO', max_length = 100 )
    orderrefnumber = models.CharField('ORDERREFNO', max_length = 100 )
    fabricname = models.CharField('FABRICNAME', max_length = 100 )
    color = models.CharField('Color', max_length = 100 )
    fabrictype = models.CharField('FABRICTYPE', max_length = 100 )
    dia = models.CharField('DIA', max_length = 100 )
    gsm = models.CharField('GSM', max_length = 100 )
    batchnumber = models.CharField('BATCHNO', max_length = 100 )
    rollsnumber = models.CharField('ROLLSNO', max_length = 100 )
    totalweight = models.CharField('TOTALWEIGHT', max_length = 100 )
    supplier = models.CharField('SUPPLIER', max_length = 100 )
    palletid =(
        
        ('6730', '6730'),
        (' 6434 ', ' 6434 '),
        ('6030 ', '6030 '),
        ('6750 ', '6750 '),
        ('6477', '6477'),
        
        )

    idofpallet = models.CharField(max_length=30,choices=palletid, default='Select')


class Materialoutward(models.Model):
    Materialinward = models.ForeignKey(Materialinward, on_delete = models.CASCADE)


class Materialreload(models.Model):
    Materialinward = models.ForeignKey(Materialinward, on_delete = models.CASCADE)


class Adjustmentreprocess(models.Model):
    Materialinward = models.ForeignKey(Materialinward, on_delete = models.CASCADE)


class Changepassword(models.Model):
    oldpassword = models.CharField('Old Password', max_length = 100)
    newpassword = models.CharField('New Password', max_length = 100)
    retypepassword = models.CharField('Retype Password', max_length = 100)
