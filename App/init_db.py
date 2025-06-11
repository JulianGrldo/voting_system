import logging
from App.database import SessionLocal, engine, Base
from App.models import Voter, Candidate


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_db():
    db = SessionLocal()
    try:
       
        Base.metadata.create_all(bind=engine)

      
        if db.query(Voter).count() == 0:
           
            voters = [
                Voter(name="Juan Pérez", email="juan@example.com"),
                Voter(name="María García", email="maria@example.com"),
            ]
            
           
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