from elasticsearch import Elasticsearch
from elasticsearch import helpers
from elastic import utility
from pathlib import Path
from settings.settings import INDEX_NAME, DATA_PATH


def build_index():
    es = Elasticsearch()
    # jj = es.indices.analyze

    if es.indices.exists(index=INDEX_NAME):
        print("Starting to delete previous index ...")
        es.indices.delete(index=INDEX_NAME)
        print("Index was deleted succesfully!")
    print("Starting to index ducuments ...")
    # We can specify Analyzer by Mapping or while creating index
    es.indices.create(index=INDEX_NAME, body={"mappings": {
        "properties": {
            "Body": {
                "type": "text",
                "analyzer": "parsi"
            },
            "Title": {
                "type": "text",
                "analyzer": "parsi"
            }
        }
    }})

    docs = utility.convertToArrayDictionary(Path(DATA_PATH))[:10]

    # for i in range(0, len(docs)):
    #     es.index(index=INDEX_NAME,
    #              id=i, body=docs[i])

    actions = [
        {
            "_index": INDEX_NAME,
            "_source": news
        }
        for news in docs]

    helpers.bulk(es, actions)

    print("Index was created succesfully!")

