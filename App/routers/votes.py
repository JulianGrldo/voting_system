from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter(prefix="/votes", tags=["Votes"])

@router.post("/", response_model=schemas.VoteOut)
def vote(vote: schemas.VoteCreate, db: Session = Depends(database.get_db)):
    try:
        return crud.create_vote(db, vote)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[schemas.VoteOut])
def read_votes(db: Session = Depends(database.get_db)):
    return crud.get_all_votes(db)

@router.get("/statistics", response_model=schemas.VotingSummary)
def statistics(db: Session = Depends(database.get_db)):
    return crud.get_statistics(db)
