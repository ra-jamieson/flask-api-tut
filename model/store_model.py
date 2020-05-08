from db import db


class StoreModel(db.Model):
    __tablename__  = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    # back reference - # the relation is used to return the 'many' in the n:1 relation
    items = db.relationship('ItemModel', lazy='dynamic')  # forestall's object creation of items

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [itm.json() for itm in self.items.all()]}  # query builder only when called

    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
