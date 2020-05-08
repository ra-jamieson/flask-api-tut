from db import db


class ItemModel(db.Model):
    __tablename__  = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel') # sqlAlchemy does the join, and now each item has a 'store' property

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price, 'store_id': self.store_id}

    @classmethod
    def get_by_name(cls, name):
        # connection, cursor = cls.get_db_cursor()
        # query = 'SELECT name, price from items where name = ?'
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # connection.close()
        # if row:
        #     return cls(*row)  # unpacking  cls(row[0], row[1])

        # replaced by SQL Alchemy code
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
