# Contact & Appointment System - Setup & Implementation Guide

## Overview
You now have a fully functional, modern Contact & Appointment page with:
- **3-column responsive grid layout** (Maps | Company Details | Booking Form)
- **Google Maps embed** centered on Kigali, Rwanda
- **Professional company details** with polished icons
- **Dynamic appointment booking form** with email notifications
- **Multi-language support** (English, Swahili, French)
- **Email notifications** to valuatorcompanyltd@gmail.com

---

## What Was Created

### 1. **Database Model** (`core/models.py`)
New `Appointment` model with:
- `name` - Client's full name (required)
- `email` - Client's email (required)
- `consultant` - FK to TeamMember (optional, auto-assign if not selected)
- `message` - Additional notes (optional)
- `created_at` - Timestamp (auto)

### 2. **Forms** (`core/forms.py`)
- `AppointmentForm` - Handles appointment submissions with:
  - Bootstrap/Tailwind-ready form styling
  - "Not Sure / Assign for Me" default option
  - Placeholder text and help text
  - Client-side validation ready

### 3. **Views** (`core/views.py`)
- `contact()` view handles:
  - GET: Displays contact page with form
  - POST: Processes form, saves to DB, sends email notification
  - Returns JSON response for AJAX form submission
  - Includes success/error handling

### 4. **Admin Interface** (`core/admin.py`)
- `AppointmentAdmin` registered with:
  - List display: Name | Email | Consultant | Created Date
  - Filtering by date and consultant
  - Search by name, email, consultant
  - Read-only created_at field
  - Formatted date display

### 5. **Template** (`templates/contact.html`)
Modern, professional template featuring:
- **Header** with title and language switcher
- **3-Column Grid**:
  - **Left**: Google Maps (centered on Kigali)
  - **Middle**: Company info (Location, Phone, Email, Hours)
  - **Right**: Booking form
- **Professional Styling**:
  - Deep blue/white color scheme
  - 20px border radius on cards
  - Subtle shadows & hover effects
  - Responsive design (1 column on mobile)
- **Interactive Features**:
  - Form validation with error display
  - Success/error toast notifications
  - Loading state on submit button
  - AJAX submission (no page reload)
  - Multi-language support with localStorage

### 6. **URL Route** (`core/urls.py`)
- Added `path('contact/', views.contact, name='contact')`
- Accessible at `/contact/`

### 7. **Email Configuration** (`equilibriumpartners/settings.py`)
- Development: Uses console backend (prints to console)
- Production-ready comments for SMTP configuration
- See "Email Setup" section below for production use

### 8. **Database Migration** (`core/migrations/0003_appointment.py`)
- Creates `core_appointment` table
- Already executed during setup

---

## Features in Detail

### 💌 Email Notifications
When a user submits an appointment:
1. Email sent to `valuatorcompanyltd@gmail.com` with:
   - User's name, email, message
   - Requested consultant (or "Assign Automatically")
   - Full appointment details
2. User sees success toast notification
3. Form clears automatically
4. Database record created for your records

### 🌐 Multi-Language Support
The contact page supports:
- **English (en)** - Default
- **Swahili (sw)**
- **French (fr)**

Language choice is saved to localStorage and persists across page visits.

### 📱 Responsive Design
- **Desktop** (1280px+): 3-column grid layout
- **Tablet** (768px-1024px): Stacked columns
- **Mobile** (< 768px): Single column, full-width

