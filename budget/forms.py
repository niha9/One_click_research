from django import forms
from .models import *
from .models import Extension, Research_fellow, Material, Other

class BudgetForm(forms.ModelForm):

    class Meta:
        model = Budget
        fields = '__all__'
        labels = {
            'Nop': "No of Patients Sanctioned for the study",
            "Travel_allow": "Patient Travel Allowance/Compensatory allowance",
            "No_of_visit": "Total no of visits per patient",
            "Rs_per_visit": "Rs per visit patient",
            " Research_fellow_id": "Research Fellow/Clinical Asst",
            "Miscellan":"Miscellaneous"
        }


class CapitalForm(forms.ModelForm):

    class Meta:
        model = Capital_equip
        fields = ("Name", "Price")


class Invest1(forms.ModelForm):

    class Meta:
        model = Investigation1
        fields = ("tests", "exist_test_id", "No_of_pat", "Tarrif")
        labels = {
            "tests" : "Name of Test",
            "exist_test_id" : "Existing Test",
            "No_of_pat": "No of Patients",
        }


class Salary(forms.ModelForm):

    class Meta:
        model = Salaryy
        fields = ("Name", "Study", "Salary")


class Invest2(forms.ModelForm):
    class Meta:
        model = Investigation2
        fields = ("tests", "exist_test_id", "No_of_pat", "Followup", "Tarrif")
        labels = {
            "tests": "Name of Test",
            "exist_test_id": "Existing Test",
            "No_of_pat": "No of Patients",
            "Followup" : "Follow-up"
        }


class Consumable(forms.ModelForm):
    class Meta:
        model = Consumable
        fields = ("consum_name", "qty", "Rs_per_unit", "Catlog_no", "Name_of_manufact")
        labels ={
            "consum_name" : "Consumables Name",
            "qty" : "Quantity Required",
            "Rs_per_unit" : "Rate/Unit",
            "Catlog_no" : "Catalog Number",
            "Name_of_manufact" : "Name of Manufacturer / Supplier"
        }

#term extension

from bootstrap_datepicker_plus import DatePickerInput

class ExtensionForm(forms.ModelForm):
    class Meta:
        model = Extension
        fields = ['Research_fellows', 'Extension_weeks', 'Project_completion', 'Reason_of_extension', 'Detail_remaining_work', 'Progress_report']
        widgets = {
            'Project_completion' :DatePickerInput()
        }
        labels = {'Research_fellows':'Research Fellows(All fellows presently working and who had worked on the project)',
                  'Extension_weeks':'Period of extension requested (in weeks)',
                  'Project_completion':'Projected Date of completion',
                  'Reason_of_extension':'Reasons/justification for extension of the study - (in details)',
                  'Detail_remaining_work':'Provide timed schedule to complete the remaining work',
                  'Progress_report':'Submit progress report of Research activity'}

class ResearchFellowForm(forms.ModelForm):
    class Meta:
        model = Research_fellow
        fields = ['Bud_utilize', 'Additional_bud', 'Justify']
        labels ={'Bud_utilize':'Budget Utilized',
                 'Additional_bud':'Additional Budget requested',
                 'Justify':'Justification for Additional Budget requested'
                 }

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['Bud_utilize', 'Additional_bud', 'Justify']
        labels = {'Bud_utilize': 'Budget Utilized',
                  'Additional_bud': 'Additional Budget requested',
                  'Justify': 'Justification for Additional Budget requested'
                  }

class OtherForm(forms.ModelForm):
    class Meta:
        model = Other
        fields = ['Bud_utilize', 'Additional_bud', 'Justify']
        labels = {'Bud_utilize': 'Budget Utilized',
                  'Additional_bud': 'Additional Budget requested',
                  'Justify': 'Justification for Additional Budget requested'
                  }