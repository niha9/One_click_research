from django.db import models
from guide.models import *
from student.models import *
from director.models import *
from budget.models import *
from secretariat.models import *



class study_design(models.Model):
    case_report = (
        ('O', 'Cohort,Prospective'), ('ER', 'Open-(non blinded)'), ('EN', 'Non-Randomized')
    )
    cs_report = models.CharField(max_length=100, choices=case_report)
    case_series = (
        ('O', 'Cohort,Retrospective'), ('ER', 'Single-blind'), ('EN', 'Study of diagnostic efficacy')
    )

    cs_series = models.CharField(max_length=100, choices=case_series)
    survey = (
        ('OC', 'Case control'), ('OS', 'Cross-sectional'), ('ERD', 'Double blind'), ('ERT', 'Triple blind')
    )
    srvey = models.CharField(max_length=100, choices=survey)
    others = models.TextField()


class Time_Frame(models.Model):
    study_coll_period = models.IntegerField()
    retro_period = models.IntegerField()
    patient_part = models.IntegerField()
    data_analysis = models.IntegerField()
    Thesis_submis = models.IntegerField()


class pat_sel_id(models.Model):
    define_pop = models.TextField()
    In_criteria = models.TextField()
    Ex_criteria = models.TextField()


class work_up(models.Model):
    clinical = models.TextField()
    Investigations = models.TextField()


class Out_funding(models.Model):
    fund_name = models.TextField()
    address = models.TextField()
    email = models.EmailField(max_length=100, null=False, blank=False)
    type = models.TextField()


class study_step(models.Model):
    patient_sel_id = models.ForeignKey(pat_sel_id, on_delete=models.CASCADE)
    inf_consent = (
        ('W', 'Written'), ('T', 'Telephonic'), ('V', 'Waiver'), ('O', 'Other')
    )
    informed_consent = models.CharField(max_length=100, choices=inf_consent)
    int_code = (
        ('D', 'Drug Studies For approved indication'),
        ('O', 'Off-label use of drugs approved for other indication'),
        ('S', 'Surgery'),
        ('T', 'Special Test'),
        ('Q', 'Questionaire'),
        ('A', 'Any other')
    )
    Intevention_code = models.CharField(max_length=100, choices=int_code)
    Q_valid = (
        ('Y', 'YES'), ('N', 'NO')
    )
    Questionaire_valid = models.CharField(max_length=100, choices=Q_valid)
    R_lang = (
        ('Y', 'YES'), ('N', 'NO')
    )
    Regional_lang = models.CharField(max_length=100, choices=R_lang)
    work_up_id = models.ForeignKey(work_up, on_delete=models.CASCADE)
    med_id = models.URLField()
    surgical_id = models.URLField()
    lab_id = models.URLField()
    outcome_measure_id = models.TextField()
    methodology = models.TextField()
    proforma = models.TextField()
    translation = models.TextField()
    budget_id = models.CharField(max_length=100)
    # outside_fund = models.ForeignKey(Out_funding, on_delete=models.CASCADE)


class expected_comp(models.Model):
    data_coll_date = models.DateTimeField()
    data_analysis_date = models.DateTimeField()
    write_up = models.DateTimeField()


class clinical_studies(models.Model):
    total_sample_sanctioned = models.IntegerField()
    no_patients_screened = models.IntegerField()
    no_failures = models.IntegerField()
    failures_reasons = models.CharField(max_length=100)
    no_patients_enrolled = models.IntegerField()
    no_patients_discontinued = models.IntegerField()


class lab_study(models.Model):
    nos_sanctioned = models.IntegerField()
    nos_collected = models.IntegerField()
    nos_tested = models.IntegerField()
    nos_rejected = models.TextField()
    new_tech_established = models.TextField()


class paper_presentation(models.Model):
    pa_level = (
        (1, 'Local'), (2, 'National'), (3, 'International'),
    )
    p_level = models.CharField(max_length=100, choices=pa_level)
    conf_name = models.TextField()
    Year = models.DateTimeField()
    other = models.TextField()
    pa_published = (
        (1, 'YES'), (2, 'NO'),
    )
    published = models.CharField(max_length=100, choices=pa_published)
    certificate = models.URLField()


class feedback(models.Model):
    study_improved_clin_practice = models.TextField()
    any_other = models.TextField()
    problems_faced = models.TextField()


