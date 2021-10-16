from typing import Dict, List
from dataclasses import dataclass
from .AddNoteOptions import AddNoteOptions

@dataclass(frozen = True)
class AddNoteRequest:
    deckName: str
    modelName: str
    fields: Dict[str, str]
    tags: List[str]
    options: AddNoteOptions

