"""
Aaron Althauser
IU International University of Applied Sciences
Data Science, M.Sc.
"""

from data_models import Sale, SaleDetail, Purchase, PurchaseDetail, Branch, Region, MenuItem, MenuDetail, Product, \
    Supplier, Time
import pandas as pd
import random
import datetime
from datetime import timedelta


def rand_list(n, nmax, nmin=1):
    liszt = []
    for i in range(0, n - 1):
        r = random.randint(nmin, nmax)
        liszt.append(r)
    return liszt


def date_builder():
    day = random.randrange(1, 29)
    month = random.randrange(1, 13)
    year = random.randrange(2019, 2022)
    if year == 2021:
        month = random.randrange(1, 10)
    date1 = datetime.date(year, month, day)
    interval = random.randrange(3, 30)
    date2 = date1 + timedelta(days=interval)
    quarter = 4
    if int(date1.month) <= 3:
        quarter = 1
    elif int(date1.month) <= 6:
        quarter = 2
    elif int(date1.month) <= 9:
        quarter = 3
    return date1, date2, interval, quarter


def time_builder():
    hr = random.randrange(9, 22)
    mn = random.randrange(0, 60)
    sec = random.randrange(0, 60)
    time = f'{hr}:{mn}:{sec}'
    return time


def purchase_builder(product_df, n=10000):
    """purchase details"""
    df = product_df
    purchases_table = pd.DataFrame(columns=['PurchaseID', 'Total', 'DateOrdered', 'DateReceived', 'ProcessTime'])
    purchase_detail_table = pd.DataFrame(columns=['PurchaseID', 'ProductID', 'SupplierID', 'TimeID', 'BranchID',
                                                  'UnitQuantity', 'UnitPrice', 'UnitTotal'])
    for purchase_id in range(1, n):
        # build random purchases, purchase details
        purchase_order_size = random.randint(1, 7)  # number of items on purchase list
        branch_id = random.randrange(1, 401)
        order_total = 0
        for i in range(purchase_order_size):
            # random purchase item
            purchase_detail_dict = {'PurchaseID': purchase_id}
            p_id = random.randrange(1, 31)  # random product
            unit_qty = random.randrange(1, 26)  # random product qty
            p = df.loc[df['ProductID'] == str(p_id)]  # search product table for id
            p = p.squeeze()  # convert df to series
            purchase_detail_dict['ProductID'] = p.ProductID
            purchase_detail_dict['SupplierID'] = p.SupplierID
            purchase_detail_dict['TimeID'] = purchase_id
            purchase_detail_dict['BranchID'] = branch_id
            purchase_detail_dict['UnitQuantity'] = unit_qty
            purchase_detail_dict['UnitPrice'] = p.UnitPrice
            unit_total = float(p.UnitPrice) * unit_qty
            purchase_detail_dict['UnitTotal'] = unit_total
            purchase_detail_table = purchase_detail_table.append(purchase_detail_dict, ignore_index=True)
            order_total += (unit_total)

        # purchases
        order_date, receive_date, process_time, q = date_builder()
        purchases_dict = {'PurchaseID': purchase_id, 'Total': order_total, 'DateOrdered': order_date,
                          'DateReceived': receive_date, 'ProcessTime': process_time}
        purchases_table = purchases_table.append(purchases_dict, ignore_index=True)
        purchases_table = purchases_table.astype(object)
    return purchases_table, purchase_detail_table


def sale_builder(menuitems, time_table, n=20000):
    menu_df = menuitems
    menu_df['Price'] = menu_df['Price'].astype(float)
    sale_details_table = pd.DataFrame(columns=['SaleID', 'MenuItemID', 'MenuItemQuantity',
                                               'Total', 'TimeID'])
    sales_table = pd.DataFrame(columns=['SaleID', 'BranchID', 'Total', 'TimeID'])
    for sale_id in range(1, n):
        last_index = time_table.iloc[-1].TimeID
        time_id_stamp = last_index + 1
        sale_order_size = random.randrange(1, 6)
        branch_id = random.randrange(1, 401)
        sale_total = 0
        for i in range(sale_order_size):
            item_id = random.randrange(1, 31)
            qty = random.randrange(1, 6)
            from_menu = menu_df.loc[menu_df['MenuItemID'] == str(item_id)]
            item = from_menu.squeeze()
            sale_details_dict = {'SaleID': sale_id, 'MenuItemID': item.MenuItemID, 'MenuItemQuantity': qty}
            total = item.Price * qty
            sale_total += total
            sale_details_dict['Total'] = total
            sale_details_dict['TimeID'] = time_id_stamp
            sale_details_table = sale_details_table.append(sale_details_dict, ignore_index=True)

        # update time table and sales
        date, d2, inter, quarter = date_builder()
        time = time_builder()
        time_dict = {'TimeID': time_id_stamp, 'Day': date.day, 'Month': date.month, 'Year': date.year,
                     'Quarter': quarter, 'Time': time}
        time_table = time_table.append(time_dict, ignore_index=True)
        sales_dict = {'SaleID': sale_id, 'BranchID': branch_id, 'Total': sale_total, 'TimeID': time_id_stamp}
        sales_table = sales_table.append(sales_dict, ignore_index=True)
        sales_table.SaleID = sales_table.SaleID.astype(str).replace('\.0+$', '', regex=True)
        sales_table.BranchID = sales_table.BranchID.astype(str).replace('\.0+$', '', regex=True)
        sales_table.TimeID = sales_table.TimeID.astype(str).replace('\.0+$', '', regex=True)
        sales_table = sales_table.astype(object)
    return sales_table, sale_details_table, time_table


