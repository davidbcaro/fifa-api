from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import TeamViewset, PlayerViewset, CoachingStaffViewset, PositionViewset, NationalityViewset, RoleViewset, PlayerCountView, TeamCountView, OldestPlayerView, YoungestPlayerView, SubstitutePlayersView, AvgSubstPlayersTeamView, OldestCoachView, AverageAgePlayersView, AveragePlayersTeamView, RegisteredMostPlayersView


router = DefaultRouter()
router.register('team', TeamViewset)
router.register('player', PlayerViewset)
router.register('coachingstaff', CoachingStaffViewset)
router.register('nationality', NationalityViewset)
router.register('position', PositionViewset)
router.register('role', RoleViewset)
#router.register('team/count/$', TeamViewset)


urlpatterns = [
    path('', include(router.urls)),
    #re_path(r'^teams/count/$', TeamCountView.as_view(), name='teams_count'),
    path('teams/count/', TeamCountView.as_view(), name='teams_count'),
    path('players/count/', PlayerCountView.as_view(), name='players_count'),
    path('players/substitute/', SubstitutePlayersView.as_view(), name='substitute_players'),
    path('players/youngestplayer/', YoungestPlayerView.as_view(), name='youngest_player'),
    path('players/oldestplayer/', OldestPlayerView.as_view(), name='oldest_player'),
    path('players/avgsubstitute/', AvgSubstPlayersTeamView.as_view(), name='avg_substitute_players'),
    path('teams/mostplayers/', RegisteredMostPlayersView.as_view(), name='team_most_players'),
    path('players/avgsplayers/', AveragePlayersTeamView.as_view(), name='avg_substitute_players'),
    path('players/avgage/', AverageAgePlayersView.as_view(), name='average_age_players'),
    path('coachs/oldestcoach/', OldestCoachView.as_view(), name='oldest_coach'),

]
