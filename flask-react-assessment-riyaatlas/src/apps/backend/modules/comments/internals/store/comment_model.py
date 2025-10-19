from dataclasses import dataclass, asdict
from datetime import datetime
from typing import Optional

from modules.application.base_model import BaseModel

@dataclass
class CommentModel(BaseModel):
    id: Optional[str]
    task_id: str
    account_id: str
    content: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    @staticmethod
    def get_collection_name() -> str:
        return "comments"
