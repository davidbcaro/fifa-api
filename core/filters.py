from django_filters import rest_framework as filters
from .models import Team, Position, Player, CoachingStaff


class TeamFilter(filters.FilterSet):
    team_name = filters.CharFilter(field_name='team_name', lookup_expr='icontains')

    class Meta:
        model = Team
        fields = ['team_name']


class PositionFilter(filters.FilterSet):
    position_name = filters.CharFilter(field_name='position_name', lookup_expr='icontains')

    class Meta:
        model = Position
        fields = ['position_name']


class PlayerFilter(filters.FilterSet):
    name_player = filters.CharFilter(field_name='name_player', lookup_expr='icontains')

    class Meta:
        model = Player
        fields = ['name_player']


class CoachingStaffFilter(filters.FilterSet):
    coach_name = filters.CharFilter(field_name='coach_name', lookup_expr='icontains')

    class Meta:
        model = CoachingStaff
        fields = ['coach_name']