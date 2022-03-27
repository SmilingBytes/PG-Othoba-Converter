from openpyxl import Workbook
from db_classes import Product

filename = "test.xlsx"

workbook = Workbook()
sheet = workbook.active

main_header = ["ProductId","Name","ShortDescription","FullDescription","Vendor","MetaKeywords","MetaTitle","ItemCode","SCMCode","ManageInventoryMethod","StockQuantity","Price","AvailablePaymentMethod","ProductCost","Categories","Manufacturers","Picture1","Picture2","Picture3"]
attribute_header = ["","","AttributeType","SpecificationAttributeId","SpecificationAttributeOptionId","Name","AllowFiltering"]

sheet.append(main_header)
sheet.append(attribute_header)

products = []
product = Product(
    name= "Product 1",
    price= '300',
    fulldescription= 'aaaaaaaaaallllllllllllllll',
    itemcode= '101',
    picture1= '1111',
    productcost= '250'
)

products.append(product)

for p in products:
    data = [p.id, p.name]

    sheet.append(data)

workbook.save(filename=filename)


