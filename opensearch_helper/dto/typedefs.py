#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Define Strict Types for the Project """


from typing import Any
from typing import List
from typing import Dict
from typing import Tuple
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
