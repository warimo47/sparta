from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 한 개 찾기 - 예시
metrix = db.movies.find_one({'title': '매트릭스'})

sameStars = list(db.movies.find({'star': metrix['star']}, {'_id': False}))

for ss in sameStars:
    print(ss['title'])


db.movies.update_one({'title': '매트릭스'}, {'$set': {'star': '0'}})


