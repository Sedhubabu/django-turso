from .models_sqla import SessionLocal, Item

def create_item(name, description):
    db = SessionLocal()
    itm = Item(name=name, description=description)
    db.add(itm)
    db.commit()
    db.refresh(itm)
    db.close()
    return itm

def list_items():
    db = SessionLocal()
    items = db.query(Item).all()
    db.close()
    return items
