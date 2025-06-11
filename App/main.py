from .database import Base, engine
from .routers import voters, candidates, votes
from fastapi import FastAPI

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Voting System API")

App.include_router(voters.routers)
App.include_router(candidates.routers)
App.include_router(votes.routers)
