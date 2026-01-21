from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum
from database import Base
from datetime import datetime

class StatusEnum(enum.Enum):
    accepted = "Accepted"
    wrong_answer = "Wrong Answer"
    runtime_error = "Runtime Error"
    time_limit_exceeded = "Time Limit Exceeded"
    memory_limit_exceeded = "Memory Limit Exceeded"
    compile_error = "Compile Error"
    
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)

class Problem(Base):
    __tablename__ = "problems"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    frontend_id = Column(Integer, unique=True, index=True)
    difficulty = Column(String, nullable=True)
    submissions = relationship("Submission", back_populates="problem")

class Submission(Base):
    __tablename__ = "submissions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    problem_id = Column(Integer, ForeignKey("problems.id"))
    code = Column(Text)
    status = Column(Enum(StatusEnum))
    runtime = Column(String, nullable=True)
    memory = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="submissions")
    problem = relationship("Problem", back_populates="submissions")

class AIFeedback(Base):
    __tablename__ = "ai_feedback"
    id = Column(Integer, primary_key=True, index=True)
    submission_id = Column(Integer, ForeignKey("submissions.id"))
    feedback = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)