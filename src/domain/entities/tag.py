from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, MetaData, SQLModel


if TYPE_CHECKING: pass
SCHEMA_NAME = "tagger"
metadata = MetaData(schema=SCHEMA_NAME)

class Tag(SQLModel, table=True):
    tag_id: Optional[int] = Field(default=None, primary_key=True)
    tag_name: str
    tag_type: Optional[str]
    tag_description: Optional[str] = None
    metadata = metadata
    def __eq__(self, other):
        if not isinstance(other, Tag):
            return False
        return (
            self.tag_id == other.tag_id 
            and self.tag_name == other.tag_name 
            and self.tag_type == other.tag_type 
            and self.tag_description == other.tag_description
        )