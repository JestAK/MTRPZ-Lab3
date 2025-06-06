from fastapi import APIRouter
import numpy as np

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}

@router.get("/matrix")
def matrix() -> dict:
    mat_a = np.random.randint(0, 10, size=(10, 10))
    mat_b = np.random.randint(0, 10, size=(10, 10))

    product = mat_a.dot(mat_b)

    return {
        "matrix_a": mat_a.tolist(),
        "matrix_b": mat_b.tolist(),
        "product":   product.tolist(),
    }