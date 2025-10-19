from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Comment:
    id: Optional[str]
    task_id: str
    account_id: str
    content: str
    created_at: Optional[datetime] = datetime.now()
    updated_at: Optional[datetime] = datetime.now()

@dataclass
class CreateCommentParams:
    task_id: str
    account_id: str
    content: str

@dataclass
class UpdateCommentParams:
    content: str
