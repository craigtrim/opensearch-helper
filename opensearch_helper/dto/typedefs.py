#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Define Strict Types for the Project """


from typing import Any
from typing import List
from typing import Dict
from typing import Optional
from typing import TypedDict


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
    _index: str
    _id: str
    _version: int
    result: str
    forced_refresh: bool
    _shards: AddDocumentShardsResult
    _seq_no: int
    _primary_term: int
