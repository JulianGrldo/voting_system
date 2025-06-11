import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status
from . import models, schemas

logger = logging.getLogger(__name__)

# Voter CRUD Operations
def create_voter(db: Session, voter: schemas.VoterCreate):
    try:
        # Check if email already exists
        existing_voter = db.query(models.Voter).filter(models.Voter.email == voter.email).first()
        if existing_voter:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
            
        db_voter = models.Voter(**voter.dict())
        db.add(db_voter)
        db.commit()
        db.refresh(db_voter)
        return db_voter
        
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Database error while creating voter: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create voter"
        )
    except Exception as e:
        db.rollback()
        logger.error(f"Unexpected error while creating voter: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred"
        )

def get_voter(db: Session, voter_id: int):
    try:
        voter = db.query(models.Voter).filter(models.Voter.id == voter_id).first()
        if not voter:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Voter not found"
            )
        return voter
    except SQLAlchemyError as e:
        logger.error(f"Database error while fetching voter: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch voter"
        )

def get_voters(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(models.Voter).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        logger.error(f"Database error while fetching voters: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch voters"
        )

def delete_voter(db: Session, voter_id: int):
    try:
        db_voter = get_voter(db, voter_id)
        if db_voter:
            db.delete(db_voter)
            db.commit()
        return db_voter
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Database error while deleting voter: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete voter"
        )

# Candidate CRUD Operations
def create_candidate(db: Session, candidate: schemas.CandidateCreate):
    try:
        db_candidate = models.Candidate(**candidate.dict())
        db.add(db_candidate)
        db.commit()
        db.refresh(db_candidate)
        return db_candidate
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Database error while creating candidate: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to create candidate"
        )

def get_candidate(db: Session, candidate_id: int):
    try:
        candidate = db.query(models.Candidate).filter(models.Candidate.id == candidate_id).first()
        if not candidate:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Candidate not found"
            )
        return candidate
    except SQLAlchemyError as e:
        logger.error(f"Database error while fetching candidate: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch candidate"
        )

def get_candidates(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(models.Candidate).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        logger.error(f"Database error while fetching candidates: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch candidates"
        )

def delete_candidate(db: Session, candidate_id: int):
    try:
        db_candidate = get_candidate(db, candidate_id)
        if db_candidate:
            db.delete(db_candidate)
            db.commit()
        return db_candidate
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Database error while deleting candidate: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete candidate"
        )

# Vote Operations
def create_vote(db: Session, vote_data: schemas.VoteCreate):
    try:
        voter = get_voter(db, vote_data.voter_id)
        candidate = get_candidate(db, vote_data.candidate_id)
        
        if not voter or not candidate:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Voter or candidate not found"
            )
            
        if voter.has_voted:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Voter has already voted"
            )

        vote = models.Vote(voter_id=voter.id, candidate_id=candidate.id)
        voter.has_voted = True
        candidate.votes += 1

        db.add(vote)
        db.commit()
        db.refresh(vote)
        return vote
        
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Database error while creating vote: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to register vote"
        )

def get_all_votes(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(models.Vote).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        logger.error(f"Database error while fetching votes: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch votes"
        )

def get_statistics(db: Session):
    try:
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
        
    except SQLAlchemyError as e:
        logger.error(f"Database error while fetching statistics: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to generate voting statistics"
        )
