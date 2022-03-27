import timeit, os, json, re
import logging

logging.basicConfig(filename='app.log', format='%(asctime)s : [%(levelname)s] %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)

start = timeit.default_timer()

logging.info(f'Starting Converter')
print(f'Starting Converter')

# Boots/Scraped Products
with open('data.json') as json_file:
    data = json.load(json_file)
    cnt  = 0
    for p in data['products']:
        __import__('pprint').pprint(p)
        print("\n\n================================================================\n\n\n")
        cnt += 1
        if cnt == 5: break;

        product_price = re.findall('\d+\.\d+', p['old_price']) if p['old_price'] else re.findall('\d+\.\d+', p['price'])
        if not product_price:
            continue
#
        if type(product_price) is list:
            product_price = float(product_price[0])
#                 
        product_price = str(int(product_price))

        options = [var['name'] for var in p['variations']]

        if options:
            pass
        else:
            sku = f'BTS_{p["code"]}'
#
#         media_link = 'https://payligram.com/wp-content/uploads/2021/11'
#
#         img_path = f"{media_link}/bts/{p['department']}/{p['category']}/{p['subcategory']}" if len(p['subcategory']) else f"{media_link}/bts/{p['department']}/{p['category']}"
#         img_path = img_path.replace('"', '')
#         img_path = img_path.replace("'", "")
#
#         product_images = [f'{img_path}/{p["code"]}.jpg']
#         product_images += [f'{img_path}/{img.split("/")[-1]}.jpg' for img in p['images'] if '_' in img]
#         product_images = [{"src": img,} for img in product_images]
#         
#
#
#
#         # checking new/existing product :: insert/update
#         if (wc_product := wc_products.get(sku)): # true mean existing product, so update it 
#
#             # - == === UPDATE === == -
#             p_data = dict()
#             v_data = list()
#             vi_data = list()
#             p_id = wc_product.get('id')
#
#             payligram_price = wc_product.get('price')
#             if int(float(payligram_price)) < int(product_price):
#                 p_data['regular_price'] = product_price
#
#             payligram_stock_info = wc_product.get('stock_status')
#             # TODO: check scraping stockinfo and update accordingly
#             # p_data['stock_status'] = 'instock'
#
#             new_category = categories.get(p['subcategory'])
#             payligram_categories = wc_product.get('categories')
#             if new_category not in payligram_categories:
#                 payligram_categories.append(new_category)
#                 wc_product['categories'] = payligram_categories
#                 wc_products[sku] = wc_product
#                 p_data['categories'] = [ { 'id': cat_id } for cat_id in payligram_categories ]
#             
#             pg_attributes = wc_product.get('attributes')
#             if len(pg_attributes) >= 1:
#                 pg_attributes = pg_attributes[0]
#                 pg_options = pg_attributes.get('options')
#
#                 new_options = []
#                 for i, var in enumerate(p['variations'], start=1):
#                     if var["name"] not in pg_options:
#                         var_dict = {
#                             "regular_price": product_price,
#                             "sku": f'BTSV{var["code"]}',
#                             "image": {
#                                 "src": f'{img_path}/{var["code"]}H.jpg',
#                                 "alt": f'{p["name"]} ({var["name"]})',
#                             },
#                             "attributes": [
#                                 {
#                                     "name": 'Variations',
#                                     "option": var["name"],
#                                 }
#                             ]
#                         }
#                         new_options.append(var["name"])
#                         vi_data.append(var_dict)
#             if len(new_options) > 0 :
#                 pg_options += new_options
#                 p_data['attributes'] = [
#                         {
#                             'name'       : 'Variations',
#                             'variation': True,
#                             'visible'  : True,
#                             'options'  : [ opt for opt in pg_options ],
#                         },
#                     ]
#             
#
#             if p_data or vi_data or int(float(payligram_price)) < int(product_price):
#                 update_product = {
#                     'id': p_id,
#                     'product': p_data,
#                     'variations': wc_product.get('variations') if int(float(payligram_price)) < int(product_price) else False, #v_data
#                     'variations_insert': vi_data,
#                 }
#                 update[p_id] = {
#                     'product': p_data,
#                     'variations': wc_product.get('variations') if int(float(payligram_price)) < int(product_price) else False, #v_data
#                     'variations_insert': vi_data,
#                 }
#
#                 cnt_u += 1
#                 print("u..", end="", flush=True)
#         
#         elif new_products.get(sku): # newly added (duplicate) product, so update categories.
#
#             # - == === CATEGORY UPDATE === == -
#             existing_categories = new_products.get(sku)
#             new_category = categories.get(p['subcategory'])
#             if new_category not in existing_categories:
#                 existing_categories.append(new_category)
#                 new_products[sku] = existing_categories
#             cnt_c += 1
#             print("c..", end="", flush=True)
#
#
#         else: # new product, so insert it.
#
#             # - == === INSERT === == -
#             clean = re.compile('<a.*?</a>') 
#             details = re.sub(clean, '', str(p.get('details')))
#
#             clean = re.compile('<img.*?/>') 
#             details = re.sub(clean, '', str(details))
#             clean = re.compile('<img.*?>') 
#             details = re.sub(clean, '', str(details))
#             
#             p_data = {
#                 "name": p['name'],
#                 "type": "variable" if len(options) > 0 else "simple",
#                 "sku": f'BTS_{p["code"]}',
#                 'stock_status': 'instock',
#                 'description': details,
#                 "regular_price": product_price,
#                 "categories": [
#                     {
#                         "id": categories.get(p['subcategory']),
#                     }
#                 ],
#                 "images": product_images,
#                 'attributes' : [
#                     {
#                         'name'       : 'Variations',
#                         'variation': True,
#                         'visible'  : True,
#                         'options'  : options,
#                     },
#                 ],
#             }
#
#             v_data = list()
#             if len(options) > 0:
#                 for i, var in enumerate(p['variations'], start=1):
#                     var_dict = {
#                         "regular_price": product_price,
#                         "sku": f'BTSV{var["code"]}',
#                         "image": {
#                             "src": f'{img_path}/{var["code"]}H.jpg',
#                             "alt": f'{p["name"]} ({var["name"]})',
#                         },
#                         "attributes": [
#                             {
#                                 "name": 'Variations',
#                                 "option": var["name"],
#                             }
#                         ]
#                     }
#                     v_data.append(var_dict)
#             
#
#             insert[sku] = {
#                 'product': p_data,
#                 'variations': v_data
#             }
#             new_products[sku] = [ categories.get(p['subcategory']) ]
#             cnt_i += 1
#             print("i..", end="", flush=True)
#
# for _sku, cat_ids in new_products.items():
#     insert_data = insert.get(_sku)
#     p_data = insert_data.get('product')
#     p_data['categories'] = [ { 'id': cat_id } for cat_id in cat_ids ]
#     insert_data['product'] = p_data
#     insert[_sku] = insert_data
#
# with open('.insert.json', 'w') as outfile:
#     json.dump(insert, outfile, indent=4)
# with open('.update.json', 'w') as outfile:
#     json.dump(update, outfile, indent=4)
#
# print(f"Inserted = {cnt_i}")
# logging.info(f"Inserted = {cnt_i}")
# print(f"Updated = {cnt_u}")
# logging.info(f"Updated = {cnt_u}")
# print(f"Duplicate/Category added = {cnt_c}")
# logging.info(f"Duplicate/Category added = {cnt_c}")
#
# duration = timeit.default_timer() - start
# print(f"\nDuration: {duration}")
# logging.info(f"\nDuration: {duration}")
#
#
# print(f"Insert = {len(insert)}")
# logging.info(f"Insert = {len(insert)}")
# print(f"Update = {len(update)}")
# logging.info(f"Update = {len(update)}")
