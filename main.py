
import sys

from flask import escape
from google.cloud import firestore

# [START functions_write_firestore]
def write_firestore(request):

    request_json = request.get_json(silent=True)
    request_args = request.args
    db = firestore.Client()

    if request_json and 'value' in request_json:
        value = request_json['value']
        doc_ref = db.collection(u'data').document(u'test')
        doc_ref.set({
            u'value': value
        })

    elif request_args and 'value' in request_args:
        value = request_args['value']
        doc_ref = db.collection(u'data').document(u'test')
        doc_ref.set({
            u'value': value
        })
    else:
        value = 'NotValue'
    return 'Value write: {}'.format(escape(value))
# [END functions_write_firestore]


# [START functions_read_firestore]
def read_firestore(request):

    db = firestore.Client()
    collection_ref = db.collection(u'data')
    doc_ref = collection_ref.document(u'test')

    doc = doc_ref.get()
    if doc.exists:
        value = doc.to_dict()
    else:
        value = 'No such document!'

    return 'Value read: {}'.format(escape(value))
# [END functions_read_firestore]