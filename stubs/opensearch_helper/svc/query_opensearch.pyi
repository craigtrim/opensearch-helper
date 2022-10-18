from baseblock import BaseObject
from opensearch_helper.dto import MultiMatchQuery as MultiMatchQuery, OpenSearchResult as OpenSearchResult
from opensearchpy import OpenSearch

class QueryOpenSearch(BaseObject):
    def __init__(self, client: OpenSearch) -> None: ...
    def query(self, d_query: MultiMatchQuery, index_name: str) -> OpenSearchResult: ...
