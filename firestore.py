from google.cloud import firestore

def project():
    project_id = 'bunny-5d019'
    db = firestore.Client(project=project_id)
    return db

def add():
    db = project()
    doc_ref = db.collection(u'users').document(u'alovelace')
    doc_ref.set({
        u'first': u'Ada',
        u'last': u'Lovelace',
        u'born': 1815
    })