from typing import Any, Dict, List, Optional, TypedDict

class MultiMatchInner2(TypedDict):
    query: str
    fields: List[str]

class MultiMatchInner1(TypedDict):
    multi_match: MultiMatchInner2

class MultiMatchQuery(TypedDict):
    size: int
    query: MultiMatchInner1

class OpenSearchResult(TypedDict):
    response: Dict[str, Any]
    events: List[Dict[str, Any]]

class ScoreResult(TypedDict):
    score: float
    type: Optional[str]

class CreateIndexResult(TypedDict):
    acknowledged: bool
    shards_acknowledged: bool
    index: str

class AddDocumentShardsResult(TypedDict):
    total: int
    successful: int
    failed: int

class AddDocumentResult(TypedDict):
    result: str
    forced_refresh: bool
