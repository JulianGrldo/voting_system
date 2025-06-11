╔══════════════════════════════════════════╗
║          🗳️ VOTING SYSTEM API            ║
╚══════════════════════════════════════════╝


Clonar el repositorio usando visual studio code


✨ CÓMO EJECUTAR EL PROYECTO

En una terminal de visual studio ubicada en la carpeta de 
el proyecto ejecutar los siguientes comandos✨

 📥 INSTALAR DEPENDENCIAS:
   --------------------------
   pip install -r requirements.txt

 🏗️ INICIALIZAR BASE DE DATOS:
   ------------------------------
   python init_db.py

 🚀 INICIAR LA API:
   ------------------
   uvicorn app.main:app --reload --port 8000

 🌐 ENDPOINTS DISPONIBLES:
   -------------------------
   🔹 GET    http://localhost:8000/voters/
   🔹 POST   http://localhost:8000/voters/
   🔹 GET    http://localhost:8000/candidates/
   🔹 POST   http://localhost:8000/votes/

 📚 DOCUMENTACIÓN INTERACTIVA:
   ----------------------------
   🔍 Swagger UI: http://localhost:8000/docs


╔══════════════════════════════════════════╗
║          TROUBLESHOOTING                 ║
╚══════════════════════════════════════════╝

🔧 Si hay errores 500:
   - Borra voting.db y ejecuta init_db.py nuevamente

🔧 Si aparece local_kw:
   - Actualiza FastAPI: pip install --upgrade fastapi
   - Usa el flag --reload al iniciar
