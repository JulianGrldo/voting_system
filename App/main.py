from .database import Base, engine
from .routers import voters, candidates, votes
from fastapi import FastAPI

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Voting System API")

app.include_router(voters.routers)
app.include_router(candidates.routers)
app.include_router(votes.routers)
