from fastapi import APIRouter
from app.models import model
from app.schemas import TransactionInput
import pandas as pd

router = APIRouter()

@router.post("/predict/")
def predict(transaction: TransactionInput):
    # Ensure that the dictionary contains all 20 expected columns
    input_data = pd.DataFrame([{
        'a': transaction.a, 'b': transaction.b, 'c': transaction.c, 'd': transaction.d, 
        'e': transaction.e, 'f': transaction.f, 'g': transaction.g, 'h': transaction.h, 
        'i': transaction.i, 'j': transaction.j, 'k': transaction.k, 'l': transaction.l, 
        'm': transaction.m, 'n': transaction.n, 'o': transaction.o, 'p': transaction.p, 
        'q': transaction.q, 'r': transaction.r, 's': transaction.s, 'monto': transaction.monto
    }], columns=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','monto'])

    prediction = model.predict(input_data)
    return {'fraudulent': bool(prediction[0])}
