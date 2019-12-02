# Register your models here.
from django.contrib import admin

from basketball.models import Ticket, Sport, Game, PaymentMethod

# Register your models here.

admin.site.register(Ticket)
admin.site.register(Sport)
admin.site.register(Game)
admin.site.register(PaymentMethod)