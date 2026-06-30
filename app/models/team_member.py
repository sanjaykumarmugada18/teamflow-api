import uuid
import enum
from sqlalchemy import Column, DateTime, ForeignKey, Enum, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.db.database import Base

# Define the allowed roles
class TeamRole(str, enum.Enum):
    owner = "owner"
    admin = "admin"
    member = "member"

class TeamMember(Base):
    __tablename__ = "team_members"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    team_id = Column(UUID(as_uuid=True), ForeignKey("teams.id", ondelete="CASCADE"), nullable=False, index=True)
    
    role = Column(Enum(TeamRole), default=TeamRole.member, nullable=False)
    joined_at = Column(DateTime(timezone=True), server_default=func.now())

    # Prevent a user from joining the same team twice
    __table_args__ = (
        UniqueConstraint('user_id', 'team_id', name='uq_user_team'),
    )

    # Relationships linking back to the parent models
    user = relationship("User", back_populates="teams")
    team = relationship("Team", back_populates="members")