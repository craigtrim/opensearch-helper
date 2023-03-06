# !/usr/bin/env python
# -*- coding: UTF-8 -*-


from pprint import pprint


from opensearch_helper.dmo import multi_phrase_prefix


def test_multi_phrase_prefix():

    d_query = multi_phrase_prefix(
        terms=['video game', 'netflix'],
        stem_terms=True)

    pprint(d_query)

    assert d_query == {
        "query": {
            "bool": {
                "must": [
                    {
                        "match_phrase_prefix": {
                            "text": {
                                "analyzer": "standard",
                                "max_expansions": 100,
                                "query": "video gam"
                            }
                        }
                    },
                    {
                        "match_phrase_prefix": {
                            "text": {
                                "analyzer": "standard",
                                "max_expansions": 100,
                                "query": "netflix"
                            }
                        }
                    }
                ]
            }
        }
    }


def main():
    test_multi_phrase_prefix()


if __name__ == "__main__":
    main()