def main():
    """
    suppliers
    regions
    branches
    menuitems
    products
    menu details
    customer orders (sales)
    product purchases (purchases)
    """

    '''supppliers'''
    companyName = ['General Goods', 'Sweets and Drinks', 'Atlantic Fish Co', 'Ovation Seafood', 'Variety Seafood',
                   'Seafood Creations', 'Wicked Seafood', 'Seafood Sales', 'Chord Seafood', 'Plus Seafood']
    address = ['Auf dem Bruch 82a', 'Theodor-Gierath-Str. 1, Apt. 981', '03517 Legros Mountain, Suite 808',
               '24115 Metz Lane, Apt. 172', 'Perssons Väg 417, Lgh. 285', 'Juliaplein 762, 3 hoog achter'
                                                                          'Vedviks Gate 85, Leil. 287',
               'Nygårds Vei 4, Oppgang A', 'Skolgatan 05, Lgh. 631', 'Södra Björkgränden 3']
    city = ['Süd Leana', 'Paeslerdorf', 'New Augustus', 'Leannaport', 'Götetuna', 'Pannerden aan de IJssel',
            'Stavsund', 'Høyeid', 'Botorp', 'Helsingås']
    postalCode = ['72121', '38773', 'MA67 7IB', 'PN97 7MI', '11465', '6696 UO', '2329', '5925', '56594', '92907']
    country = ['Germany', 'Germany', 'Great Britain', 'Great Britain', 'Sweden', 'Netherlands', 'Norway', 'Norway',
               'Sweden', 'Sweden']
    supplier_table = pd.DataFrame(columns=['SupplierID', 'CompanyName', 'Address', 'City', 'PostalCode', 'Country'])
    for i in range(1, 10):
        Supplier.name = companyName.pop(0)
        Supplier.address = address.pop(0)
        Supplier.city = city.pop(0)
        Supplier.postal_code = postalCode.pop(0)
        Supplier.country = country.pop(0)
        supplier_dict = {'SupplierID': Supplier.name, 'CompanyName': Supplier.name, 'Address': Supplier.address,
                         'City': Supplier.city, 'PostalCode': Supplier.postal_code, 'Country': Supplier.country}
        supplier_table = supplier_table.append(supplier_dict, ignore_index=True)
        # insert into suppliers table
    print(supplier_table.head())

    '''branches'''
    branches_table = pd.DataFrame(columns=['BranchID', 'RegionID', 'City', 'PostalCode'])
    with open('./BI_casestudy_testdata_branches.csv', 'r') as csv:
        for r in csv.readlines()[1:]:
            row = r.split(',')
            if not row[0].__sizeof__() == 49:
                Branch.id = row[0]
                Branch.region_id = row[1]
                Branch.city = row[2]
                Branch.postal_code = row[3].strip()
                branch_dict = {'BranchID': Branch.id, 'RegionID': Branch.region_id, 'City': Branch.city,
                               'PostalCode': Branch.postal_code}
                branches_table = branches_table.append(branch_dict, ignore_index=True)
                # insert into branches table
            else:
                break
    print(branches_table.head())

    '''regions'''
    rs = ['Baden-Württemberg', 'Bavaria', 'Berlin', 'Brandenburg', 'Bremen', 'Hamburg', 'Hesse',
          'Lower Saxony', 'Mecklenburg-Western Pomerania', 'North Rhine-Westphalia', 'Rhineland-Palatinate',
          'Saarland', 'Saxony', 'Saxony-Anhalt', 'Schleswig-Holstein', 'Thuringia']
    region_table = pd.DataFrame(columns=['RegionID', 'Name'])
    for i in range(1, 15):
        reg_dict = {'RegionID': i, 'Name': rs.pop(0)}
        region_table = region_table.append(reg_dict, ignore_index=True)
    print(region_table.head())

    '''Menu items'''
    menuitem_table = pd.DataFrame(columns=['MenuItemID', 'Name', 'Category', 'Price'])
    '''items = ['Cod, 3 pc', 'Cod, 5 pc', 'Halibut', 'Salmon', 'Oysters', 'Clams', 'Scallops', 'Baby Prawns',
             'Jumbo Prawns', 'Atlantic Salmon', 'Black Cod with Miso', 'Curried Cod and Mussels',
             'Soused Herring', 'Salmon Caesar', 'Shrimp Caesar', 'Smoked-Trout Chowder', 'Salmon and Potato',
             'Corn and Cod Chowder', 'Fries', 'Shrimp Cocktail', 'Corn Bread', 'Cole Slaw', 'Chocolate Souffle',
             'Ice Cream', 'Red Berry Compte', 'Vanilla Tart', 'Coffee', 'Milk', 'Juice', 'Soda']'''
    with open('./BI_casestudy_testdata_menuitems.csv', 'r') as csv:
        for r in csv.readlines()[1:]:
            row = r.split(',')
            if not row[0].__sizeof__() == 49:
                MenuItem.id = row[0]
                MenuItem.name = row[1]
                MenuItem.category = row[2]
                MenuItem.price = row[3].strip()
                menu_dict = {'MenuItemID': MenuItem.id, 'Name': MenuItem.name, 'Category': MenuItem.category,
                             'Price': MenuItem.price}
                menuitem_table = menuitem_table.append(menu_dict, ignore_index=True)
    # insert into meunuitems table
    print(menuitem_table.head())

    '''products'''
    prod_table = pd.DataFrame(columns=['ProductID', 'ProductName', 'SupplierID', 'UnitQuantity', 'UnitMeasure',
                                       'UnitPrice', 'UnitsInStock'])
    with open('./BI_casestudy_testdata_products.csv', 'r') as csv:
        for r in csv.readlines()[1:]:
            row = r.split(',')
            if not row[0].__sizeof__() == 49:
                Product.id = row[0]
                Product.product_name = row[1]
                Product.supplier_id = row[2]
                Product.unit_qty = row[3]
                Product.unit_measure = row[4]
                Product.unit_price = row[5]
                Product.units_stock = row[6].strip()
                prod_dict = {'ProductID': Product.id, 'ProductName': Product.product_name,
                             'SupplierID': Product.supplier_id, 'UnitQuantity': Product.unit_qty,
                             'UnitMeasure': Product.unit_measure, 'UnitPrice': Product.unit_price,
                             'UnitsInStock': Product.units_stock}
                prod_table = prod_table.append(prod_dict, ignore_index=True)
    print(prod_table.head())

    '''menu details'''
    menudetail_table = pd.DataFrame(columns=['ProductID', 'MenuItemID', 'ProductQuantity'])
    with open('./BI_casestudy_testdata_menudetails.csv', 'r') as csv:
        for r in csv.readlines()[1:]:
            row = r.split(',')
            if not row[0].__sizeof__() == 49:
                MenuDetail.product_id = row[0]
                MenuDetail.menuitem_id = row[1]
                MenuDetail.product_qty = row[2].strip()
                menudetail_dict = {'ProductID': MenuDetail.product_id, 'MenuItemID': MenuDetail.menuitem_id,
                                   'ProductQuantity': MenuDetail.product_qty}
                menudetail_table = menudetail_table.append(menudetail_dict, ignore_index=True)
    print(menudetail_table.head())

    '''purchases & purchase details'''
    purchases, purchase_details = purchase_builder(prod_table, 10)
    print(purchases.head())
    print(purchase_details.head())

    '''time'''
    time_table = pd.DataFrame(columns=['TimeID', 'Day', 'Month', 'Year', 'Quarter', 'Time'])
    # Purchases part of Time table
    for row in purchases.iterrows():
        date = row[1].DateOrdered
        time = time_builder()
        quarter = 4
        if int(date.month) <= 3:
            quarter = 1
        elif int(date.month) <= 6:
            quarter = 2
        elif int(date.month) <= 9:
            quarter = 3
        time_dict = {'TimeID': row[1].PurchaseID, 'Day': date.day, 'Month': date.month, 'Year': date.year,
                     'Quarter': quarter, 'Time': time}
        time_table = time_table.append(time_dict, ignore_index=True)


    '''sales'''
    sales_table, sale_details_table, time_table = sale_builder(menuitem_table, time_table, 200)
    print(sales_table.head())
    print(sale_details_table.head())
    print(time_table.head())

if __name__ == '__main__':
    main()
