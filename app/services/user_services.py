from werkzeug.security import generate_password_hash
from bson import ObjectId
from database import mongo

class UserService:
    @staticmethod
    def create_user(data):
        data['password'] = generate_password_hash(data['password'])
        data['_id'] = ObjectId(data['id'])
        print({
            "id": data['_id'],
            "name": data['name'],
            "email": data['email'],
            "password": data['password']
        })
        mongo.db.users.insert_one(data) 
        return data
    
    @staticmethod
    def get_all_users():
        users = mongo.db.users.find()
        if users:
            user_list = [{
                "id": str(user["_id"]),
                "name": user["name"],
                "email": user["email"]
            } for user in users]
            return user_list
        else:
            raise Exception("No users found")
    
    @staticmethod
    def get_user_by_id(id):
        user = mongo.db.users.find_one({"_id": ObjectId(id)})
        if user:
            user_data = {
                "id": str(user["_id"]),
                "name": user["name"],
                "email": user["email"]  #Password is not returned for security reasons :)
            }
            return user_data
        else:
            raise Exception("User not found")
        
    @staticmethod
    def update_user(id, data):
        user = mongo.db.users.find_one({"_id": ObjectId(id)})
        if user:
            if "password" in data:
                data["password"] = generate_password_hash(data["password"])
            
            mongo.db.users.update_one({"_id": ObjectId(id)}, {"$set": data})
            return True
        else:
            raise Exception("User not found")
        
    @staticmethod
    def delete_user(id):
        result = mongo.db.users.delete_one({"_id": ObjectId(id)})
        return result
    

  