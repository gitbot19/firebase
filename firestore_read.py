from firestore import project
import firestore

db = project()
users_ref = db.collection(u'users')
docs = users_ref.stream()

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
    di = doc.to_dict()

print(di)
for key, value in di.items():
    print(key, ' : ',value)

doc_ref = db.collection(u'users').document(u'alovelace')

# get() method
doc = doc_ref.get()
if doc.exists:
    print(f'Document data: {doc.to_dict()}')
else:
    print(u'No such document!')