from baseblock import BaseObject
from opensearch_helper.dto import MultiMatchQuery as MultiMatchQuery, OpenSearchResult as OpenSearchResult

class OpenSearchAPI(BaseObject):
    def __init__(self): ...
    def query(self, d_query: MultiMatchQuery, index_name: str) -> OpenSearchResult: ...
