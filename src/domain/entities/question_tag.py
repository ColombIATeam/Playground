from sqlmodel import Field, MetaData, SQLModel
from typing import Optional


schema_name = 'tagger'
metadata = MetaData(schema=schema_name)

class Question_Tag(SQLModel, table=True):
    question_id: Optional[int] = Field(primary_key=True, foreign_key="question.question_id")
    tag_id: Optional[int] = Field(primary_key=True, foreign_key="tag.tag_id")
    metadata = metadata