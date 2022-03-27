from dataclasses import dataclass
from typing import Any
# from typing import List

# @dataclass
# class Sale:
    # quantity: int

@dataclass
class Product:
    # sales: List[Sale]
    name: str
    shortdescription: str
    fulldescription: str
    metakeywords: str
    metatitle: str
    itemcode: str
    price: str
    productcost: str
    manufacturers: str
    picture1: str
    picture2: str
    picture3: str

    stockquantity: int = 101
    scmcode: str = ''
    id: Any = 0
    vendor: Any = "PG"
    manageinventorymethod: Any = 'Manage Stock By Attributes'
    availablepaymentmethod: Any = 'Payments.Bkash,Payments.CashOnDelivery,Payments.CityBank,Payments.EasyPayBd,Payments.EblSkyPay,Payments.InstantPay'
    categories: Any = '66,75,85'
