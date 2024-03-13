from sqlmodel import Field, MetaData, SQLModel
from typing import Optional


schema_name = 'tagger'
metadata = MetaData(schema=schema_name)

class Subject(SQLModel, table=True):
    subject_id: Optional[int] = Field(default=None, primary_key=True)
    subject_name: str
    description: str
    study_id: Optional[int] = Field(default=None, primary_key=True)
    metadata = metadata