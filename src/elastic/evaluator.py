import pytrec_eval
from elastic.elastic_query import Queries
from settings.settings import QREL_FIELD, TEST_FIELDS, TEST_FIELD_VALUES


def evaluate(weights: list):
    imaginaryCorrectWeights = [12, 2, 110, 18]
    diff = 0
    for i in range(4):
        diff += imaginaryCorrectWeights[i] - weights[i]
    return diff


def evaluate(weights: list):
    query = build_query(weights)
    correct_answer = Queries.weighted_search(query, QREL_FIELD)
    qrel_dic = build_trec_dic(correct_answer)
    retrieved_result = Queries.multi_field_weighted_search(query, TEST_FIELDS)
    result_dic = build_trec_dic(retrieved_result)
    evaluator = pytrec_eval.RelevanceEvaluator(qrel_dic, {'map', 'ndcg'})
    evaluated_dic = evaluator.evaluate(result_dic)["query"]
    return evaluated_dic["map"] * evaluated_dic["ndcg"]


def test_evaluate(weights: list):
    query = build_query(weights)
    correct_answer = Queries.weighted_search(query, QREL_FIELD)
    qrel_dic = build_trec_dic(correct_answer)
    evaluator = pytrec_eval.RelevanceEvaluator(qrel_dic, {'map', 'ndcg'})
    return evaluator.evaluate(qrel_dic)


def build_trec_dic(docs):
    trec_dic = {
        'query': dict()
    }
    for rank, doc in enumerate(docs):
        trec_dic['query'][doc['_id']] = rank
    return trec_dic


def build_query(weights: list):
    if len(TEST_FIELD_VALUES) != len(weights):
        raise Exception(f"weights and qrel fields values length don't match: received {weights}")
    return ' '.join([f'({TEST_FIELD_VALUES[i]})^{weights[i]}' for i in range(len(TEST_FIELD_VALUES))])
