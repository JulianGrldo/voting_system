from typing import Optional
from pydantic import BaseModel, EmailStr


class VoterBase(BaseModel):
    name: str
    email: EmailStr

class VoterCreate(VoterBase):
    pass

class Voter(VoterBase):
    id: int
    has_voted: bool

    class Config:
        orm_mode = True

class CandidateBase(BaseModel):
    name: str
    party: Optional[str] = None

class CandidateCreate(CandidateBase):
    pass

class Candidate(CandidateBase):
    id: int
    votes: int

    class Config:
        orm_mode = True

class VoteCreate(BaseModel):
    voter_id: int
    candidate_id: int

class VoteOut(BaseModel):
    id: int
    voter_id: int
    candidate_id: int

    class Config:
        orm_mode = True

class VoteStatistics(BaseModel):
    candidate_id: int
    candidate_name: str
    votes: int
    percentage: float

class VotingSummary(BaseModel):
    statistics: list[VoteStatistics]
    total_voters_voted: int
