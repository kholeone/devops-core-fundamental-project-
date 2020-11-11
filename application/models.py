from application import db
  
class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable = False)
    categories = db.relationship('Category', backref='listing')

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    list_description = db.Column(db.String(4000), nullable = False)
    listing_id = db.Column(db.Integer, db.ForeignKey('listing.id'), nullable=False)
