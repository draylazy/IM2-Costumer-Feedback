from django.shortcuts import render, redirect
from .forms import CustomerFeedbackForm, ComplaintFeedbackForm, ComplimentFeedbackForm, SignupForm
from .models import Customer, Feedback
from django.core.mail import send_mail
from django.contrib.auth import login
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render



@login_required
def home_view(request):
    return render(request, 'UI/home.html')

def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_staff or user.is_superuser:
                login(request, user)
                return redirect('admin_dashboard')  
            else:
                messages.error(request, "You don't have admin access.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'UI/admin_login.html', {'form': form})


@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to access the admin dashboard.")
        return redirect('home')
    users = User.objects.all()
    return render(request, 'UI/admin_dashboard.html', {'users': users})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('login') 
    else:
        form = SignupForm()
    return render(request, 'UI/signup.html', {'form': form})

def thank_you(request):
    return render(request, 'UI/thankyou.html')

def feedback_view(request):
    if request.method == 'POST':
        form = CustomerFeedbackForm(request.POST)
        if form.is_valid():
            customer, created = Customer.objects.get_or_create(
                email=form.cleaned_data['EMAIL'],
                defaults={
                    'name': form.cleaned_data['NAME'],
                    'occupation': form.cleaned_data['OCCUPATION'],
                    'phone_number': form.cleaned_data['PHONE_NUMBER']
                }
            )

            feedback = form.save(commit=False)
            feedback.customer = customer
            feedback.save()

            email_body = (
                f"Thank you for your feedback, {customer.name}!\n\n"
                "Here are your responses:\n"
                f"1. How would you rate our service? {feedback.get_question_1_display()}\n"
                f"2. How likely are you to recommend us to a friend? {feedback.get_question_2_display()}\n"
                f"3. How satisfied are you with your experience? {feedback.get_question_3_display()}\n"
                f"4. How would you rate our customer support? {feedback.get_question_4_display()}\n"
                f"5. How well did our service meet your expectations? {feedback.get_question_5_display()}\n"
                f"6. How would you rate the quality of our product? {feedback.get_question_6_display()}\n"
                f"7. How likely are you to use our service again? {feedback.get_question_7_display()}\n"
                f"8. How would you rate the value for money? {feedback.get_question_8_display()}\n"
                f"9. How well do you think we handle customer feedback? {feedback.get_question_9_display()}\n"
                f"10. Overall, how would you rate us? {feedback.get_question_10_display()}\n\n"
                "We appreciate your feedback and will use it to improve our services."
            )

            send_mail(
                'Thank you for your feedback!',
                email_body,
                settings.DEFAULT_FROM_EMAIL,
                [customer.email],
                fail_silently=False,
            )

            return redirect('thank_you')
    else:
        form = CustomerFeedbackForm()

    return render(request, 'UI/feedback.html', {'form': form})

def complaint_view(request):
    if request.method == 'POST':
        form = ComplaintFeedbackForm(request.POST)
        if form.is_valid():
            customer, created = Customer.objects.get_or_create(
                email=form.cleaned_data['EMAIL'],
                defaults={
                    'name': form.cleaned_data['NAME'],
                    'occupation': form.cleaned_data['OCCUPATION'],
                    'phone_number': form.cleaned_data['PHONE_NUMBER']
                }
            )

            feedback = form.save(commit=False)
            feedback.customer = customer
            feedback.save()

            email_body = (
                 f"Thank you for your feedback, {customer.name}!\n\n"
                    "Here are your complaint responses:\n"
                f"1. How would you rate the clarity of the information provided regarding your complaint? {feedback.get_question_1_display()}\n"
                f"2. How satisfied were you with the timeliness of the response to your complaint? {feedback.get_question_2_display()}\n"
                f"3. How well did our staff handle your complaint? {feedback.get_question_3_display()}\n"
                f"4. How would you rate the professionalism of the customer service representative you spoke with? {feedback.get_question_4_display()}\n"
                f"5. How likely are you to reach out to us again for assistance after this experience? {feedback.get_question_5_display()}\n"
                f"6. How would you rate the overall quality of the resolution provided for your complaint? {feedback.get_question_6_display()}\n"
                f"7. How clearly were your concerns understood by our team? {feedback.get_question_7_display()}\n"
                f"8. How would you rate the ease of the complaint submission process? {feedback.get_question_8_display()}\n"
                f"9. How likely are you to recommend our service to others based on your experience? {feedback.get_question_9_display()}\n"
                f"10. How effective do you think our communication was during the complaint resolution process? {feedback.get_question_10_display()}\n\n"
                    "We appreciate your feedback and will use it to improve our services."
            )

            send_mail(
                'Thank you for your feedback!',
                email_body,
                settings.DEFAULT_FROM_EMAIL,
                [customer.email],
                fail_silently=False,
            )

            return redirect('thank_you')
    else:
        form = ComplaintFeedbackForm()

    return render(request, 'UI/complaint.html', {'form': form})

def compliment_view(request):
    if request.method == 'POST':
        form = ComplimentFeedbackForm(request.POST)
        if form.is_valid():
            customer, created = Customer.objects.get_or_create(
                email=form.cleaned_data['EMAIL'],
                defaults={
                    'name': form.cleaned_data['NAME'],
                    'occupation': form.cleaned_data['OCCUPATION'],
                    'phone_number': form.cleaned_data['PHONE_NUMBER']
                }
            )

            feedback = form.save(commit=False)
            feedback.customer = customer
            feedback.save()

            email_body = (
                f"Thank you for your feedback, {customer.name}!\n\n"
                "Here is your compliment response:\n"
                f"{form.cleaned_data['FEEDBACK']}\n\n"
                "We appreciate your feedback and will use it to improve our services."
            )

            send_mail(
                'Thank you for your feedback!',
                email_body,
                settings.DEFAULT_FROM_EMAIL,
                [customer.email],
                fail_silently=False,
            )

            return redirect('thank_you')
    else:
        form = ComplimentFeedbackForm()

    return render(request, 'UI/compliment.html', {'form': form})

def admin_dashboard(request):
    customers = Customer.objects.all()
    feedbacks = Feedback.objects.all()
    return render(request, 'UI/admin_dashboard.html', {'customers': customers, 'feedbacks': feedbacks})

