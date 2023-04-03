import numpy
from fastapi import APIRouter

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}


@router.get('/matrixproduct')
def matrix_product() -> dict:
    matrix_a = numpy.random.rand(10, 10).tolist()
    matrix_b = numpy.random.rand(10, 10).tolist()
    product = numpy.dot(matrix_a, matrix_b).tolist()
    return {"matrix_a": matrix_a, "matrix_b": matrix_b, "product": product}
