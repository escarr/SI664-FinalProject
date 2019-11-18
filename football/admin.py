from django.contrib import admin

from football.models import Ticket, Sport, Game, Section, PaymentMethod

# Register your models here.

admin.site.register(Ticket)
admin.site.register(Sport)
admin.site.register(Game)
admin.site.register(Section)
admin.site.register(PaymentMethod)