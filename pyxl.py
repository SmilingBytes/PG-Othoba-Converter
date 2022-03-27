from openpyxl import Workbook

filename = "hello_world.xlsx"

workbook = Workbook()
sheet = workbook.active

main_header = ["ProductId","Name","ShortDescription","FullDescription","Vendor","MetaKeywords","MetaTitle","ItemCode","SCMCode","ManageInventoryMethod","StockQuantity","Price","AvailablePaymentMethod","ProductCost","Categories","Manufacturers","Picture1","Picture2","Picture3"]
sheet.append(main_header)
workbook.save(filename=filename)

