from baseblock import BaseObject, Stopwatch as Stopwatch
from opensearch_helper.dto import MultiMatchQuery as MultiMatchQuery, OpenSearchResult as OpenSearchResult
from opensearch_helper.svc import QueryOpenSearch as QueryOpenSearch
from opensearchpy import AWSV4SignerAuth as AWSV4SignerAuth, RequestsHttpConnection as RequestsHttpConnection

class OpenSearchDEV(BaseObject):
    def __init__(self): ...
    def query(self, d_query: MultiMatchQuery, index_name: str) -> OpenSearchResult: ...
