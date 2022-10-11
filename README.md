# Open Search Helper (opensearch-helper)
A collection of methods for assisting with OpenSearch querying on AWS

## MultiMatch Query Generator

**Method Definition**
```python
multimatch_generator(input_text: str, size: int = 5, *args) -> MultiMatchQuery
```

**Invoke Function**

Pass in one-or-more field names after the query:
```python
from opensearch_helper import multimatch_generator

d_query = multimatch_generator("what is the average PH of rainwater?" "question", "context")
```

**Sample Output**
```json
{
   "size":5,
   "query":{
      "multi_match":{
         "query":"input_text",
         "fields":[
            "question"
         ]
      }
   }
}
```

## API Query
**Method Definition**
```python
query(d_query: MultiMatchQuery, index_name: str) -> OpenSearchResult
```

**Invoke Function**

The following environment variables must exist and be encrypted via `baseblock::Run-Encrypt`
1. OPENSEARCH_HOST
2. OPENSEARCH_REGION
3. OPENSEARCH_USERNAME
4. OPENSEARCH_PASSWORD

```python
from opensearch_helper import query

query(d_query, index_name='myindex')
```

## Score Top Hit
This method will retrieve the top hit and both quantitatively and qualitatively score the result.

**Method Definition**
```python
score_top_hit(d_hits: dict) -> ScoreResult
```

**Invoke Function**
```python
from opensearch_helper import score_top_hit

score_top_hit(d_hits)
```

**Sample Output**
```json
{
   "score":14.23432,
   "type":"HIGH"
}
```