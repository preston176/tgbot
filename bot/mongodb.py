import pymongo
from bot import mongodb_uri, db_name

# connecting to db
client = pymongo.MongoClient(mongodb_uri)
db = client[db_name]

class MongoDB:
    def insert_single_data(collection_name, data):
        collection = db[collection_name]
        #ex. data = {"name": "John", "age": 30, "city": "New York"}

        try:
            print(f"Inserting Single Data in {collection_name} MongoDB...")
            inject = collection.insert_one(data)
            inserted_id = inject.inserted_id
            print("Inserted ID:", inserted_id)
            return inserted_id
        except Exception as e:
            print(f"Error (inserting db_data): {e}")


    def insert_multiple_data(collection_name, data_list):
        collection = db[collection_name]

        # ex. data = [
        #     { "name": "Alice", "age": 25, "city": "San Francisco" },
        #     { "name": "Bob", "age": 28, "city": "Seattle" },
        # ]

        try:
            print(f"Inserting Multiple Data in {collection_name} MongoDB...")
            inject = collection.insert_many(data_list)
            inserted_ids = inject.inserted_ids
            print("Inserted IDs:", inserted_ids)
            return inserted_ids
        except Exception as e:
            print(f"Error (inserting db_data): {e}")


    def find_one(collection_name, search, match):
        collection = db[collection_name]
        try:
            print(f"Finding Data in {collection_name} MongoDB...")
            document = collection.find_one({search: match})
            if document:
                print("Data Found: [DATA INFO HIDDEN BECASUE OF DATA PRIVACY]!!")
            else:
                print("Data Not Found!")
            return document
        except Exception as e:
            print(f"Error (finding db_data): {e}")
    

    def find(collection_name, search):
        collection = db[collection_name]
        try:
            print(f"Finding Data in {collection_name} MongoDB...")
            documents = collection.find({})
            storage = []
            if documents:
                for document in documents:
                    doc_value = document.get(search)
                    storage.append(doc_value)
                    print("Data Found: [DATA INFO HIDDEN BECASUE OF DATA PRIVACY]!!")
            return storage
        except Exception as e:
            print(f"Error (finding db_data): {e}")



    def get_data(collection_name, get_data):
        collection = db[collection_name]
        try:
            print(f"Getting Data from {collection_name} MongoDB...")
            documents = collection.find_one()
            data = documents.get(get_data)
            if data:
                print("Got Data: [DATA INFO HIDDEN BECASUE OF DATA PRIVACY]!!")
            else:
                print("Data Not Found!")
            return data
        except Exception as e:
            print(f"Error (Getting db_data): {e}")


    def update_db(collection_name, search, match, update_data_name, update_data_value):
        collection = db[collection_name]
        try:
            print(f"Updating {collection_name} MongoDB Data...")
            collection.update_one(
                {search: match},
                {"$set": {update_data_name: update_data_value}}
            )
            print(f"{collection_name} MongoDB DATA UPDATED !!")
        except Exception as e:
            print(f"Error (Updating db_data): {e}")


    def info_db(collection_name=None):
        docs_name = db.list_collection_names()
        if collection_name:
            if collection_name in docs_name:
                doc_stats = db.command("collstats", collection_name)
                # stats
                doc_name = collection_name
                doc_count = doc_stats['count']
                doc_size = f"{doc_stats['storageSize'] / (1024 * 1024):.2f} MB"
                doc_acsize = f"Actual Size: {doc_stats['size'] / (1024 * 1024):.2f} MB"
                return doc_name, doc_count, doc_size, doc_acsize
            else:
                print(f"{collection_name} Not found!!")
        else:
            storage = []
            for collection_name in docs_name:
                doc_stats = db.command("collstats", collection_name)
                # stats
                doc_name = collection_name
                doc_count = doc_stats['count']
                doc_size = f"{doc_stats['storageSize'] / (1024 * 1024):.2f} MB"
                doc_acsize = f"Actual Size: {doc_stats['size'] / (1024 * 1024):.2f} MB"
                storage.append((doc_name, doc_count, doc_size, doc_acsize))
            return storage


    def delete_all_doc(collection_name):
        collection = db[collection_name]
        try:
            print(f"{collection_name} Data deleting process started...")
            collection.delete_many({})
            print(f"{collection_name} Data Deleted!!")
        except Exception as e:
            print(f"Error (Deleting db_data): {e}")
