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
- Total de jugadores que participarán en el campeonato
- Quién es el jugador más joven
- Quién es el jugador mas viejo
- Cuántos jugadores suplentes hay
- Promedio de número jugadores suplentes en cada equipo
- Cuál de los equipo fue el que mas registró jugadores?
- Cuál es la edad promedio de los jugadores?
- Cuál es el promedio de número de jugadores en cada equipo?
- Quién es el técnico más viejo

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
