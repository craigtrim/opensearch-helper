from baseblock import BaseObject
from opensearch_helper.dto import ScoreResult as ScoreResult

class ScoreTopHit(BaseObject):
    def __init__(self) -> None: ...
    def process(self, d_hits: dict) -> ScoreResult: ...