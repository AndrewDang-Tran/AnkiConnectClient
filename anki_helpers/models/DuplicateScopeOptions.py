from typing import Dict, List
from dataclasses import dataclass

@dataclass(frozen = True)
class DuplicateScopeOptions:
    deckName: str
    checkChildren: bool
    checkAllModels: bool
