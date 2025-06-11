from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter(prefix="/voters", tags=["Voters"])

@router.post("/", response_model=schemas.Voter)
def create_voter(voter: schemas.VoterCreate, db: Session = Depends(database.get_db)):
    return crud.create_voter(db, voter)

@router.get("/", response_model=list[schemas.Voter])
def read_voters(db: Session = Depends(database.get_db)):
    return crud.get_voters(db)

@router.get("/{voter_id}", response_model=schemas.Voter)
def read_voter(voter_id: int, db: Session = Depends(database.get_db)):
    voter = crud.get_voter(db, voter_id)
    if not voter:
        raise HTTPException(status_code=404, detail="Voter not found")
    return voter

@router.delete("/{voter_id}")
def delete_voter(voter_id: int, db: Session = Depends(database.get_db)):
    voter = crud.delete_voter(db, voter_id)
    if not voter:
        raise HTTPException(status_code=404, detail="Voter not found")
    return {"message": "Voter deleted"}
