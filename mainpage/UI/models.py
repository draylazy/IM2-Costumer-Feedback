from django.db import models
from django.utils import timezone

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    occupation = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return self.name

class Feedback(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='feedbacks')
    question_1 = models.IntegerField(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')], null=True, blank=True)
    question_2 = models.IntegerField(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')], null=True, blank=True)
    question_3 = models.IntegerField(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')], null=True, blank=True)
    question_4 = models.IntegerField(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')], null=True, blank=True)
    question_5 = models.IntegerField(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')], null=True, blank=True)
    question_6 = models.IntegerField(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')], null=True, blank=True)
    question_7 = models.IntegerField(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')], null=True, blank=True)
    question_8 = models.IntegerField(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')], null=True, blank=True)
    question_9 = models.IntegerField(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')], null=True, blank=True)
    question_10 = models.IntegerField(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')], null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Feedback from {self.customer.name}"
        
