# !/usr/bin/env python
# -*- coding: UTF-8 -*-


from pprint import pprint


from opensearch_helper.dmo import ConfidenceCompute


def test_no_results():

    compute = ConfidenceCompute().process
    assert compute

    no_results = {
        "took": 2,
        "timed_out": False,
        "_shards": {
            "total": 1,
            "successful": 1,
            "skipped": 0,
            "failed": 0
        },
        "hits": {
            "total": {
                "value": 0,
                "relation": "eq"
            },
            "max_score": None,
            "hits": []
        }
    }

    assert compute(no_results) == no_results


def test_results():

    compute = ConfidenceCompute().process
    assert compute

    results = {
        "took": 2,
        "timed_out": False,
        "_shards": {
            "total": 1,
            "successful": 1,
            "skipped": 0,
            "failed": 0
        },
        "hits": {
            "total": {
                "value": 4,
                "relation": "eq"
            },
            "max_score": 8.828966,
            "hits": [
                {
                    "_index": "trends_summaries",
                    "_id": "jdvoGoYBwVxr156y_CZk",
                    "_score": 8.828966,
                    "_source": {
                        "id": 10913,
                    }
                },
                {
                    "_index": "trends_summaries",
                    "_id": "6NvoGoYBwVxr156y_CJj",
                    "_score": 6.765611,
                    "_source": {
                        "id": 9980,
                    }
                },
                {
                    "_index": "trends_summaries",
                    "_id": "advoGoYBwVxr156y_Ati",
                    "_score": 4.07501,
                    "_source": {
                        "id": 3965,
                    }
                },
                {
                    "_index": "trends_summaries",
                    "_id": "69voGoYBwVxr156y_CJj",
                    "_score": 3.7193546,
                    "_source": {
                        "id": 9983,
                    }
                }
            ]
        }
    }

    assert compute(results) == {
        "took": 2,
        "timed_out": False,
        "_shards": {
            "failed": 0,
            "skipped": 0,
            "successful": 1,
            "total": 1
        },
        "hits": {
            "total": {
                "relation": "eq",
                "value": 4
            },
            "max_score": 8.828966,
            "hits": [
                {
                    "_id": "jdvoGoYBwVxr156y_CZk",
                    "_index": "trends_summaries",
                    "_score": 8.828966,
                    "_source": {
                        "id": 10913
                    },
                    "confidence": 100
                },
                {
                    "_id": "6NvoGoYBwVxr156y_CJj",
                    "_index": "trends_summaries",
                    "_score": 6.765611,
                    "_source": {
                        "id": 9980
                    },
                    "confidence": 77
                },
                {
                    "_id": "advoGoYBwVxr156y_Ati",
                    "_index": "trends_summaries",
                    "_score": 4.07501,
                    "_source": {
                        "id": 3965
                    },
                    "confidence": 46
                },
                {
                    "_id": "69voGoYBwVxr156y_CJj",
                    "_index": "trends_summaries",
                    "_score": 3.7193546,
                    "_source": {
                        "id": 9983
                    },
                    "confidence": 42
                }
            ],
        },
    }


def main():
    test_no_results()
    test_results()


if __name__ == "__main__":
    main()
