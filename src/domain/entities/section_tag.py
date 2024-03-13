from sqlmodel import Field, MetaData, SQLModel
from typing import Optional


schema_name = 'tagger'
metadata = MetaData(schema=schema_name)

class Section_tag(SQLModel, table=True):
    section_id: Optional[int] = Field(primary_key=True, foreign_key="section.section_id")
    tag_id: Optional[int] = Field(primary_key=True, foreign_key="tag.tag_id")
    metadata = metadata