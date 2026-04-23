# is-2026-checkpoint-01

Este es el repositorio para el Checkpoint 01 de la materia Ingeniería y Calidad de Software.

## Integrantes
| Felipe | 31477 | Feature 01 | Coordination |
| Santiago | 31481 | Feature 02 | Frontend |
| Federico | 31147 | Feature 03 | Backend |
| Tiago | 33374 | Feature 04 | Database |
| Facundo | 32874 | Feature 05 | Portainer |

## Prerrequisitos
 
- **Docker** 24 o superior
- **Docker Compose** v2 (viene incluido en Docker Desktop)
- **Git**
Probado en Windows 11 con WSL2 + Docker Desktop, y en Linux nativo.
 
---
 
## Cómo levantar el proyecto
 
### 1. Clonar el repositorio
 
```bash
git clone https://github.com/fpianelli/is-2026-checkpoint-01.git
cd is-2026-checkpoint-01
```
 
### 2. Crear el archivo `.env`
 
Copiá la plantilla y completá con los valores que quieras:
 
```bash
cp .env.example .env
```
 
Los valores por defecto del `.env.example` son placeholders descriptivos. 
 
### 3. Levantar todos los servicios
 
```bash
docker compose up -d --build
```
 
El primer arranque tarda 1-2 minutos porque tiene que descargar las imágenes y construir las de frontend y backend. PgAdmin tarda un rato más en arrancar, si se inicia inmediatamente después de correr docker compose up no va a funcionar. Se debe esperar mínimo un minuto. 
 
### 4. Verificar que todos los contenedores están corriendo
 
```bash
docker compose ps
```
---

## URLs de acceso
 
| Frontend   | http://localhost:8080 |
| Backend    | http://localhost:5000/api/team | devuelve JSON con integrantes  |
| Portainer  | http://localhost:9000      | 
| pgadmin    | http://localhost:5050      | Credenciales en `.env`  

