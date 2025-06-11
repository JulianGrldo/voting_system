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
