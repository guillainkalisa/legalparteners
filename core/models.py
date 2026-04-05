from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class TeamMember(models.Model):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    photo_focus_x = models.PositiveIntegerField(default=50, validators=[MinValueValidator(0), MaxValueValidator(100)])
    photo_focus_y = models.PositiveIntegerField(default=50, validators=[MinValueValidator(0), MaxValueValidator(100)])
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    linkedin_url = models.URLField(blank=True)
    x_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    display_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', 'name']

    def __str__(self):
        return f"{self.name} ({self.role})"


class Appointment(models.Model):
    name = models.CharField(max_length=150, help_text="Your full name")
    email = models.EmailField(help_text="Your email address")
    consultant = models.ForeignKey(TeamMember, on_delete=models.SET_NULL, null=True, blank=True, help_text="Leave blank to auto-assign")
    message = models.TextField(blank=True, help_text="Additional notes or details about your inquiry")
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Appointment'
        verbose_name_plural = 'Appointments'
    
    def __str__(self):
        consultant_name = self.consultant.name if self.consultant else "Auto-assign"
        return f"Appointment: {self.name} ({consultant_name})"
