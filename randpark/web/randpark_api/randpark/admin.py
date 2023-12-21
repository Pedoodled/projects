from django.contrib import admin

from .models import Course, Booking, TeeTimes
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Course Details", {"fields": ["name", "description", "rating_yellow", "rating_white", "rating_gold", "rating_red", "rating_blue", "record_mens", "record_ladies"]})
    ]
    list_display = ["name"]

class BookingAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Booking", {"fields": ["member_no_1", "member_no_2", "member_no_3", "member_no_4", "play_date", "course_id", "tee_time_id"]})
    ]
    list_display = ["course_id", "tee_time_id", "play_date", "member_no_1", "member_no_2", "member_no_3", "member_no_4"]
    list_filter = ["course_id", "tee_time_id", "play_date"]
    search_fields = ["play_date", "member_no_1", "member_no_2", "member_no_3", "member_no_4"]

admin.site.register(Course, CourseAdmin) 
admin.site.register(Booking, BookingAdmin)