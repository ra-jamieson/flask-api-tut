from flask_restful import Resource, reqparse

from model.user_model import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help='This field cannot be left blank')
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This field cannot be left blank')

    def post(self):
        data = UserRegister.parser.parse_args()

        return_msg = 'User created successfully'
        # Enforce unique username's
        if UserModel.find_by_username(data['email']):
            return_msg = f"Account using {data['email']} already exists. "

        else:
            user = UserModel(data['email'], data['password'])
            user.save_to_db()

        return {'message':return_msg}, 201