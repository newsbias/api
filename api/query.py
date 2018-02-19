from flask import *
from extensions import *
import math

query = Blueprint('query', __name__)

@query.route('/', methods=['GET'])
def query_route():
    try:
        w = float(request.args['w'])
        q = request.args['q']
    except KeyError:
        abort(400)

    raw_query = q.split()
    query = []

    # get query word information
    query_info = {}
    total_docs = {}
    for word in raw_query:
        word = word.lower()
        word = re.sub(r'[^a-zA-Z0-9]+', '', word)
        if not word or word in stopwords:
            continue
        else:
            query.append(word)

        # get tf, idf, and docs
        if word not in query_info:
            if word not in word_info:
                # word not in any docs
                return jsonify({'hits': []})
            query_info[word] = {
                'tf': 0,
                'idf': word_info[word]['idf'],
                'docs': {}
            }
            # number of query words in each doc
            for doc in word_info[word]['docs']:
                # docid -> [freq, norm]
                query_info[word]['docs'][doc[0]] = [doc[1], doc[2]]
                if doc[0] not in total_docs:
                    total_docs[doc[0]] = 0
                total_docs[doc[0]] += 1
        query_info[word]['tf'] += 1

    # get only valid documents
    valid_docs = []
    for doc, val in total_docs.items():
        if val == len(query_info):
            valid_docs.append(doc)

    # normalize query
    norm = 0
    query_vec = {}
    for word in query:
        query_vec[word] = query_info[word]['tf'] * query_info[word]['idf']
        norm += query_info[word]['tf'] ** 2 + query_info[word]['idf'] ** 2
    norm = math.sqrt(norm)

    # get results
    results = []
    for docid in valid_docs:
        num = 0
        for word in query:
            # docid -> [freq, norm]
            freq, doc_norm = query_info[word]['docs'][docid]
            idf = word_info[word]['idf']
            weight = idf * int(freq)
            num += weight * query_vec[word]

        den = float(doc_norm) * norm
        sim = num / den
        if docid not in pagerank:
            pagerank[docid] = 0
        score = w * pagerank[docid] + (1 - w) * sim
        results.append({'docid': docid, 'score': score})

    # sort and return query results
    results = sorted(results, key=lambda k: k["score"], reverse=True)
    return jsonify({'hits': results})
