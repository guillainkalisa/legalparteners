from django import forms
from .models import Appointment, TeamMember


class AppointmentForm(forms.ModelForm):
    consultant = forms.ModelChoiceField(
        queryset=TeamMember.objects.filter(is_active=True),
        required=False,
        empty_label="Not Sure / Assign for Me",
        help_text="Select a team member or leave blank for automatic assignment"
    )
    
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'consultant', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition',
                'placeholder': 'Your Full Name',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition',
                'placeholder': 'your.email@example.com',
                'required': True,
            }),
            'consultant': forms.Select(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition bg-white',
            }),
            'message': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition',
                'placeholder': 'Tell us more about your request (optional)',
                'rows': 5,
            }),
        }
