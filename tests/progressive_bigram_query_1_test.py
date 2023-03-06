# !/usr/bin/env python
# -*- coding: UTF-8 -*-


from pprint import pprint


from opensearch_helper.dmo import progressive_bigram_query


def test_progressive_bigram_query():

    d_query = progressive_bigram_query(
        input_text='cloud-based core banking platforms')

    pprint(d_query)

    assert d_query == {
        "query": {
            "bool": {
                "should": [
                    {
                        "match_phrase_prefix": {
                            "text": {
                                "analyzer": "standard",
                                "boost": 1.0,
                                "max_expansions": 100,
                                "query": "banking platform"
                            }
                        }
                    },
                    {
                        "match_phrase_prefix": {
                            "text": {
                                "analyzer": "standard",
                                "boost": 2.0,
                                "max_expansions": 100,
                                "query": "core banking platform"
                            }
                        }
                    },
                    {
                        "match_phrase_prefix": {
                            "text": {
                                "analyzer": "standard",
                                "boost": 4.0,
                                "max_expansions": 100,
                                "query": "cloud-based core banking platform"
                            }
                        }
                    }
                ]
            }
        }
    }


def main():
    test_progressive_bigram_query()


if __name__ == "__main__":
    main()
