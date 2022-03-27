# Fifa API
## Descripción de la prueba
La FIFA te ha contactado para que le ayudes a consolidar la información de todos los equipos que
van a ir al próximo mundial, así que te dicen que debes crear una API con un CRUD para cada una
de la siguiente información:
- Equipo
  - Nombre del Equipo
  - Imagen de Bandera
  - Escudo del Equipo
- Jugadores del equipo, con los siguientes datos de cada jugador:
  - Foto del jugador
  - Nombre
  - Apellido
  - Fecha de nacimiento
  - Posición en la que juega
  - Número de camiseta
  - ¿Es titular?
- Cuerpo técnico
  - Nombre
  - Apellido
  - Fecha de nacimiento
  - Nacionalidad
  - Rol (técnico | asistente | médico | preparador)

## Requerimientos
De toda la información recolectada la FIFA desea tener un servicio donde retorne la siguiente
información:
- Cuántos equipos hay registrados
  http://127.0.0.1:8000/teams/count/
- Total de jugadores que participarán en el campeonato
  http://127.0.0.1:8000/players/count/
- Quién es el jugador más joven
  http://127.0.0.1:8000/players/youngestplayer/
- Quién es el jugador mas viejo
  http://127.0.0.1:8000/players/oldestplayer/
- Cuántos jugadores suplentes hay
  http://127.0.0.1:8000/players/substitute/
- Promedio de número jugadores suplentes en cada equipo
  http://127.0.0.1:8000/players/avgsubstitute/
- Cuál de los equipo fue el que mas registró jugadores?
  http://127.0.0.1:8000/teams/mostplayers/
- Cuál es la edad promedio de los jugadores?
  http://127.0.0.1:8000/players/avgsplayers/
- Cuál es el promedio de número de jugadores en cada equipo?
  http://127.0.0.1:8000/players/avgage/
- Quién es el técnico más viejo
  http://127.0.0.1:8000/coachs/oldestcoach/

## Desarrollo
### Api Root
The default basic root view for DefaultRouter
```json
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "team": "http://127.0.0.1:8000/team/",
    "player": "http://127.0.0.1:8000/player/",
    "coachingstaff": "http://127.0.0.1:8000/coachingstaff/",
    "nationality": "http://127.0.0.1:8000/nationality/",
    "position": "http://127.0.0.1:8000/position/",
    "role": "http://127.0.0.1:8000/role/"
}
```
### Evidencias consultas
![Consulta 1](https://raw.githubusercontent.com/davidbcaro/fifa-api/main/queries/01-TeamCount.png)
![Consulta 2](https://raw.githubusercontent.com/davidbcaro/fifa-api/main/queries/02-PlayerCount.png)
![Consulta 3](https://raw.githubusercontent.com/davidbcaro/fifa-api/main/queries/03-YoungestPlayer.png)
![Consulta 4](https://raw.githubusercontent.com/davidbcaro/fifa-api/main/queries/04-OldestPlayer.png)
![Consulta 5](https://raw.githubusercontent.com/davidbcaro/fifa-api/main/queries/05-SubstitutePlayers.png)
![Consulta 6](https://raw.githubusercontent.com/davidbcaro/fifa-api/main/queries/06-AvgSubstPlayersTeam.png)
![Consulta 7](https://raw.githubusercontent.com/davidbcaro/fifa-api/main/queries/07-RegisteredMostPlayers.png)
![Consulta 8](https://raw.githubusercontent.com/davidbcaro/fifa-api/main/queries/08-AveragePlayersTeam.png)
![Consulta 9](https://raw.githubusercontent.com/davidbcaro/fifa-api/main/queries/09-AverageAgePlayers.png)
![Consulta 10](https://raw.githubusercontent.com/davidbcaro/fifa-api/main/queries/10-OldestCoach.png)
