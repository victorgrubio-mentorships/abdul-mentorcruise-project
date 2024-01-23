from __init__.py import db

class Association(db.Model):
    item_id = db.Column(db.String(50), db.ForeignKey('item.id'), primary_key=True)
    account_id = db.Column(db.String(50), db.ForeignKey('account.id'), primary_key=True)
    # Additional fields can be added here if needed

    item = db.relationship("Item", back_populates="accounts")
    account = db.relationship("Account", back_populates="items")

   
   # def toDict(self):
   #     return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs} >>> commented out undefined variable.