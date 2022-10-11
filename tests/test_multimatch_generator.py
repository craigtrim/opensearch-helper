# !/usr/bin/env python
# -*- coding: UTF-8 -*-


from pprint import pprint


from opensearch_helper import multimatch_generator


def test_service():

    input_text = "What is the PH of rain"
    d_query = multimatch_generator(input_text, 'question')

    assert d_query == {
        "size": 5,
        "query": {
            "multi_match": {
                "query": "What is the PH of rain",
                "fields": [
                    "question"
                ],
            }
        }
    }


def main():
    test_service()


if __name__ == "__main__":
    main()
