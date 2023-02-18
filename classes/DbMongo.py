import pymongo
import os

class DbMongo:

    @staticmethod
    def getDB():
        user = os.environ['mariafernandaocon']
        password = os.environ['sakurita']
        cluster = os.environ['cluster0.aovexi6.mongodb.net']
        query_string = 'retryWrites=true&w=majority'

        ##conecction string
        uri = "mongodb+srv://{0}:{1}@{2}/?{3}".format(
            user
            , password
            , cluster
            , query_string
        )

        client = pymongo.MongoClient(uri)
        print(uri)
        db = client[os.environ['unah']]

        return client, db