from baseblock import BaseObject
from opensearch_helper.dto import MultiMatchQuery as MultiMatchQuery, OpenSearchResult as OpenSearchResult
from opensearch_helper.svc import QueryOpenSearch as QueryOpenSearch

class OpenSearchAWS(BaseObject):
    def __init__(self): ...
    def query(self, d_query: MultiMatchQuery, index_name: str) -> OpenSearchResult: ...