class protocol_amend(models.Model):
    has_amended = (
        (1, 'YES'), (2, 'NO')
    )
    has_been_amended = models.CharField(max_length=100, choices=has_amended)
    comm_appr = models.DateTimeField()


class prog_report(models.Model):
    date_of_comencenment = models.DateField()
    exp_date_completion = models.ForeignKey(expected_comp, on_delete=models.CASCADE)
    project_rate = models.TextField()
    breif = (
        (1, 'Patients(Clinical)'), (2, 'Laboratory')
    )
    brief_summary = models.CharField(max_length=100, choices=breif)
    patient_clinical_id = models.ForeignKey(clinical_studies, on_delete=models.CASCADE)
    lab_study_id = models.ForeignKey(lab_study, on_delete=models.CASCADE)
    provisonal = models.TextField()
    ######budget#####
    #####study extension#####
    protocol_id = models.ForeignKey(protocol_amend, on_delete=models.CASCADE)
    paper_id = models.ForeignKey(paper_presentation, on_delete=models.CASCADE)
    feed_id = models.ForeignKey(feedback, on_delete=models.CASCADE)



# todo give info for coinvestigator
class comp_report(models.Model):
    p_id = models.ForeignKey(Principal_investigator, on_delete=models.CASCADE)
   # ci_id = models.ForeignKey(Co_Investigator, on_delete=models.CASCADE)
    st_id = models.ForeignKey(Std_details, on_delete=models.CASCADE)
    date_study_completion = models.DateField()
    clin_stud_id = models.ForeignKey(clinical_studies, on_delete=models.CASCADE)
    budeget_status = models.BooleanField(default=True)
    protocol_id = models.ForeignKey(protocol_amend, on_delete=models.CASCADE)
    #############budget details###############
    original_protocol_changed = models.BooleanField(default=True)
    paper_id = models.ForeignKey(paper_presentation, on_delete=models.CASCADE)

    #----------------------------------------------------------------------------------------------------------
class project_details(models.Model):


    # todo project code was ccommented .. use python generated ids

    #project_code_no = models.CharField(editable=True, max_length=100)

    # 1
    PI_id = models.ForeignKey(Principal_investigator, on_delete=models.CASCADE)
    #Co_id = models.ForeignKey(Principal_investigator, on_delete=models.CASCADE)
    stud_id = models.ForeignKey(Std_details, on_delete=models.CASCADE)
    Time_frame_id = models.ForeignKey(Time_Frame, on_delete=models.CASCADE)

    coinvestigator_name = models.CharField(max_length=100)
    coinvestigator_designation  = models.CharField(max_length=100)


    # 4
    period_of_data = models.IntegerField()
    enroll_period = models.IntegerField()

    budget_estimate = models.IntegerField()

    project_title = models.CharField(max_length=256)
    appr_date_erb = models.DateField(null=True)
    sample_size = models.IntegerField()
    fund = (
        ('H', 'HH'), ('O', 'Out')
    )

    choose_fund = models.CharField(max_length=100, choices=fund)
  #  Funding_body = models.ForeignKey(Out_funding, on_delete=models.CASCADE)
class project_details2(models.Model):
    studd_id = models.ForeignKey(Std_details, on_delete=models.CASCADE)
    st_design_id = models.ForeignKey(study_design, on_delete=models.CASCADE)
    study_steps_id = models.ForeignKey(study_step, on_delete=models.CASCADE)
    # progress_report_id = models.ForeignKey(prog_report, on_delete=models.CASCADE)
    # completion_report_id = models.ForeignKey(comp_report, on_delete=models.CASCADE)
    # feedback_id = models.ForeignKey(feedback, on_delete=models.CASCADE)
    Hypothesis = models.TextField()
    Rationale = models.TextField()
    Aim = models.TextField()
    objectives = models.TextField()
    Lit_review = models.TextField()
    preliminary_work= models.TextField()
    Research_plan= models.TextField()
    conflict_of_interest = models.BooleanField(max_length=2)
    conflict_comment = models.CharField(max_length=100)


class collaborations(models.Model):
    Institue = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Collab_type = models.TextField()
    Ec_approval = models.BooleanField(max_length=2)
    Authorship = models.TextField()
