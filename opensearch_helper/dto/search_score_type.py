# !/usr/bin/env python
# -*- coding: UTF-8 -*-
""" Classification Type """


from enum import Enum


class SearchScoreType(Enum):

    # Use a 5-Point Likhert Scale

    HIGH = 5
    MEDIUM_HIGH = 4
    MEDIUM = 3
    MEDIUM_LOW = 4
    LOW = 5

    UNKNOWN = 0


def find_score_type(score: float) -> SearchScoreType:
    """ Put a Quantitative Score into a Qualitative Bucket for more consistent downstream decision making

    Args:
        d_opensearch_result (dict): an OpenSearch result

    Returns:
        SearchScoreType: the proper enum value
    """
    if score is None or type(score) != float:
        return SearchScoreType.UNKNOWN

    # 20221010; these buckets are entirely anecdotal and heuristic
    #           I have noticed <5 is irrelevant and ~20 is on point, but that's about it

    if score < 5:
        return SearchScoreType.LOW

    if score < 7.5:
        return SearchScoreType.MEDIUM_LOW

    if score < 10:
        return SearchScoreType.MEDIUM

    if score < 14:
        return SearchScoreType.MEDIUM_HIGH

    # highly relevant == 14.844854
    return SearchScoreType.HIGH
