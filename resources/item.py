from flask_jwt import jwt_required
from flask_restful import Resource, reqparse

from model.item_model import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,
                        required=True,
                        help='This field cannot be left blank')

    parser.add_argument('store_id',
                        type=int,
                        required=True,
                        help='Every item needs a store id')

    @jwt_required()
    def get(self, name):
        item = ItemModel.get_by_name(name)
        if item:
            return item.json()
        return {'message': 'No item was found'}, 404

    # @jwt_required()
    def post(self, name):
        if ItemModel.get_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, **data)   # data['price'], data['store_id'])
        try:
            item.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item'}, 500  # Internal server error

        return item.json(), 201  # returning json

    # @jwt_required()
    def delete(self, name):
        item = ItemModel.get_by_name(name)
        if item:
            item.delete_from_db()
            return {'message':f'{name} was deleted from the database'}
        return {'message':f'{name} was not found in the database'}

    # @jwt_required()
    def put(self, name):
        data = self.parser.parse_args()
        item = ItemModel.get_by_name(name)
        if item is None:
            item = ItemModel(name, **data)  # data['price'], data['store_id'])
        else:
            item.price = data['price']
            item.store_id = data['store_id']
        try:
            item.save_to_db()
        except:
            return {'message': 'An error occurred saving the item'}, 500  # Internal server error

        return item.json()


class ItemList(Resource):
    def get(self):
        return {'items': [itm.json() for itm in ItemModel.query.all()]}