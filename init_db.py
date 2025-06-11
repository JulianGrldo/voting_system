import logging
from app.database import SessionLocal, engine, Base
from app.models import Voter, Candidate

# Configurar logging (para ver mensajes de error/info)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_db():
    db = SessionLocal()
    try:
        # 1. Crear tablas si no existen
        Base.metadata.create_all(bind=engine)

        # 2. Verificar si ya hay datos para no duplicar
        if db.query(Voter).count() == 0:
            # Datos de ejemplo para votantes
            voters = [
                Voter(name="Juan Pérez", email="juan@example.com"),
                Voter(name="María García", email="maria@example.com"),
            ]
            
            # Datos de ejemplo para candidatos
            candidates = [
                Candidate(name="Sofía Ramírez", party="Partido Verde"),
                Candidate(name="Pedro Sánchez", party="Partido Azul"),
            ]
            
            # Insertar datos en la base de datos
            db.add_all(voters + candidates)
            db.commit()
            logger.info("✅ Datos iniciales insertados correctamente")
        else:
            logger.info("ℹ️ La base de datos ya contiene datos")
    except Exception as e:
        logger.error(f"❌ Error al inicializar la base de datos: {str(e)}")
        raise
    finally:
        db.close()

if __name__ == "__main__":
    init_db()