import logging
from app.database import SessionLocal, engine, Base
from app.models import Voter, Candidate


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_db():
    db = SessionLocal()
    try:

        Base.metadata.create_all(bind=engine)

        if db.query(Voter).count() == 0 and db.query(Candidate).count() == 0:
            
            voters = [
                Voter(name="Juan Pérez", email="juan@example.com"),
                Voter(name="María García", email="maria@example.com"),
                Voter(name="Luis Torres", email="luis@example.com"),
                Voter(name="Ana Martínez", email="ana@example.com"),
                Voter(name="Carlos Gómez", email="carlos@example.com"),
                Voter(name="Laura Ruiz", email="laura@example.com"),
                Voter(name="Jorge Herrera", email="jorge@example.com"),
                Voter(name="Camila Díaz", email="camila@example.com"),
                Voter(name="Santiago López", email="santiago@example.com"),
                Voter(name="Daniela Castro", email="daniela@example.com"),
                Voter(name="Felipe Ríos", email="felipe@example.com"),
                Voter(name="Valentina Ortiz", email="valentina@example.com"),
                Voter(name="Andrés Molina", email="andres@example.com"),
                Voter(name="Paula Navarro", email="paula@example.com"),
                Voter(name="Mateo Cárdenas", email="mateo@example.com"),
            ]

            
            candidates = [
                Candidate(name="Sofía Ramírez", party="Partido Verde"),
                Candidate(name="Pedro Sánchez", party="Partido Azul"),
                Candidate(name="Lucía Fernández", party="Partido Rojo"),
                Candidate(name="Miguel Ángel", party="Partido Amarillo"),
                Candidate(name="Diana Salazar", party="Partido Naranja"),
                Candidate(name="Andrés Pérez", party="Partido Independiente"),
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
