from turtle import position
from rest_framework.response import Response
from rest_framework import serializers
from .models import Team, Player, CoachingStaff, Nationality, Position, Role


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):
    #position = serializers.StringRelatedField()
    #team = serializers.StringRelatedField()

    class Meta:
        model = Player
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'photo': instance.photo if instance.photo != '' else '',
            'name_player': instance.name_player, 
            'last_name': instance.last_name,
            'birth_date': instance.birth_date,
            'number': instance.number,
            'starting_XI': instance.titular,
            'position': instance.position.position_name, 
            'team': instance.team.team_name,
        }
        


class CoachingStaffSerializer(serializers.ModelSerializer):
    #role = serializers.StringRelatedField()
    #team = serializers.StringRelatedField()

    class Meta:
        model = CoachingStaff
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'coach_name': instance.coach_name, 
            'last_name': instance.last_name,
            'birth_date': instance.birth_date,
            'nationality': instance.nationality.nationality_name,
            'role': instance.role.role_name,
            'team': instance.team.team_name,
        }


class NationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Nationality
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
