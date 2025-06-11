# 🗳️ VOTING SYSTEM API

API RESTful para gestionar un sistema de votaciones con votantes, candidatos y votos.

---

## 🚀 CÓMO EJECUTAR EL PROYECTO

### 1. Clonar el repositorio

Usa Visual Studio Code o tu editor favorito:

```bash
git clone https://github.com/JulianGrldo/voting_system.git
```

### 2. Instalar dependencias

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
pip install -r requirements.txt
```

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

### 📍 Votantes (`http://localhost:8000/voters/`)

- 🔵 `GET` Obtener lista de votantes
- 
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

### 📍 Candidatos (`http://localhost:8000/candidates/`)

- 🔵 `GET` Obtener lista de candidatos  
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

### 📍 Votos (`http://localhost:8000/votes/`)

- 🔵 `GET` Obtener lista de votos
- - 🔵 `GET` Obtener estadisticas de votos
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

- 🔵 `GET` Obtener lista de votantes

   ![image](https://github.com/user-attachments/assets/c7724089-2c2f-4aab-95b5-c60dd0b0ac33)
  
- 🔵 `GET` Obtener votante por id
  
  ![image](https://github.com/user-attachments/assets/d01ae513-be50-4438-bb9b-c208fcf1f054)

- 🟢 `POST` Crear un nuevo votante
  
   ![image](https://github.com/user-attachments/assets/3a0833b8-084a-484c-aac0-9fff1c2a6e7e)

- 🔴 `DELETE` Eliminar votante por ID  

   ![image](https://github.com/user-attachments/assets/ff8a5a1a-f90a-44f0-890b-dc7e004877ea)

---

- 🔵 `GET` Obtener lista de candidatos

   ![image](https://github.com/user-attachments/assets/03d63e00-26d5-4fdb-a0f9-4bccd795146f)

  
- 🔵 `GET` Obtener candidato por id
  
  ![image](https://github.com/user-attachments/assets/0cdd77ea-c087-4ef7-84bf-72a88b1b4115)


- 🟢 `POST` Crear un nuevo candidato
  
  ![image](https://github.com/user-attachments/assets/a70fa758-17e3-4a97-830c-1b75966f9f80)

  
 - 🔴 `DELETE` Eliminar candidato por ID  

  ![image](https://github.com/user-attachments/assets/c5b28672-dd26-4b4d-a1ae-beac9865d4cc)


---

- 🔵 `GET` Obtener votos

  ![image](https://github.com/user-attachments/assets/9c539b77-5199-40f6-a49b-6ee12c288b8e)

  
- 🔵 `GET` Obtener estadisticas
  
  ![image](https://github.com/user-attachments/assets/c581c743-7587-49bb-b640-3ecf888902b1)


- 🟢 `POST` Registrar voto
- 
  ![image](https://github.com/user-attachments/assets/12eb23e4-8ac7-446c-96a5-40847fa08ab1)


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
