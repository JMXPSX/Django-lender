# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from .models import (Lender, Occupancy, CommitmentPeriod, Company, PropertyType, CompPayerType, 
                     LoanOfficer, DocumentationType, PropertyState, EscrowImpound, LoanType, 
                     LoanTerm, BuydownType, County, FlexTerm, PrepaymentPenalty, TitleSelection,
                     FirstHomebuyer)


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput, CheckboxInput

# - Create User
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# - Login
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class CustomCheckboxInput(CheckboxInput):
    template_name = 'widgets/checkbox.html'

    def __init__(self, attrs=None):
        default_attrs = {'class': 'form-checkbox'}
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)

# - Lender Entry Form
class CreateLenderForm(forms.ModelForm):
    occupancy = forms.ModelChoiceField(queryset=Occupancy.objects.all(), initial=Occupancy.objects.first())
    commitment_period = forms.ModelChoiceField(queryset=CommitmentPeriod.objects.all(), initial=CommitmentPeriod.objects.first())
    company = forms.ModelChoiceField(queryset=Company.objects.all(), initial=Company.objects.first())
    property_type = forms.ModelChoiceField(queryset=PropertyType.objects.all(), initial=PropertyType.objects.first())
    comp_payer_type = forms.ModelChoiceField(queryset=CompPayerType.objects.all(), initial=CompPayerType.objects.first())
    loan_officer = forms.ModelChoiceField(queryset=LoanOfficer.objects.all(), initial=LoanOfficer.objects.first())
    documentation_type = forms.ModelChoiceField(queryset=DocumentationType.objects.all(), initial=DocumentationType.objects.first())
    property_state = forms.ModelChoiceField(queryset=PropertyState.objects.all(), initial=PropertyState.objects.first())
    escrow_impound = forms.ModelChoiceField(queryset=EscrowImpound.objects.all(), initial=EscrowImpound.objects.first())
    loan_type = forms.ModelChoiceField(queryset=LoanType.objects.all(), initial=LoanType.objects.first())
    loan_term = forms.ModelChoiceField(queryset=LoanTerm.objects.all(), initial=LoanTerm.objects.first())
    buydown_type = forms.ModelChoiceField(queryset=BuydownType.objects.all(), initial=BuydownType.objects.first())
    county = forms.ModelChoiceField(queryset=County.objects.all(), initial=County.objects.first())
    flex_term = forms.ModelChoiceField(queryset=FlexTerm.objects.all(), initial=FlexTerm.objects.first())
    prepayment_penalty = forms.ModelChoiceField(queryset=PrepaymentPenalty.objects.all(), initial=PrepaymentPenalty.objects.first())
    title_selection = forms.ModelChoiceField(queryset=TitleSelection.objects.all(), initial=TitleSelection.objects.first())
    first_homebuyer = forms.ModelChoiceField(queryset=FirstHomebuyer.objects.all(), initial=FirstHomebuyer.objects.first())
    class Meta:
        model = Lender
        fields = ['id', 
                  'correspondent', 'occupancy', 'credit_score', 'commitment_period', 
                  'company', 'property_type', 'monthly_income', 'comp_payer_type',
                  'loan_officer', 'number_units', 'monthly_debt', 'documentation_type',
                  'borrower_name', 'property_state', 'dti', 'escrow_impound',
                  'loan_type', 'zip_code', 'taxes', 'loan_term',
                  'buydown_type', 'county', 'hoi', 'flex_term',
                  'prepayment_penalty', 'financed_properties', 'finance_charges', 'title_selection',
                  'loan_amount', 'new_construction', 'first_homebuyer', 
                  'second_loan_amount', 'self_employed', 'rural_property'
                  ]
        widgets = {
            'correspondent': CustomCheckboxInput(attrs={'label': 'Correspondent?'}),
            'occupancy': forms.Select(attrs={'class': 'form-select block w-full mt-1'}),
            'dti': CustomCheckboxInput(attrs={'label': 'DTI Over 45% (Higher MI)'}),
            'new_construction': CustomCheckboxInput(attrs={'label': 'New Construction'}),
            'self_employed': CustomCheckboxInput(attrs={'label': 'Self Employed'}),
            'rural_property': CustomCheckboxInput(attrs={'label': 'Rural Property'}),
        }
        labels = {
            'correspondent': '',
            'occupancy': '',
            'dti': '',
            'new_construction': '',
            'self_employed': '',
            'rural_property': '',
        }

    


        
