from .models import Team, Player, CoachingStaff, Nationality, Position, Role
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import TeamSerializer, PlayerSerializer, CoachingStaffSerializer, NationalitySerializer, PositionSerializer, RoleSerializer
from .filters import TeamFilter, PositionFilter, PlayerFilter, CoachingStaffFilter
from rest_framework.views import APIView
from django.db.models import Max, Min, Avg, F, Count


class TeamCountView(APIView):
    """
    A view that returns the count of register teams.
    """
    def get(self, request, format=None):
        teams_count = Team.objects.count()
        content = {'Cuántos equipos hay registrados': teams_count}
        return Response(content)


class PlayerCountView(APIView):
    """
    A view that returns the count of register players.
    """
    def get(self, request, format=None):
        players_count = Player.objects.count()
        content = {'Total de jugadores que participarán en el campeonato': players_count}
        return Response(content)


class YoungestPlayerView(APIView):
    """
    A view that returns the younger player.
    """
    def get(self, request, format=None):
        youngest_player = Player.objects.earliest('calc_age')
        content = {
            'Quién es el jugador más joven': youngest_player.name_player+' '+youngest_player.last_name,
            'Edad': youngest_player.calc_age}
        return Response(content)


class OldestPlayerView(APIView):
    """
    A view that returns the oldest player.
    """
    def get(self, request, format=None):
        oldest_player = Player.objects.latest('calc_age')
        content = {
            'Quién es el jugador más viejo': oldest_player.name_player+' '+ oldest_player.last_name,
            'Edad': oldest_player.calc_age}
        return Response(content)


class SubstitutePlayersView(APIView):
    """
    A view that returns the substitute player count.
    """
    def get(self, request, format=None):
        substitute_players = Player.objects.filter(titular__exact=False).count()
        content = {'Cuántos jugadores suplentes hay': substitute_players}
        return Response(content)


class AvgSubstPlayersTeamView(APIView):
    """
    A view that returns the average number of substitute players.
    """
    def get(self, request, format=None):
        avg_substitute_players = Player.objects.filter(titular__exact=False).count() / Team.objects.count()
        content = {'Promedio de jugadores suplentes en cada equipo': avg_substitute_players}
        return Response(content)


class RegisteredMostPlayersView(APIView):
    """
    A view that returns the team that registered more players.
    """
    def get(self, request, format=None):
        registered_most_players = Team.objects.annotate(registered_players=Count('player')).order_by('-registered_players')[0]
        content = {'Cuál de los equipos fue el que más registró jugadores': registered_most_players.team_name}
        return Response(content)

class AverageAgePlayersView(APIView):
    """
    A view that returns the team that average age of players.
    """
    def get(self, request, format=None):
        average_age_players = Player.objects.aggregate(Avg('calc_age'))
        content = {'Cuál es la edad promedio de los jugadores': average_age_players}
        return Response(content)


class AveragePlayersTeamView(APIView):
    """
    A view that returns the team that average number of players.
    """
    def get(self, request, format=None):
        avg_players_team = Player.objects.count() / Team.objects.count()
        content = {'Cuál es el promedio de número de jugadores en cada equipo': avg_players_team}
        return Response(content)


class OldestCoachView(APIView):
    """
    A view that returns the oldest coach.
    """
    def get(self, request, format=None):
        oldest_coach = CoachingStaff.objects.filter(role__exact=1).latest('calc_age')
        content = {
            'Quién es el técnico más viejo': oldest_coach.coach_name+' '+ oldest_coach.last_name,
            'Edad': oldest_coach.calc_age}
        return Response(content)


class TeamViewset(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filterset_class = TeamFilter


class PlayerViewset(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filterset_class = PlayerFilter


class CoachingStaffViewset(viewsets.ModelViewSet):
    queryset = CoachingStaff.objects.all()
    serializer_class = CoachingStaffSerializer
    filterset_class = CoachingStaffFilter


class NationalityViewset(viewsets.ModelViewSet):
    queryset = Nationality.objects.all()
    serializer_class = NationalitySerializer


class PositionViewset(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    filterset_class = PositionFilter
    


class RoleViewset(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


# class TeamAPIView(APIView):

#     def get(self,request):
#         teams = Team.objects.all()
#         teams_serializer = TeamSerializer(teams, many=True)
#         return Response(teams_serializer.data)