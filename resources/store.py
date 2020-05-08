from flask_restful import Resource
from model.store_model import StoreModel

class Store(Resource):
        def get(self, name):
            store = StoreModel.get_by_name(name)
            if store:
                return store.json()
            return {'message': f'Store with name {name} not found.'}, 404

        def post(self, name):
            if StoreModel.get_by_name(name):
                return {'message': f'Store with name {name} already exists.'}, 400

            store = StoreModel(name)
            try:
                store.save_to_db()
            except:
                return {'message': f'Error saving store'}, 500

            return store.json(), 201

        def delete(self, name):
            store = StoreModel.get_by_name(name)
            if store:
                store.delete_from_db()

            return {'message': f'Store {name} is no more'}, 500


class StoreList(Resource):
    def get(self):
        return {'stores': [st.json() for st in StoreModel.query.all()]}