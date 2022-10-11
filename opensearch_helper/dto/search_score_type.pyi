from enum import Enum

class SearchScoreType(Enum):
    HIGH: int
    MEDIUM_HIGH: int
    MEDIUM: int
    MEDIUM_LOW: int
    LOW: int
    UNKNOWN: int

def find_score_type(score: float) -> SearchScoreType: ...
