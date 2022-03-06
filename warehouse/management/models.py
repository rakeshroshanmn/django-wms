from django.db import models

# Create your models here.

class Company(models.Model):
    company_name = models.CharField('Company Name', max_length = 100 )
    company_address = models.CharField('Address', max_length = 100 )
    company_mobile_number = models.CharField('Number', max_length = 12)
    company_email = models.EmailField('Email')


    def __str__(self):
        return self.company_name


class Asrusagereport(models.Model):
    from_date = models.DateTimeField('From Date',  blank = False )
    to_date = models.DateTimeField('To Date', blank = False )
    report_type =(
        
        ('Summary', 'Summary'),
        (' Detail', ' Detail'),
        
        )

    type_of_report = models.CharField(max_length = 30, choices = report_type, default='Select')

    def __str__(self):
        return self.report_type


class Shifts(models.Model):
    no_of_shifts = (

        ('2','2'),
        ('3','3'),

    )

    shift = models.CharField(max_length=30,choices=no_of_shifts, default='Select')
    
    shift_one_start_time = (

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
    
    one_start_time = models.CharField(max_length=30,choices=shift_one_start_time, default='Select')

    shift_two_start_time = (

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
    
    two_start_time = models.CharField(max_length=30,choices=shift_two_start_time, default='Select')

    shift_three_start_time = (

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
    
    three_start_time = models.CharField(max_length=30,choices=shift_three_start_time , default='Select')

    shift_four_start_time = (

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
    
    four_start_time = models.CharField(max_length=30,choices=shift_four_start_time, default='Select')


    def __str__(self):
        return self.shift


class Employee(models.Model):
    user_type =(
        
        ('Operator', 'Operator'), 
        ('Supervisor', 'Supervisor'),
        (' Mechanical', ' Mechanical'),
        (' Electrical', ' Electrical'),
        (' Production', ' Production'),
        (' Management', ' Management'),

        )
    user = models.CharField(max_length=30,choices=user_type, default='Select')
    user_code = models.CharField('User Code', max_length = 100 )
    user_name = models.CharField('User Name', max_length = 100 )
    user_email = models.EmailField('Email')
    user_mobile_number = models.CharField('Mobile Number', max_length = 12 )
    user_is_login = models.BooleanField(default = False)
    user_ip_address = models.CharField('Mobile Number', max_length = 100, blank = True )


    def __str__(self):
        return self.user_name


class Toleranceweight(models.Model):
    plus = models.CharField('Tolerance Weight+', max_length = 100 )
    minus = models.CharField('Tolerance Weight-', max_length = 100 )

    def __str__(self):
        return self.plus


class Pallettwo(models.Model):
    pallet_id = models.CharField('Pallet Id', max_length = 100 )
    pallet_color = models.CharField('Pallet Color', max_length = 100 )
    pallet_weight = models.CharField('Pallet Weight', max_length = 100 )
    Toleranceweight = models.ForeignKey(Toleranceweight, on_delete = models.CASCADE)
    pallet_suplier = models.CharField('Pallet Suplier', max_length = 100 )

    def __str__(self):
        return self.pallet_id


class Qstatus(models.Model):
    q_status_code = models.CharField('Q Status Code', max_length = 100 )
    q_status_name = models.CharField('Q Status Name', max_length = 100 )

    def __str__(self):
        return self.q_status_name


class Materialinward(models.Model):
    grn = models.CharField('GRN', max_length = 100 )
    order_number = models.CharField('ORDERNO', max_length = 100 )
    order_ref_number = models.CharField('ORDERREFNO', max_length = 100 )
    fabric_name = models.CharField('FABRICNAME', max_length = 100 )
    color = models.CharField('Color', max_length = 100 )
    fabric_type = models.CharField('FABRICTYPE', max_length = 100 )
    dia = models.CharField('DIA', max_length = 100 )
    gsm = models.CharField('GSM', max_length = 100 )
    batch_number = models.CharField('BATCHNO', max_length = 100 )
    roll_snumber = models.CharField('ROLLSNO', max_length = 100 )
    total_weight = models.CharField('TOTALWEIGHT', max_length = 100 )
    supplier = models.CharField('SUPPLIER', max_length = 100 )
    pallet_id =(
        
        ('6730', '6730'),
        (' 6434 ', ' 6434 '),
        ('6030 ', '6030 '),
        ('6750 ', '6750 '),
        ('6477', '6477'),
        
        )

    id_of_pallet = models.CharField(max_length=30,choices=pallet_id, default='Select')

    def __str__(self):
        return self.supplier


class Materialoutward(models.Model):
    Materialinward = models.ForeignKey(Materialinward, on_delete = models.CASCADE)
    pallet_id =(
        
        ('6002', '6002'),
        ('6003', ' 6003 '),
        ('6004 ', '6004 '),
        ('6005 ', '6005 '),
        ('6006', '6006'),
        
        )

    id_of_pallet = models.CharField(max_length=30,choices=pallet_id, default='Select')


    def __str__(self):
        return self.pallet_id


class Materialreload(models.Model):
    Materialinward = models.ForeignKey(Materialinward, on_delete = models.CASCADE)

    def __str__(self):
        return self.Materialinward


class Adjustmentreprocess(models.Model):
    Materialinward = models.ForeignKey(Materialinward, on_delete = models.CASCADE)

    def __str__(self):
        return self.Materialinward


class Changepassword(models.Model):
    old_password = models.CharField('Old Password', max_length = 100)
    new_password = models.CharField('New Password', max_length = 100)
    retype_password = models.CharField('Retype Password', max_length = 100)

    def __str__(self):
        return self.new_password

