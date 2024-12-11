from django import forms
from .models import Customer, Feedback
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField

class SignupForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    first_name = forms.CharField(max_length=30, required=True, label='First Name')
    last_name = forms.CharField(max_length=30, required=True, label='Last Name')
    email = forms.EmailField(max_length=254, required=True, label='Email Address')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2


class CustomerFeedbackForm(forms.ModelForm):
    NAME = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}),
        required=True
    )
    EMAIL = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        required=True
    )
    OCCUPATION = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your occupation'}),
        required=False
    )
    PHONE_NUMBER = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
        required=False
    )

    CHOICES = [
        (1, 'Very Bad'),
        (2, 'Bad'),
        (3, 'Good'),
        (4, 'Excellent'),
    ]

    QUESTIONS = [
        'How satisfied are you with our product/service?',
        'How would you rate the quality of the customer support you received?',
        'Were you pleased with the speed and efficiency of our service?',
        'How would you rate the professionalism and friendliness of our staff?',
        'How would you rate the availability of our products/services?',
        'How would you rate the variety of products/services we offer?',
        'How would you rate the response time of our customer service?',
        'How would you rate our communication?',
        'How would you rate the effort it took to resolve your issue with us?',
        'How would you rate your overall experience with us?',
    ]

    class Meta:
        model = Feedback
        fields = ['question_1', 'question_2', 'question_3', 'question_4', 'question_5', 'question_6', 'question_7', 'question_8', 'question_9', 'question_10']
        widgets = {
            'question_1': forms.RadioSelect(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')]),
            'question_2': forms.RadioSelect(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')]),
            'question_3': forms.RadioSelect(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')]),
            'question_4': forms.RadioSelect(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')]),
            'question_5': forms.RadioSelect(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')]),
            'question_6': forms.RadioSelect(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')]),
            'question_7': forms.RadioSelect(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')]),
            'question_8': forms.RadioSelect(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')]),
            'question_9': forms.RadioSelect(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')]),
            'question_10': forms.RadioSelect(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')]),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for idx, question in enumerate(self.QUESTIONS, start=1):
            field_name = f'question_{idx}'
            self.fields[field_name].label = question
            self.fields[field_name].choices = self.CHOICES
            self.fields[field_name].required = True

    captcha = ReCaptchaField()


class ComplaintFeedbackForm(forms.ModelForm):
    NAME = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}),
        required=True
    )
    EMAIL = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        required=True
    )
    OCCUPATION = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your occupation'}),
        required=False
    )
    PHONE_NUMBER = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
        required=False
    )

    CHOICES = [
        (1, 'Very Bad'),
        (2, 'Bad'),
        (3, 'Good'),
        (4, 'Excellent'),
    ]

    QUESTIONS = [
        'How would you rate the clarity of the information provided regarding your complaint?',
        'How satisfied were you with the timeliness of the response to your complaint?',
        'How well did our staff handle your complaint?',
        'How would you rate the professionalism of the customer service representative you spoke with?',
        'How likely are you to reach out to us again for assistance after this experience?',
        'How would you rate the overall quality of the resolution provided for your complaint?',
        'How clearly were your concerns understood by our team?',
        'How would you rate the ease of the complaint submission process?',
        'How likely are you to recommend our service to others based on your experience?',
        'How effective do you think our communication was during the complaint resolution process?',
    ]

    class Meta:
        model = Feedback
        fields = ['question_1', 'question_2', 'question_3', 'question_4', 'question_5', 'question_6', 'question_7', 'question_8', 'question_9', 'question_10']
        widgets = {
            'question_1': forms.RadioSelect(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')]),
            'question_2': forms.RadioSelect(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')]),
            'question_3': forms.RadioSelect(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')]),
            'question_4': forms.RadioSelect(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')]),
            'question_5': forms.RadioSelect(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')]),
            'question_6': forms.RadioSelect(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')]),
            'question_7': forms.RadioSelect(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')]),
            'question_8': forms.RadioSelect(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')]),
            'question_9': forms.RadioSelect(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')]),
            'question_10': forms.RadioSelect(choices=[(1, 'Very Bad'), (2, 'Bad'), (3, 'Good'), (4, 'Excellent')]),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for idx, question in enumerate(self.QUESTIONS, start=1):
            field_name = f'question_{idx}'
            self.fields[field_name].label = question
            self.fields[field_name].choices = self.CHOICES
            self.fields[field_name].required = True

    captcha = ReCaptchaField()


class ComplimentFeedbackForm(forms.ModelForm):
    NAME = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}),
        required=True
    )
    EMAIL = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        required=True
    )
    OCCUPATION = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your occupation'}),
        required=False
    )
    PHONE_NUMBER = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
        required=False
    )
    compliment_feedback = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Please provide your feedback here...', 'rows': 50}),
        required=True
    )
   
    class Meta:
        model = Feedback
        fields = ['NAME', 'EMAIL', 'OCCUPATION', 'PHONE_NUMBER', 'compliment_feedback']

    captcha = ReCaptchaField()