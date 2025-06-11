from fastapi import FastAPI
from .database import Base, engine
from .routers import voters, candidates, votes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Voting System API")

app.include_router(voters.router)
app.include_router(candidates.router)
app.include_router(votes.router)