### 🎨 Professional Styling
- **Colors**: Deep blues (#0f172a, #1e3a8a) with light blues (#3b82f6)
- **Spacing**: 2rem gaps, 2.5rem padding on cards
- **Shadows**: Subtle 4px-12px shadows with hover effects
- **Borders**: 20px border radius on cards, 12px on form inputs
- **Animations**: Slide-in toast, hover transforms

---

## How to Use

### 1. **View Appointments in Admin**
```
1. Go to http://localhost:8000/admin
2. Login with admin credentials
3. Click "Appointments" in left sidebar
4. View, edit, or delete appointment records
```

### 2. **Customize Company Details**
Update these in `templates/contact.html`:
- Phone number (currently: +250 798 123 456)
- Email (currently: info@equilibriumparlegalpartners.rw)
- Business hours
- Map embed (currently: centered on Kigali)

### 3. **Access the Contact Page**
```
Route: /contact/
Direct: http://localhost:8000/contact/
```

### 4. **Test Email Sending**
In development (console backend):
1. Submit the form
2. Check Django server console for email output
3. Email content will be printed to terminal

---

## Email Setup (Production)

### Option A: Gmail SMTP
1. **Enable 2-Factor Authentication** on your Gmail account
2. **Generate App Password**:
   - Go to myaccount.google.com/apppasswords
   - Select "Mail" and "Windows Computer"
   - Copy the 16-character password
3. **Update `equilibriumpartners/settings.py`**:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-16-char-app-password'
DEFAULT_FROM_EMAIL = 'noreply@equilibriumparlegalpartners.rw'
```

### Option B: sendgrid, Mailgun, or Other Provider
Follow their SMTP documentation and update the email settings accordingly.

### Option C: Environment Variables (Recommended)
Store sensitive data in `.env` file:
```bash
# .env
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

Then in settings.py:
```python
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
```

---

## Customization Guide

### Change Colors
Edit `:root` variables in `templates/contact.html`:
```css
:root {
    --primary-dark: #0f172a;      /* Main dark blue */
    --primary-blue: #1e3a8a;      /* Secondary blue */
    --primary-light: #3b82f6;     /* Bright blue */
    --accent: #7ec8ff;            /* Light accent */
    /* ... more colors */
}
```

### Modify Form Fields
In `core/forms.py`, add/remove fields:
```python
class AppointmentForm(forms.ModelForm):
    # Add custom fields here
    phone = forms.CharField(required=False)
    
    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'consultant', 'message']
```

### Add More Languages
In `templates/contact.html`, add `data-{lang}` attributes:
```html
<h1 data-en="Get in Touch" 
    data-sw="Wasiliana Nasi" 
    data-fr="Nous Contacter"
    data-de="Kontaktieren Sie uns">
    Get in Touch
</h1>
```

Then update the language switcher buttons.

### Customize Email Template
In `core/views.py`, modify the `message` variable in the `contact()` function to create a custom email template.

---

## Troubleshooting

### Issue: Form not submitting
- **Check**: Browser console for JavaScript errors
- **Verify**: CSRF token is present in form
- **Ensure**: `POST` method is used in form tag

### Issue: Emails not sending
- **Check**: Email backend in settings.py
- **For development**: Console backend prints to server terminal
- **For production**: Check SMTP credentials and firewall rules

### Issue: Consultant dropdown is empty
- **Reason**: No active TeamMembers in database
- **Fix**: Go to admin, add TeamMembers with `is_active = True`

### Issue: Language switcher not working
- **Check**: Browser localStorage is enabled
- **Verify**: JavaScript is enabled in browser

---

## Files Modified/Created

```
Core Changes:
- core/models.py              → Added Appointment model
- core/forms.py             → Created (new) - AppointmentForm
- core/views.py             → Updated with contact() view
- core/admin.py             → Added AppointmentAdmin
- core/urls.py              → Added contact route
- core/migrations/0003_appointment.py → Created (new)

Templates:
- templates/contact.html    → Created (new) - Contact page

Configuration:
- equilibriumpartners/settings.py → Added email configuration
```

---

## Next Steps

1. ✅ **Migrations applied** - Database ready
2. 📧 **Configure email** - Set up SMTP for production
3. 👥 **Add team members** - Populate TeamMembers if not done
4. 🎨 **Customize styling** - Adjust colors/branding
5. 🧪 **Test form submission** - Try booking in development
6. 📍 **Update map location** - Change map embed coordinates
7. 🌍 **Add custom languages** - Extend multi-language support
8. 🚀 **Deploy** - Move to production with email configured

---

## Tech Stack
- **Backend**: Django 4.2+
- **Database**: SQLite (development) / PostgreSQL (production recommended)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Icons**: Font Awesome 6.5.2
- **Maps**: Google Maps Embed API
- **Email**: Django Email Backend

---

## Support Notes
- All forms use AJAX for seamless UX
- Toast notifications provide feedback
- Mobile-responsive design included
- Multi-language built-in
- Admin interface fully integrated
- Validated and tested

For updates to this system, maintain the structure and conventions used.
