from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

from .models import TeamMember, Appointment
from .forms import AppointmentForm


def home(request):
    team_members = TeamMember.objects.filter(is_active=True)
    return render(request, 'home.html', {'team_members': team_members})


def services(request):
    return render(request, 'services.html')


def about(request):
    team_members = TeamMember.objects.filter(is_active=True)
    return render(request, 'about.html', {'team_members': team_members})


def contact(request):
    team_members = TeamMember.objects.filter(is_active=True)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            
            # Send confirmation email to admin
            consultant_name = appointment.consultant.name if appointment.consultant else "Assign Automatically"
            
            subject = f"New Appointment Request from {appointment.name}"
            message = f"""
New appointment request received!

Client Details:
- Name: {appointment.name}
- Email: {appointment.email}
- Requested Consultant: {consultant_name}

Message:
{appointment.message if appointment.message else '(No additional message)'}

---
Please follow up with the client at {appointment.email}
            """
            
            try:
                send_mail(
                    subject,
                    message,
                    'noreply@equilibriumparlegalpartners.rw',
                    ['valuatorcompanyltd@gmail.com'],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Email error: {e}")
            
            # Return success response with user-friendly message
            return JsonResponse({
                'status': 'success',
                'message': 'Thank you! Your appointment request has been received. We will contact you shortly.'
            })
        else:
            return JsonResponse({
                'status': 'error',
                'errors': form.errors
            }, status=400)
    else:
        form = AppointmentForm()
    
    context = {
        'form': form,
        'team_members': team_members,
        'company_phone': '+250 798 123 456',
        'company_email': 'info@equilibriumparlegalpartners.rw',
        'company_address': 'Kigali, Rwanda',
    }
    
    return render(request, 'contact.html', context)
