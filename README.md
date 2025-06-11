# 🗳️ VOTING SYSTEM API

API RESTful para gestionar un sistema de votaciones con votantes, candidatos y votos.

---

## 🚀 CÓMO EJECUTAR EL PROYECTO

### 1. Clonar el repositorio

Usa Visual Studio Code o tu editor favorito:

```bash
git clone https://github.com/JulianGrldo/voting_system.git
```
### 1.1 IMPORTANTE

A LA CARPETA APP SE LE DEBE CAMBIAR EL NOMBRE DE App a app por que si no da error


### 2. Instalar dependencias

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
pip install -r requirements.txt
```
reinicia visual para aplicar los paquetes instalados y no den fallos

### 3. Inicializar la base de datos

```bash
python init_db.py
```

### 4. Iniciar el servidor

```bash
uvicorn app.main:app --reload --port 8000
```

---

## 🌐 ENDPOINTS DISPONIBLES

### 📍 Votantes (`http://127.0.0.1:8000/voters/`)

- 🔵 `GET` Obtener lista de votantes
  
- 🟢 `POST` Crear un nuevo votante

```json
{
  "name": "string",
  "email": "user@example.com"
}
```

- 🔴 `DELETE` Eliminar votante por ID  
  `DELETE /voters/{voter_id}`

---

### 📍 Candidatos (`http://127.0.0.1:8000/candidates/`)

- 🔵 `GET` Obtener lista de candidatos
- 
- 🟢 `POST` Crear un nuevo candidato

```json
{
  "name": "string",
  "party": "string"
}
```

- 🔴 `DELETE` Eliminar candidato por ID  
  `DELETE /candidates/{candidate_id}`

---

### 📍 Votos (`http://127.0.0.1:8000/votes/`)

- 🔵 `GET` Obtener lista de votos
- 
- - 🔵 `GET` Obtener estadisticas de votos
  - 
- 🟢 `POST` Registrar un voto

```json
{
  "voter_id": 0,
  "candidate_id": 0
}
```

---

## 📚 DOCUMENTACIÓN INTERACTIVA

- Swagger UI → [http://localhost:8000/docs](http://localhost:8000/docs)
![image](https://github.com/user-attachments/assets/0aafa889-7242-4c33-bbee-8eb4c8429027)

---
---

## 📚 IMAGENES DE EJECUCION EN POSTMAN

Metodos de postman

![image](https://github.com/user-attachments/assets/6e9d3668-3f7b-422d-a75d-d558dd13371a)


- 🔵 `GET` Obtener lista de votantes

   ![image](https://github.com/user-attachments/assets/d99036b7-4f92-4297-bcac-f7c54be1c72c)

  
- 🔵 `GET` Obtener votante por id
  
  ![image](https://github.com/user-attachments/assets/4259a4ec-4e01-4972-a8ce-cf171fc05089)


- 🟢 `POST` Crear un nuevo votante
  
   ![image](https://github.com/user-attachments/assets/78582d2a-6f75-47db-ac50-960173121b19)


- 🔴 `DELETE` Eliminar votante por ID  

   ![image](https://github.com/user-attachments/assets/57a082a3-61eb-4604-bd38-857ead6ec417)


---

- 🔵 `GET` Obtener lista de candidatos

   ![image](https://github.com/user-attachments/assets/07f51ce9-fdad-4619-868b-6b9a1363bc70)


  
- 🔵 `GET` Obtener candidato por id
  
  ![image](https://github.com/user-attachments/assets/529d40bc-5efc-4691-83ca-c993d2a70a6e)



- 🟢 `POST` Crear un nuevo candidato
  
  ![image](https://github.com/user-attachments/assets/7709fe82-d1c7-4245-920e-6e8d1fa14482)


  
 - 🔴 `DELETE` Eliminar candidato por ID  

  ![image](https://github.com/user-attachments/assets/c54db59d-99fa-4791-8487-b8545809263f)



---

- 🔵 `GET` Obtener votos

  ![image](https://github.com/user-attachments/assets/c3ce1fbb-a553-46d1-bfca-0fec04dec27a)


  
- 🔵 `GET` Obtener estadisticas
  
  ![image](https://github.com/user-attachments/assets/40d88d49-b160-446d-80b4-1ec79d50e8e5)

  json completo de la respuesta 
{
    "statistics": [
        {
            "candidate_id": 1,
            "candidate_name": "Sofía Ramírez",
            "votes": 2,
            "percentage": 13.33
        },
        {
            "candidate_id": 2,
            "candidate_name": "Pedro Sánchez",
            "votes": 6,
            "percentage": 40.0
        },
        {
            "candidate_id": 3,
            "candidate_name": "Lucía Fernández",
            "votes": 3,
            "percentage": 20.0
        },
        {
            "candidate_id": 4,
            "candidate_name": "Miguel Ángel",
            "votes": 2,
            "percentage": 13.33
        },
        {
            "candidate_id": 5,
            "candidate_name": "Diana Salazar",
            "votes": 1,
            "percentage": 6.67
        },
        {
            "candidate_id": 6,
            "candidate_name": "Andrés Pérez",
            "votes": 1,
            "percentage": 6.67
        }
    ],
    "total_voters_voted": 15

}
```json
{
  "voter_id": 0,
  "candidate_id": 0
}
```

- 🟢 `POST` Registrar voto
  
  ![image](https://github.com/user-attachments/assets/67a074c0-774f-4d00-aa38-5c9dfac2784e)



---
## 🛠️ TROUBLESHOOTING

### ❌ Error 500

- Borra el archivo `voting.db`
- Ejecuta `python init_db.py` nuevamente

### ⚠️ Error relacionado con `local_kw`

- Ejecuta:  
  ```bash
  pip install --upgrade fastapi
  ```
- Usa el flag `--reload` al iniciar el servidor:
  ```bash
  uvicorn app.main:app --reload
  ```

---

Desarrollado con ❤️ por JULIAN GRLDO
