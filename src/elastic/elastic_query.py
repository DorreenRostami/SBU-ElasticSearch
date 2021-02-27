from elasticsearch import Elasticsearch

from settings.settings import INDEX_NAME


class Queries:
    es = Elasticsearch()

    @classmethod
    def initiateMethod(self, question_number, section_number, match_query):
        print("============================================")
        print(
            f"This is answer to {question_number} question in section {section_number}")
        print(f"Search for: {match_query}")

    @classmethod
    def printResult(cls, res):
        print("Got %d Hits:" % res['hits']['total']['value'])
        for hit in res['hits']['hits']:
            tmp = str(hit["_score"])
            print(
                "Title: %(Title)s: News_url: %(Short_Link)s Score: " % hit["_source"] + tmp)

    @classmethod
    def customSearch(cls, query_text, fields):

        cls.initiateMethod("Custom", "Custom", query_text)
        res = cls.es.search(index=INDEX_NAME, body={"query": {
            "multi_match": {
                "query": query_text,
                "fields": fields
            }
        }, "suggest": {"text": query_text,
                       "simple_phrase": {
                           "phrase": {
                               "field": "Body.trigram",
                               "size": 1,
                               "gram_size": 3,
                               "direct_generator": [{
                                   "field": "Body.trigram",
                                   "suggest_mode": "always"
                               }],
                               "highlight": {
                                   "pre_tag": "<em>",
                                   "post_tag": "</em>"
                               }
                           }
                       }
                       }})
        Queries.printResult(res)
        return res

    @classmethod
    def weighted_search(cls, query, field):
        return cls.es.search(index=INDEX_NAME, body={
            "query": {
                "match": {
                    field: query
                }
            },
            "size": 10
        })['hits']['hits']

    @classmethod
    def multi_field_weighted_search(cls, query, fields):
        return cls.es.search(index=INDEX_NAME, body={
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": fields
                }
            },
            'size': 10
        })['hits']['hits']

    @classmethod
    def customSearchByTermSugestion(cls, query_text, indexname, fields, question_numberr
                                    ):
        print(f"Search for: {query_text}")
        res = cls.es.search(index=INDEX_NAME, body={"query": {
            "multi_match": {
                "query": query_text,
                "fields": fields

            }
        }, "suggest": {
            "text": query_text,
            "my-suggest-1": {
                "term": {
                    "suggest_mode": "always",
                    "analyzer": "standard",
                    "field": fields[0]
                }
            }
        }})
        print("This is answer to question " + question_numberr)
        Queries.printSuggestion(res)
        Queries.printResult(res)
        print("=========================================================================")
        return res

    @classmethod
    def printSuggestion(cls, result):
        print("Suggetion per term:")
        for term in result['suggest']['my-suggest-1']:
            arr = []
            for suggested_term in term['options']:
                arr.append(suggested_term['text'])
            if len(term['options']) != 0:
                print(f"Term:{term['text']} Suggestions:{arr}")
