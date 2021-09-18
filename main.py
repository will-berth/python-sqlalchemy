import db
from models import Producto

def run():
    arroz = Producto('Arroz', 1.25)
    db.session.add(arroz)
    print(arroz.id)
    agua = Producto('Agua', 0.3)
    db.session.add(agua)
    db.session.commit()
    print(arroz.id)
    
    productos = db.session.query(Producto).get(2)
    print(productos)

    agua = db.session.query(Producto).filter_by(nombre='Agua').first()
    print(agua)

    menos_de_1 = db.session.query(Producto).filter(Producto.precio < 1).all()
    print(menos_de_1)

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    run()