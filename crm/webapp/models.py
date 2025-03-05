from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

# - Occupancy
class Occupancy(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# - Commitment Period
class CommitmentPeriod(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# - Company
class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# - Property Type
class PropertyType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# - Compensation Payer Type
class CompPayerType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# - Loan Officer
class LoanOfficer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# - Documentation Type
class DocumentationType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# - Property State
class PropertyState(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# - Escrow / Impound Waiver Type
class EscrowImpound(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# - Loan Type
class LoanType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# - Loan Term
class LoanTerm(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# - Buydown Type
class BuydownType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# - County
class County(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        
# - Flex Term
class FlexTerm(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# - Prepayment Penalty
class PrepaymentPenalty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# - Prepayment Penalty
class TitleSelection(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
# - First Time Homebuyer
class FirstHomebuyer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# - Lender
class Lender(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)

    correspondent = models.BooleanField(default=False)
    occupancy = models.ForeignKey(Occupancy, on_delete=models.CASCADE)
    credit_score = models.PositiveIntegerField(validators=[MaxValueValidator(99)])
    commitment_period = models.ForeignKey(CommitmentPeriod, on_delete=models.CASCADE)

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    comp_payer_type = models.ForeignKey(CompPayerType, on_delete=models.CASCADE)

    loan_officer = models.ForeignKey(LoanOfficer, on_delete=models.CASCADE, null=True, blank=True)
    number_units = models.PositiveIntegerField(validators=[MaxValueValidator(99)], default='0')
    monthly_debt = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default='0.00')
    documentation_type = models.ForeignKey(DocumentationType, on_delete=models.CASCADE, null=True, blank=True)

    borrower_name = models.CharField(max_length=100, default='N/A')
    property_state = models.ForeignKey(PropertyState, on_delete=models.CASCADE, null=True, blank=True)
    dti = models.BooleanField(default=False)
    escrow_impound = models.ForeignKey(EscrowImpound, on_delete=models.CASCADE, null=True, blank=True)

    loan_type = models.ForeignKey(LoanType, on_delete=models.CASCADE, null=True, blank=True)
    zip_code = models.CharField(
        max_length=5,
        validators=[RegexValidator(regex=r'^\d{5}$', message='Enter a valid ZIP code (5 digits)')],
        default='00000'
    )
    taxes = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default='0.00')
    loan_term = models.ForeignKey(LoanTerm, on_delete=models.CASCADE, default='0')

    buydown_type = models.ForeignKey(BuydownType, on_delete=models.CASCADE, null=True, blank=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE, null=True, blank=True)
    hoi = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default='0.00')
    flex_term = models.ForeignKey(FlexTerm, on_delete=models.CASCADE, default='0')

    prepayment_penalty = models.ForeignKey(PrepaymentPenalty, on_delete=models.CASCADE, null=True, blank=True)
    financed_properties = models.PositiveIntegerField(validators=[MaxValueValidator(99)], default='0')
    finance_charges = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default='0.00')
    title_selection = models.ForeignKey(TitleSelection, on_delete=models.CASCADE, null=True, blank=True)

    loan_amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default='0.00')
    new_construction = models.BooleanField(default=False)
    first_homebuyer = models.ForeignKey(FirstHomebuyer, on_delete=models.CASCADE, null=True, blank=True)

    second_loan_amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default='0.00')
    self_employed = models.BooleanField(default=False)

    rural_property = models.BooleanField(default=False)
