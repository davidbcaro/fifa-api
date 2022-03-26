from django.contrib import admin
from .models import Team, Player, CoachingStaff, Nationality, Position, Role


admin.site.register(Team)
#admin.site.register(Player)
admin.site.register(CoachingStaff)
admin.site.register(Nationality)
admin.site.register(Position)
admin.site.register(Role)


@admin.register(Player) 
class PlayerAdmin(admin.ModelAdmin):
     list_display = ['name_player', 'last_name', 'birth_date', 'position', 'number', 'calc_age', 'titular']