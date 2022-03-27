from dataclasses import dataclass
from typing import Any
# from typing import List

@dataclass
class Options:
    AttributeType: Any = ''
    SpecificationAttributeId: Any = ''
    SpecificationAttributeOptionId: Any = ''
    Name: Any = ''
    AllowFiltering: Any = ''

@dataclass
class Product:
    # sales: List[Sale]
    name: Any
    fulldescription: Any
    itemcode: Any
    price: Any
    productcost: Any
    picture1: str
    picture2: str = ''
    picture3: str = ''
    manufacturers: str = ''

    shortdescription: str = ''
    stockquantity: int = 101
    scmcode: str = ''
    id: Any = 0
    vendor: Any = "PG"
    manageinventorymethod: Any = 'Manage Stock By Attributes'
    availablepaymentmethod: Any = 'Payments.Bkash,Payments.CashOnDelivery,Payments.CityBank,Payments.EasyPayBd,Payments.EblSkyPay,Payments.InstantPay'
    categories: Any = '66,75,85'
    metakeywords: str = ''
    metatitle: str = ''
