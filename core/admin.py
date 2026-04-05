from django.contrib import admin
from django.utils.html import format_html

from .models import TeamMember, Appointment


admin.site.site_header = 'EquilbriumLegalPartners Admin'
admin.site.site_title = 'EquilbriumLegalPartners Admin'
admin.site.index_title = 'Dashboard'


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('photo_preview', 'name', 'role', 'phone', 'email', 'is_active', 'display_order')
    list_editable = ('is_active', 'display_order')
    list_filter = ('is_active',)
    search_fields = ('name', 'role', 'email', 'phone')
    ordering = ('display_order', 'name')
    readonly_fields = ('photo_preview',)

    fieldsets = (
        ('Profile', {
            'fields': ('name', 'role', 'bio', 'photo', 'photo_focus_x', 'photo_focus_y', 'photo_preview', 'is_active', 'display_order')
        }),
        ('Contact', {
            'fields': ('email', 'phone')
        }),
        ('Social Links', {
            'fields': ('linkedin_url', 'x_url', 'facebook_url')
        }),
    )

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, request, **kwargs)
        if db_field.name in {'bio', 'email', 'phone', 'linkedin_url', 'x_url', 'facebook_url'}:
            formfield.help_text = 'Optional. Leave blank if this member does not have this detail.'
        if db_field.name in {'photo_focus_x', 'photo_focus_y'}:
            formfield.help_text = 'Optional. Use 0-100 to shift the crop focus and center the face better.'
        return formfield

    def photo_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" style="width:144px;height:144px;object-fit:cover;object-position:{}% {}%;border-radius:50%;border:none;box-shadow:0 8px 18px rgba(15,23,42,.12);background:#fff;" />',
                obj.photo.url,
                obj.photo_focus_x,
                obj.photo_focus_y,
            )
        return 'No photo uploaded yet.'

    photo_preview.short_description = 'Photo preview'


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'consultant_name', 'created_at_formatted')
    list_filter = ('created_at', 'consultant')
    search_fields = ('name', 'email', 'consultant__name')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Appointment Details', {
            'fields': ('name', 'email', 'consultant', 'message', 'created_at')
        }),
    )
    
    def consultant_name(self, obj):
        return obj.consultant.name if obj.consultant else "Auto-assign"
    consultant_name.short_description = 'Consultant'
    
    def created_at_formatted(self, obj):
        return obj.created_at.strftime('%b %d, %Y - %I:%M %p')
    created_at_formatted.short_description = 'Booked On'
