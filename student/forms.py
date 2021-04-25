from django import forms
from .models import *

class AddDocument(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['name', 'doc']
        labels = {
            'name' : "Name",
            'doc' : 'Documents',
        }


class ReviewForm(forms.ModelForm):

    class Meta:
        model = hindu
        fields = '__all__'
        labels = { "Title":"1.Title of study",
                    "Place_of_study":"2.Place of study",
                    "Prin_invest":"3.Principal Investigator",
                    "Name":"4.Name",
                    "Desig":"5.Designation",
                    "NAme_of_research_fellow":"6.Name of research fellow",
                    "Invitation_paragraph":"7.Invitation Paragraph",
                    "Intro":"8.Introduction",
                    "Why_am_i":"9.Why am I being requested to participate in this study",
                    "Site_details": "10.Site Details",
                    "Duration":"11.Duration of individual patient participation",
                    "How_many":"12.How many subjects will be participating in the study",
                    "Is_my_part":"13.Is my participation Compulsory?",
                    "Can_i_withdraw":"14.Can I withdraw from the study",
                    "What_will_be_done":"15.What will be done at the first visit?",
                    "Inter_detail":"16.Intervention Details-Drugd, Surgery, Questionnaire",
                    "Follow_up":"17.Follow up Schedule (if applicable) & What will be done at the follow-ups (clinical, investigations, etc)?",
                    "allot":"18.If an allotment procedure is involved- State & explain terms like blinding/randomization",
                    "Brief":"19.Explain briefly additional investigations & procedures that are not part of standard of care but required for the study. Print instructions for the study if applicable",
                    "What_are_my_responsibility":"20.What are my responsibilities",
                    "What_are_risk":"21.What are the foreseeable risk/discomforts/inconvience involved?",
                    "What_are_benefits":"22.What are the benefits of my participation?",
                    "Will_results":"23.Will my results be informed to me?",
                    "Cost_participation":"24.What will be the cost of participation?",
                    "Funding":"25.Who is funding the study?",
                    "If_wrong":"26.If something goes wrong what happens? Who treats & bears the cost?",
                    "Alt_treatment":"27.Availability of alternate treatments, if any-",

                    "Confidentiality":"28.What about the confidentiality of my dada?",
                    "Study_approve":"29.Is the study approved by institution ethics committee?",
                    "Whom_contact":"30.Whom can I contact for more information?"
        }
