from .bp import *
from .svc import *
from .dmo import *
from .dto import *
from .bp.opensearch_aws import OpenSearchAWS
from .bp.opensearch_dev import OpenSearchDEV as OpenSearchDEV
from .dto.typedefs import MultiMatchQuery as MultiMatchQuery, ScoreResult as ScoreResult
from _typeshed import Incomplete

class SingletonApi:
    def api(self) -> OpenSearchAWS: ...

sapi: Incomplete

def top_hit(d_hits: dict) -> dict: ...
def score_top_hit(d_top: dict) -> ScoreResult: ...
def query(d_query: MultiMatchQuery, index_name: str) -> OpenSearchResult: ...
def multimatch_generator(input_text: str, *args) -> MultiMatchQuery: ...
