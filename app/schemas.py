from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional

class IssueStatus(str, Enum):
    
    open = "open"
    in_progress = "in_progress"
    closed = "closed"
    
class IssuePriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"