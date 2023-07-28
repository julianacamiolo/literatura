from fastapi import APIRouter, Query, Path
from pydantic import BaseModel

router = APIRouter()

class Libros(BaseModel):
    id: int
    name: str
    price: float
    stock: int

libros = [
    {
        "id": 2,
        "name": "libros 2",
        "price": 500,
        "stock": 150
    }
]

Literatura_Fantastica = [
    {
        "id": 3,
        "name": "Literatura_Fantastica",
        "stock": 350
    }
]

Literatura_Clasica = [
    {
        "id": 4,
        "name": "Literatura_Clasica",
        "stock": 5000
    }
]

Literatura_Autor = [
    {
        "id": 5,
        "name": "Literatura_Autor",
        "stock": 400
    }
]

@router.get('/Generos_Literarios')
def get_Generos_Literarios():
    return "Generos_Literarios"

@router.get('/libros/{id}')
def get_libros(id: int = Path(gt=0)):
    return list(filter(lambda item: item['id'] == id, libros))

@router.get('/Literatura_Fantastica')
def get_Literatura_Fantastica():
    return Literatura_Fantastica

@router.get('/Literatura_Clasica')
def get_Literatura_Clasica():
    return Literatura_Clasica

@router.get('/Literatura_Autor')
def get_Literatura_Autor():
    return Literatura_Autor

@router.get('/libros/')
def get_libros_by_stock(stock: int = Query(..., gt=0), price: float = Query(..., gt=0)):
    return list(filter(lambda item: item['stock'] == stock and item['price'] > price, libros))

@router.post('/libros')
def encuentra_libros(libro: Libros):
    libros.append(libro.dict())
    return libro

@router.put('/libros/{id}')
def update_libros(id: int, libro: Libros):
    for index, item in enumerate(libros):
        if item['id'] == id:
            libros[index]['name'] = libro.name
            libros[index]['stock'] = libro.stock
            libros[index]['price'] = libro.price
            break
    return libro

@router.delete("/libros/{id}")
def delete_libros(id: int):
    global libros
    libros = [item for item in libros if item['id'] != id]
    return libros   