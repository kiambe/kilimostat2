from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 

length = 256
# Ignore this table was used for test


# Use these table was used for test
class Institution(models.Model):
  id = models.AutoField(primary_key=True)   
  name = models.CharField(max_length=256, null=True)   
  date_created = models.DateTimeField(auto_now_add=True)
  def __str__(self):
        return str(self.name)


class DataEntryOfficer(models.Model): 
  id = models.AutoField(primary_key=True)   
  nationalid = models.CharField(max_length=256, null=True)
  firstname = models.CharField(max_length=256, null=True)
  lastname = models.CharField(max_length=256, null=True)     
  telephone = models.IntegerField(null=True)
  email = models.EmailField(max_length=256, null=True)
  designation = models.CharField(max_length=256, null=True)
  institution = models.ForeignKey(
    Institution, 
            on_delete=models.PROTECT, 
            null=True, 
            blank=True
    )
  date_created = models.DateTimeField(auto_now_add=True)
  def __str__(self):
        return str(self.nationalid)



class County(models.Model):    
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=256, null=False, unique=True) 
  code = models.CharField(max_length=3, null=True) 
  def __str__(self):
        return str(self.name)
      

class SubCounty(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    county_id = models.ForeignKey('County', on_delete=models.CASCADE)
    name = models.CharField(max_length=length, blank=True, null=True,)
    lat = models.CharField(max_length=length, blank=True, null=True,)
    lng = models.CharField(max_length=length, blank=True, null=True,)
    category = models.CharField(max_length=length, blank=True, null=True,)
    code = models.CharField(max_length=length, blank=True, null=True,)
    loccode = models.CharField(max_length=length, blank=True, null=True,)

    def __str__(self):
        return '%s' % self.name


class Ward(models.Model):
    county_id = models.ForeignKey('County', on_delete=models.CASCADE)
    subcounty_id = models.ForeignKey('SubCounty', on_delete=models.CASCADE)
    name = models.CharField(max_length=length, blank=True, null=True,)
    lat = models.CharField(max_length=length, blank=True, null=True,)
    lng = models.CharField(max_length=length, blank=True, null=True,)
    category = models.CharField(max_length=length, blank=True, null=True,)
    code = models.CharField(max_length=length, blank=True, null=True,)
    loccode = models.CharField(max_length=length, blank=True, null=True,)

    def __str__(self):
        return '%s' % self.name



class SubSector(models.Model):    
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=256, null=True,
    blank=True) 
  def __str__(self):
        return str(self.name)

class Domain(models.Model):    
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=256, null=True,
    blank=True) 
  def __str__(self):
        return str(self.name)

class DomainElement(models.Model):    
  id = models.AutoField(primary_key=True)  
  domainelement = models.CharField(max_length=256, null=True,
    blank=True) 
  def __str__(self):
        return str(self.domainelement)



class ElementItem(models.Model):    
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=256, null=True,
    blank=True) 
  def __str__(self):
        return str(self.name)

class ItemCategory(models.Model):    
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=256, null=True,
    blank=True) 
  def __str__(self):
        return str(self.name)

class ItemSpecify(models.Model):    
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=256, null=True) 
  itemCategory = models.ForeignKey(
    ItemCategory, 
    on_delete=models.PROTECT,null=True,
    blank=True
    )
  def __str__(self):
        return str(self.name)

class UoM(models.Model):    
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=256, null=True,
    blank=True) 
  def __str__(self):
        return str(self.name)


class Flags(models.Model):    
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=256, null=True,
    blank=True) 
  def __str__(self):
        return str(self.name)




class KilimoData(models.Model):
  id = models.AutoField(primary_key=True)

  county = models.ForeignKey(
    County, 
    on_delete=models.PROTECT, null=True,
    blank=True
    )

  subsector = models.ForeignKey(
    SubSector, 
    on_delete=models.PROTECT, null=True,
    blank=True
    )

  domain = models.ForeignKey(
    Domain, 
    on_delete=models.PROTECT,null=True,
    blank=True
    )

  domainelement = models.ForeignKey(
    DomainElement, 
    on_delete=models.PROTECT,null=True,
    blank=True
    )



  elementitem = models.ForeignKey(
    ElementItem, 
    on_delete=models.PROTECT, 
    null=True,
    blank=True
    )

  itemspecify = models.ForeignKey(
    ItemSpecify, 
    on_delete=models.PROTECT,  
    null=True,
    blank=True
    )

  refperiod = models.DateField(null=True,
    blank=True)
  value = models.FloatField()
  uom = models.ForeignKey(
    UoM, 
    on_delete=models.PROTECT,  
    null=True,
    blank=True
    )
  flagdescription  = models.CharField(max_length=256, null=True) 
  flagdescription = models.ForeignKey(
    Flags, 
    on_delete=models.PROTECT,  
    null=True,
    blank=True
    )
  datasource = models.CharField(max_length=256, null=True,
    blank=True) 
  doneby = models.CharField(max_length=256, null=True,
    blank=True) 
  validated = models.BooleanField(null=True,
    blank=True)
  publish = models.BooleanField(null=True,
    blank=True)
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)