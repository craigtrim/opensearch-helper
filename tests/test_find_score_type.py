# !/usr/bin/env python
# -*- coding: UTF-8 -*-


from pprint import pprint

from opensearch_helper import top_hit
from opensearch_helper.dto import SearchScoreType
from opensearch_helper.dto import find_score_type


d_search_results = {
    "_shards": {
        "failed": 0,
        "skipped": 0,
        "successful": 5,
        "total": 5
    },
    "hits": {
        "hits": [
            {
                "_id": "1115",
                "_index": "clmt",
                "_score": 8.488908,
                "_source": {
                    "answer": [
                       "The pH of vinegar is 3."
                    ],
                    "chapter":6,
                    "context":[
                        "The pH of vinegar is 3."
                    ],
                    "page":9,
                    "question":"What is the pH of vinegar?"
                },
                "_type":"_doc"
            },
            {
                "_id": "1114",
                "_index": "clmt",
                "_score": 8.003047,
                "_source": {
                    "answer": [
                        "The pH of normal rain is 5.6."
                    ],
                    "chapter":6,
                    "context":[
                        "Normal rain has a pH of 5.6.\n Acid rain has a pH lower than this value, and can be as low as 3 (vinegar)."
                    ],
                    "page":9,
                    "question":"What is the pH of normal rain?"
                },
                "_type":"_doc"
            },
            {
                "_id": "3458",
                "_index": "clmt",
                "_score": 5.488017,
                "_source": {
                    "answer": [
                        "I cannot find the answer to your question in the textbook."
                    ],
                    "chapter":16,
                    "context":[
                        "There is no definitive answer to this question as it depends on a number of factors, such as the type of refrigerator, how well it is maintained, and the environment in which it is used. However, on average, most refrigerators have a lifespan of about 15 years."
                    ],
                    "page":16,
                    "question":"What is the average lifespan of a refrigerator?"
                },
                "_type":"_doc"
            },
            {
                "_id": "652",
                "_index": "clmt",
                "_score": 5.4357386,
                "_source": {
                    "answer": [
                        "The average temperature of the Universe is 2.7 Kelvin, and it primarily emits microwave radiation."
                    ],
                    "chapter":4,
                    "context":[
                        "The average temperature of the Universe is 2.7 Kelvin, and it primarily emits microwave radiation."
                    ],
                    "page":14,
                    "question":"What is the average temperature of the Universe?"
                },
                "_type":"_doc"
            },
            {
                "_id": "2687",
                "_index": "clmt",
                "_score": 5.21017,
                "_source": {
                    "answer": [
                        "The average temperature of Earth is 33°C."
                    ],
                    "chapter":12,
                    "context":[
                        "Earth's average temperature is 33°C.\n Mars' average temperature is minimal.\n Venus' average temperature is 735 K."
                    ],
                    "page":18,
                    "question":"What is the average temperature of Earth?"
                },
                "_type":"_doc"
            }
        ],
        "max_score": 8.488908,
        "total": {
            "relation": "eq",
            "value": 2317
        }
    },
    "timed_out": False,
    "took": 8
}


def test_function():

    d_top_hit = top_hit(d_search_results)
    pprint(d_top_hit)

    score_type = find_score_type(d_top_hit['_score'])
    print(f"Score: {d_top_hit['_score']}")
    print(f"Score Type: {score_type}")

    assert score_type == SearchScoreType.MEDIUM_LOW


def main():
    test_function()


if __name__ == "__main__":
    main()
