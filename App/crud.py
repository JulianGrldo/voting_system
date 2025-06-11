from . import models, schemas
from sqlalchemy.orm import Session


# Voter CRUD
def create_voter(db: Session, voter: schemas.VoterCreate):
    db_voter = models.Voter(**voter.dict())
    db.add(db_voter)
    db.commit()
    db.refresh(db_voter)
    return db_voter

def get_voter(db: Session, voter_id: int):
    return db.query(models.Voter).filter(models.Voter.id == voter_id).first()

def get_voters(db: Session):
    return db.query(models.Voter).all()

def delete_voter(db: Session, voter_id: int):
    db_voter = get_voter(db, voter_id)
    if db_voter:
        db.delete(db_voter)
        db.commit()
    return db_voter

# Candidate CRUD
def create_candidate(db: Session, candidate: schemas.CandidateCreate):
    db_candidate = models.Candidate(**candidate.dict())
    db.add(db_candidate)
    db.commit()
    db.refresh(db_candidate)
    return db_candidate



def get_candidates(db: Session):
    return db.query(models.Candidate).all()

def get_candidate(db: Session, candidate_id: int):
    return db.query(models.Candidate).filter(models.Candidate.id == candidate_id).first()

def delete_candidate(db: Session, candidate_id: int):
    db_candidate = get_candidate(db, candidate_id)
    if db_candidate:
        db.delete(db_candidate)
        db.commit()
    return db_candidate

# Votes
def create_vote(db: Session, vote_data: schemas.VoteCreate):
    voter = get_voter(db, vote_data.voter_id)
    candidate = get_candidate(db, vote_data.candidate_id)
    if not voter or not candidate:
        raise ValueError("Voter or candidate not found")
    if voter.has_voted:
        raise ValueError("Voter has already voted")

    vote = models.Vote(voter_id=voter.id, candidate_id=candidate.id)
    voter.has_voted = True
    candidate.votes += 1

    db.add(vote)
    db.commit()
    db.refresh(vote)
    return vote

def get_all_votes(db: Session):
    return db.query(models.Vote).all()

def get_statistics(db: Session):
    total_votes = db.query(models.Vote).count()
    candidates = db.query(models.Candidate).all()
    stats = []
    for candidate in candidates:
        percent = (candidate.votes / total_votes * 100) if total_votes > 0 else 0
        stats.append(schemas.VoteStatistics(
            candidate_id=candidate.id,
            candidate_name=candidate.name,
            votes=candidate.votes,
            percentage=round(percent, 2)
        ))
    total_voters_voted = db.query(models.Voter).filter(models.Voter.has_voted == True).count()
    return schemas.VotingSummary(statistics=stats, total_voters_voted=total_voters_voted)
