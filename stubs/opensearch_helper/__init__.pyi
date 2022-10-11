from .bp import *
from .svc import *
from .dmo import *
from .dto import *
from .bp.opensearch_api import OpenSearchAPI
from .dto.typedefs import MultiMatchQuery as MultiMatchQuery, ScoreResult as ScoreResult
from _typeshed import Incomplete
from operator import index as index

class SingletonApi:
    def api(self) -> OpenSearchAPI: ...

sapi: Incomplete

def score_top_hit(d_hits: dict) -> ScoreResult: ...
def query(d_query: MultiMatchQuery, index_name: str) -> OpenSearchResult: ...
def multimatch_generator(input_text: str, size: int = ..., *args) -> MultiMatchQuery: ...
