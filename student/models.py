from django.db import models

# Create your models here.
class Std_details(models.Model):
    student_id = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    st_designation = models.CharField(max_length=100)
    study_purpose = (
        ('D', 'DNB'), ('M', 'MSc'), ('P', 'PhD'), ('O', 'Others')
    )

    # 3
    st_any_pub = models.TextField()
    # 2
    st_study_purpose = models.CharField(max_length=100, choices=study_purpose)

    st_study_other = models.CharField(max_length=100)
  # todo  st_collab_id = models.ForeignKey('project.collaborations', on_delete=models.CASCADE)

    status_choice = (
        (1, 'Not applied'),
        (2, 'applied'),
        (3, 'approved'),
        (4, 'rejected')
    )
    status_choice_id = models.IntegerField(choices=status_choice, default=1)
    project_status = (
        # (0, 'Not Filled'),
        # ############################
        # (1, 'Gone for Co-Guide Approval'), #yellow circle
        # (2, 'Co-guide modified'),
        # (3, ' Gone for Guide-Approval'),
        # (4, 'Guide modified'),
        # (5, 'Secretary Approval'), #guide approved
        # #############################
        # (6, 'Gone for director approval'),  #sec done
        # (7, 'director modified'),   #go to student
        # (8, 'Director approval'),   #dir gone
        # (9, 'IRB modification'),    #modified by irb -->student
        #
        # (10, 'IRB approval'),        #irb
        # #############################
        # (11, 'Final review pending'),
        # (12, 'Final review done'),

        (0, 'Not Filled'),
        (1, 'Guide Approval Pending'),  #form filled -> Routed to 0 for loop if guide rejects
        (2, 'Sectretary Approval Pending '),    #guide approved
        (3, 'Director Approval Pending'),    #Secretary approved -> Routed to 0 for loop if director rejects
        (4, 'IRB Review Pending'),  #Director Approved
        (5, 'Final Review Pending'),    #IRB approved
        (6, 'Student queryset'),    #IRB Modification
        (7, 'Guide Forward for IRB'),   #guide forward after IRB Modications
        (8, 'Secretary Forward for IRB'),   #sec forward for IRB Modifications -> routed to 3 for loop with director
        (9, 'Final Review Complete'),   #All steps done

    )

    st_project_status = models.IntegerField(choices=project_status, default=0)
    is_initreview_done = models.BooleanField(default=False)
    is_interreview_done = models.BooleanField(default=False)
    is_finalreview_done = models.BooleanField(default=False)

class Document(models.Model):
    student_id = models.ForeignKey(Std_details, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    doc = models.FileField()


class hindu(models.Model):
    Title = models.CharField(max_length=250)
    Place_of_study = models.TextField()
    Prin_invest = models.CharField(max_length=250)
    Name = models.CharField(max_length=250)
    Desig = models.CharField(max_length=250)
    NAme_of_research_fellow = models.CharField(max_length=250)
    Invitation_paragraph = models.TextField()
    Intro = models.TextField()
    Why_am_i = models.TextField()
    Site_details = models.TextField()
    Duration = models.TextField()
    How_many = models.TextField()
    IS_my_part = models.TextField()
    Can_i_withdraw = models.TextField()
    What_will_be_done = models.TextField()
    Inter_detail =models.TextField()
    Follow_up = models.TextField()
    allot = models.TextField()
    Brief = models.TextField()
    What_are_my_responsibility = models.TextField()
    What_are_risk = models.TextField()
    What_are_benefits = models.TextField()
    Will_results = models.TextField()
    Cost_participation = models.TextField()
    Funding = models.TextField()
    If_wrong = models.TextField()
    Alt_treatment = models.TextField()
    Confidentiality = models.TextField()
    Study_approve = models.TextField()
    Whom_contact = models.TextField()

