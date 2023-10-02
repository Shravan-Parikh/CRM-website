from django.db import models
from django.contrib.auth.models import User

class Lead(models.Model):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    CHOICES_PRIORITY=(
        (LOW,'low'),
        (HIGH,'high'),
        (MEDIUM,'medium'),
    )
    
    NEW ='new'
    CONTACTED = 'contacted'
    WON ='won'
    LOST ='lost'

    CHOICES_STATUS = (
        (NEW,'new'),
        (CONTACTED,'contacted'),
        (WON,'won'),
        (LOST,'lost'),
    )
    INSTAGRAM='instagram'
    GOOGLE_ADS='google_ads'
    WOM='wom'
    FACEBOOK='facebook'
    EMAIL_MARKETING='email_marketing'
    OTHERS='others'

    CHOICES_SOURCE = (
        (INSTAGRAM,'instagram'),(GOOGLE_ADS,'google_ads'),(WOM,'wom'),(FACEBOOK,'facebook'),(EMAIL_MARKETING,'email_marketing'),(OTHERS,'others'),
    )

    SILK='silk'
    COTTON='cotton'
    WOOL='wool'
    POLYSTER='polyster'
    SATIN='satin'
    VELVET='velvet'

    CHOICES_FABRIC=((SILK,'silk'),(COTTON,'cotton'),(POLYSTER,'polyster'),(WOOL,'wool'),(SATIN,'satin'),(VELVET,'velvet'),)

    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField(blank=True,null=True)
    
    priority= models.CharField(max_length=10,choices=CHOICES_PRIORITY,default=MEDIUM)
    status= models.CharField(max_length=10,choices=CHOICES_STATUS,default=NEW)
    converted_to_client = models.BooleanField(default=False)
    source = models.CharField(max_length=50,choices=CHOICES_SOURCE,default='google_ads')
    fabric=models.CharField(max_length=20,choices=CHOICES_FABRIC,default='cotton')
    created_by = models.ForeignKey(User, related_name='leads',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name
