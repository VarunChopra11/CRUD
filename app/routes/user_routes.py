from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from services.user_services import UserService
from models.user_model import UserSchema

# Blueprint for user routes
user_bp = Blueprint('user', __name__)

#Route to create a new user
@user_bp.route('/users', methods=['POST'])
def create_user():
    try:
        schema = UserSchema()
        data = schema.load(request.json)
        user_data = UserService.create_user(data)
        print("............User Created............")
        print("User created successfully!", user_data)
        return jsonify({"message": "User created successfully!"}), 201
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#Route to get all users
@user_bp.route('/users', methods=['GET'])
def get_all_users():
    try:
        user_list = UserService.get_all_users()
        return jsonify(user_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#Route to get a user by id
@user_bp.route('/users/<id>', methods=['GET'])
def get_user_by_id(id):
    try:
        user_data = UserService.get_user_by_id(id)
        return jsonify(user_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#Route to update a user by id
@user_bp.route('/users/<id>', methods=['PUT'])
def update_user(id):
    try:
        status = UserService.update_user(id, request.json)
        if status:
            return jsonify({"message": "User updated successfully!"}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#Route to delete a user by id
@user_bp.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        result = UserService.delete_user(id)
        if result.deleted_count == 1:
            return jsonify({"message": "User deleted successfully!"}), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
