from sqlmodel import Field, MetaData, SQLModel
from typing import Optional


schema_name = 'tagger'
metadata = MetaData(schema=schema_name)

class Question(SQLModel, table=True):
    question_id: Optional[int] = Field(primary_key=True)
    topic_id: int
    question_type: str = Field(max_length=24)
    wording: str
    option_a: str
    option_b: str
    option_c: Optional[str] = None
    option_d: Optional[str] = None
    correct_option: str = Field(max_length=1)
    reasoning: Optional[str] = None
    is_validated: bool = Field(default=False)
    is_exam_ready: bool = Field(default=False)
    is_from_old_exam: bool = Field(default=False)
    metadata = metadata