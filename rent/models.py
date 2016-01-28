# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class client(models.Model): #客户信息表
    customer_id = models.PositiveIntegerField()
    customer_name = models.CharField(max_length=100)
    link_man = models.CharField(max_length=40)
    telephone = models.CharField(max_length=11)
    mobilephone = models.CharField(max_length=11)
    foregift = models.FloatField() #押金
    reg_date = models.DateTimeField() #开户日期

    def __unicode__(self):
	return self.customer_name

class materInformation(models.Model): #建筑材料信息表
    equipment_id = models.PositiveIntegerField()
    equipment_name = models.CharField(max_length=100)
    specification = models.CharField(max_length=50) #设备规格
    equipment_type = models.CharField(max_length=50) #设备型号
    unit = models.CharField(max_length=50) #计量单位
    amount = models.PositiveIntegerField() #数量
    left_amount = models.PositiveIntegerField() #剩余数量

    def __unicode__(self):
	return self.equipment_name

class priceInformation(models.Model): #价格信息表
    price_id = models.PositiveIntegerField()
    valid_date = models.DateTimeField() #生效日期
    site_name = models.CharField(max_length=100) #工地名称
    sequence_number = models.CharField(max_length=50) #序号
    equipment_name = models.CharField(max_length=100) #设备名称
    unit = models.CharField(max_length=50)
    unitprice = models.FloatField()

class systemClientInoformation(models.Model): #系统用户信息表
    user_id = models.PositiveIntegerField()
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    stock = models.BooleanField(default = False) #库存管理
    data_input = models.BooleanField(default = False) #数据录入
    data_search = models.BooleanField(default = False) #数据查询
    account_settlement = models.BooleanField(default = False) #财务结算
    print_settlement = models.BooleanField(default = False) #打印结算
    print_checkup = models.BooleanField(default = False) #打印对账单
    finance = models.BooleanField(default = False) #财务管理
    data_erase = models.BooleanField(default=False) #数据清除
    user_admin = models.BooleanField(default=False) #用户管理

    def __unicode__(self):
	return user_name

class materRentInformation(models.Model): #料单信息表
    bill_id = models.PositiveIntegerField()
    bill_sequence_number = models.CharField(max_length=50) #序号
    lease_out_date = models.DateTimeField() #出租日期
    add_information = models.CharField(max_length=50) #附加描述
    lease_out_amount = models.PositiveIntegerField() #租赁数量
    price_id = models.PositiveIntegerField() #价格id
    customer_id = models.PositiveIntegerField() #客户id
    equipment_id = models.PositiveIntegerField() 
    money = models.FloatField()
    is_settled = models.BooleanField(default=False) #是否结算过
    settled_date = models.DateTimeField() #结算时间

class settleInformation(models.Model): #结算信息
    settle_record_id = models.PositiveIntegerField() #记录id
    customer_id = models.PositiveIntegerField() #客户id
    last_settle_date = models.DateTimeField() #上次结算日期
    money = models.FloatField()


  
