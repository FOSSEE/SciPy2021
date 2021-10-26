from django.contrib import admin
from .models import CFP, RegistrationDetail, Proposal, TentativeSchedule

class CFPAdmin(admin.ModelAdmin):
	list_display = ['start_date','end_date','date_of_announcement']

class RegistrationDetailAdmin(admin.ModelAdmin):
	list_display = ['registration_type', 'start_date', 'end_date', 'registration_ticket','registration_description']		

class ProposalAdmin(admin.ModelAdmin):
	list_display = ['title', 'email', 'phone']

class TentativeScheduleAdmin(admin.ModelAdmin):
	list_display = ['schedule_table']
		

admin.site.register(CFP, CFPAdmin)
admin.site.register(RegistrationDetail, RegistrationDetailAdmin)
admin.site.register(Proposal, ProposalAdmin)
admin.site.register(TentativeSchedule, TentativeScheduleAdmin)
