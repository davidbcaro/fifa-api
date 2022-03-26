from unicodedata import name
from django.db import models
from datetime import date


class Team(models.Model):
    """ Model used to represent an Team """
    team_name = models.CharField(max_length=100, verbose_name='Nombre del equipo')
    flag_image = models.ImageField(upload_to='flags/', null=True, blank=True, verbose_name='Imagen de bandera')
    team_shield = models.ImageField(upload_to='shields/', null=True, blank=True, verbose_name='Escudo del equipo')

    def __str__(self):
        return self.team_name

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        db_table = 'equipo'
        ordering = ['id']


class Nationality(models.Model):
    """ Model used to represent the Nationality """
    nationality_name = models.CharField(max_length=100, verbose_name='Nacionalidad')

    def __str__(self):
        return self.nationality_name

    class Meta:
        verbose_name = 'Nacionalidad'
        verbose_name_plural = 'Nacionalidades'
        db_table = 'nacionalidad'
        ordering = ['id']


class Position(models.Model):
    """ Model used to represent an Position """
    position_name = models.CharField(max_length=100, verbose_name='Posición')

    def __str__(self):
        return self.position_name

    class Meta:
        verbose_name = 'Posición'
        verbose_name_plural = 'Posiciones'
        db_table = 'posicion'
        ordering = ['id']


class Role(models.Model):
    """ Model used to represent an Role """
    role_name = models.CharField(max_length=100, verbose_name='Rol')

    def __str__(self):
        return self.role_name

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
        db_table = 'rol'
        ordering = ['id']


class Player(models.Model):
    """ Model used to represent an Player """
    photo = models.ImageField(upload_to='photos/', null=True, blank=True, verbose_name='Foto del jugador')
    name_player = models.CharField(max_length=100, verbose_name='Nombre del jugador')
    last_name = models.CharField(max_length=100, verbose_name='Apellido del jugador')
    birth_date = models.DateField(verbose_name='Fecha de nacimiento')
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Posición')
    number = models.IntegerField(verbose_name='Número de camiseta')
    titular = models.BooleanField(verbose_name='Titular')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Equipo')
    calc_age = models.IntegerField(verbose_name="Edad calculada", blank=True)


    @property
    def calculate_age(self):
        if(self.birth_date != None):
            calc_age = date.today().year - self.birth_date.year
            return calc_age
    
    def save(self, *args, **kwargs):
        self.calc_age = self.calculate_age
        super(Player, self).save(*args, **kwargs)

    def __int__(self):
        return self.calc_age

    def __str__(self):
        return self.name_player
    
    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'
        db_table = 'jugador'
        ordering = ['id']


class CoachingStaff(models.Model):
    """ Model used to represent an Coaching Staff """
    coach_name = models.CharField(max_length=100, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, verbose_name='Apellido')
    birth_date = models.DateField(verbose_name='Fecha de nacimiento')
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE, verbose_name='Nacionalidad')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name='Rol')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='Equipo')
    calc_age = models.IntegerField(verbose_name="Edad calculada", blank=True)

    @property
    def calculate_age_coach(self):
        if(self.birth_date != None):
            calc_age = date.today().year - self.birth_date.year
            return calc_age
    
    def save(self, *args, **kwargs):
        self.calc_age = self.calculate_age_coach
        super(CoachingStaff, self).save(*args, **kwargs)

    def __int__(self):
        return self.calc_age

    def __str__(self):
        return self.coach_name
    
    class Meta:
        verbose_name = 'Cuerpo Técnico'
        verbose_name_plural = 'Cuerpo Técnico'
        db_table = 'cuerpo_tecnico'
        ordering = ['id']