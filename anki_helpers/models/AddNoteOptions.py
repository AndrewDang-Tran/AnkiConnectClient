from typing import Dict, List
from dataclasses import dataclass
from .DuplicateScopeOptions import DuplicateScopeOptions

@dataclass(frozen = True)
class AddNoteOptions:
    allowDuplicate: str
    duplicateScope: str
    duplicateScopeOptions: DuplicateScopeOptions
