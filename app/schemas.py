from pydantic import BaseModel
from enum import Enum

class J(str, Enum):
    UY = "UY"
    MX = "MX"
    US = "US"
    ES = "ES"
    AR = "AR"
    CA = "CA"
    GB = "GB"   
    UA = "UA"
    CL = "CL"
    CO = "CO"
    IT = "IT"
    GT = "GT"
    PT = "PT"
    CH = "CH"
    TR = "TR"
    FR = "FR"
    KR = "KR"
    AU = "AU"
    BR = "BR"

class TransactionInput(BaseModel):
    a: int
    b: int
    c: int
    d: int
    e: float
    f: float
    g: float
    h: int
    i: int
    j: J
    k: float
    l: int
    m: int
    n: int
    o: int
    p: int
    q: float
    r: float
    s: float
    monto: float
