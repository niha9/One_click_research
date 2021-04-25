from django.db import models

# Create your models here.
class Budget(models.Model):
    budget_id = models.ForeignKey(to='student.Std_details', on_delete=models.CASCADE)
    Nop = models.IntegerField()
    Travel_allow = models.IntegerField()
    No_of_visit = models.IntegerField()
    Rs_per_visit = models.IntegerField()
    Research_fellow_choices = (
        (1, 'In-house'),
        (2, 'New'),
        (3, 'DNB')
    )
    Research_fellow_id = models.IntegerField(choices = Research_fellow_choices)
    Remarks = models.TextField(blank=True)
    Miscellan = models.CharField(max_length=100)

class Consumable(models.Model):
    consum_id = models.ForeignKey(to = Budget, on_delete=models.CASCADE)
    consum_name = models.CharField(max_length=250)
    qty = models.IntegerField()
    Rs_per_unit = models.IntegerField()
    Catlog_no = models.IntegerField()
    Name_of_manufact = models.CharField(max_length=250)
    Total3 = models.IntegerField(default=9)


class Investigation2(models.Model):
    invest2_id = models.ForeignKey(to = Budget, on_delete=models.CASCADE)
    tests = models.CharField(max_length=250)
    exist_test_choice = (
        (1, 'yes'),
        (2, 'no')
    )
    exist_test_id = models.IntegerField(choices=exist_test_choice)
    No_of_pat = models.IntegerField()
    Followup = models.IntegerField()
    Tarrif = models.IntegerField()
    Total2 = models.IntegerField(default=19)


class Investigation1(models.Model):
    invest1_id = models.ForeignKey(to=Budget, on_delete=models.CASCADE)
    tests = models.CharField(max_length=250)
    exist_test_choice = (
        (1, 'yes'),
        (2, 'no')
    )
    exist_test_id = models.IntegerField(choices=exist_test_choice)
    No_of_pat = models.IntegerField()
    Tarrif = models.IntegerField()
    Total1 = models.IntegerField(default=10)


class Capital_equip(models.Model):
    Budget_id = models.ForeignKey(to=Budget, on_delete=models.CASCADE)
    Name = models.CharField(max_length=250)
    Price = models.IntegerField()


class Salaryy(models.Model):
    Salary_id = models.ForeignKey(to=Budget, on_delete=models.CASCADE)
    Name = models.CharField(max_length=250)
    Study = models.CharField(max_length=100)
    Salary = models.IntegerField()
    Total0 = models.IntegerField(default=10)

#term extension models

from django.db import models

# Create your models here.
class Extension(models.Model):
    Research_fellows = models.CharField(max_length=500)
    Extension_weeks = models.IntegerField()
    Project_completion = models.DateField()
    Reason_of_extension = models.TextField()
    Detail_remaining_work = models.TextField()
    Progress_report = models.FileField()

class Research_fellow(models.Model):
    Bud_utilize = models.IntegerField()
    Additional_bud = models.IntegerField()
    Justify = models.TextField()

class Material(models.Model):
    Bud_utilize = models.IntegerField()
    Additional_bud = models.IntegerField()
    Justify = models.TextField()

class Other(models.Model):
    Bud_utilize = models.IntegerField(blank=True)
    Additional_bud = models.IntegerField(blank=True)
    Justify = models.TextField(blank=True)


