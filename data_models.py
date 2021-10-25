from dataclasses import dataclass


@dataclass
class Sale:
    id: int
    branch_id: int
    total: float
    time_id: int
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value
    @property
    def branch_id(self):
        return self._branch_id
    @branch_id.setter
    def branch_id(self, value):
        self._branch_id = value
    @property
    def total(self):
        return self._total
    @total.setter
    def total(self, value):
        self._total = value
    @property
    def time_id(self):
        return self._time_id
    @time_id.setter
    def time_id(self, value):
        self._time_id = value

@dataclass
class SaleDetail:
    sale_id: int
    menuitem_id: int
    menuitem_qty: int
    total: float
    time_id: int
    @property
    def sale_id(self):
        return self._sale_id
    @sale_id.setter
    def sale_id(self, value):
        self._sale_id = value
    @property
    def menuitem_id(self):
        return self._menuitem_id
    @menuitem_id.setter
    def menuitem_id(self, value):
        self._menuitem_id = value
    @property
    def menuitem_qty(self):
        return self._menuitem_qty
    @menuitem_qty.setter
    def menuitem_qty(self, value):
        self._menuitem_qty = value
    @property
    def total(self):
        return self._total
    @total.setter
    def total(self, value):
        self._total = value
    @property
    def time_id(self):
        return self._timem_id
    @time_id.setter
    def time_id(self, value):
        self._time_id = value

@dataclass
class Time:
    id: int
    day: int
    month: int
    year: int
    quarter: int
    time: float
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value
    @property
    def day(self):
        return self._day
    @day.setter
    def day(self, value):
        self._day = value
    @property
    def month(self):
        return self._month
    @month.setter
    def month(self, value):
        self._month = value
    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, value):
        self._year = value
    @property
    def quarter(self):
        return self._quarter
    @quarter.setter
    def quarter(self, value):
        self._quarter = value
    @property
    def time(self):
        return self._time
    @time.setter
    def time(self, value):
        self._time = value

@dataclass
class Purchase:
    id: int
    total: float
    date_ordered: str
    date_received: str
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value
    @property
    def total(self):
        return self._total
    @total.setter
    def total(self, value):
        self._total = value
    @property
    def date_ordered(self):
        return self._date_ordered
    @date_ordered.setter
    def date_ordered(self, value):
        self._date_ordered = value
    @property
    def date_received(self):
        return self._date_received
    @date_received.setter
    def date_received(self, value):
        self._date_received = value

@dataclass
class PurchaseDetail:
    purchase_id: int
    product_id: int
    supplier_id: int
    time_id: int
    branch_id: int
    unit_qty: int
    unit_price: float
    unit_total: float
    order_total: float
    @property
    def purchase_id(self):
        return self._purchase_id
    @purchase_id.setter
    def purchase_id(self, value):
        self._purchase_id = value
    @property
    def product_id(self):
        return self._product_id
    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def supplier_id(self):
        return self._supplier_id
    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def time_id(self):
        return self._time_id
    @time_id.setter
    def time_id(self, value):
        self._time_id = value
    @property
    def branch_id(self):
        return self._branch_id
    @branch_id.setter
    def branch_id(self, value):
        self._branch_id = value
    @property
    def unit_qty(self):
        return self._unit_qty
    @unit_qty.setter
    def unit_qty(self, value):
        self._unit_qty = value
    @property
    def unit_price(self):
        return self._unit_price
    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value
    @property
    def unit_total(self):
        return self._unit_total
    @unit_total.setter
    def unit_total(self, value):
        self._unit_total = value
    @property
    def order_total(self):
        return self._order_total
    @order_total.setter
    def order_total(self, value):
        self._order_total = value

@dataclass
class Product:
    id: int
    product_name: str
    supplier_id: int
    unit_qty: int
    unit_measure: str
    unit_price: float
    units_stock: float
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value
    @property
    def product_name(self):
        return self._product_name
    @product_name.setter
    def product_name(self, value):
        self._product_name = value
    @property
    def supplier_id(self):
        return self._supplier_id
    @supplier_id.setter
    def supplier_id(self, value):
        self._supplier_id = value
    @property
    def unit_qty(self):
        return self._unit_qty
    @unit_qty.setter
    def unit_qty(self, value):
        self._unit_qty = value
    @property
    def unit_measure(self):
        return self._unit_measure
    @unit_measure.setter
    def unit_measure(self, value):
        self._unit_measure = value
    @property
    def unit_price(self):
        return self._unit_price
    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value
    @property
    def units_stock(self):
        return self._units_stock
    @units_stock.setter
    def units_stock(self, value):
        self._units_stock = value

@dataclass
class MenuItem:
    id: int
    name: str
    category: str
    price: float
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self, value):
        self._category = value
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        self._price = value

@dataclass
class MenuDetail:
    product_id: int
    menuitem_id: int
    product_qty: float
    @property
    def product_id(self):
        return self._product_id
    @product_id.setter
    def product_id(self, value):
        self._product_id = value
    @property
    def menuitem_id(self):
        return self._menuitem_id
    @menuitem_id.setter
    def menuitem_id(self, value):
        self._menuitem_id = value
    @property
    def product_qty(self):
        return self._product_qty
    @product_qty.setter
    def product_qty(self, value):
        self._product_qty = value

@dataclass
class Supplier:
    id: int
    name: str
    address: str
    city: str
    postal_code: str
    country: str
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
    @property
    def address(self):
        return self._address
    @address.setter
    def address(self, value):
        self._address = value
    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, value):
        self._city = value
    @property
    def postal_code(self):
        return self._postal_code
    @postal_code.setter
    def postal_code(self, value):
        self._postal_code = value
    @property
    def country(self):
        return self._country
    @country.setter
    def country(self, value):
        self._country = value

@dataclass
class Branch:
    id: int
    region_id: int
    city: str
    postal_code: str
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value
    @property
    def region_id(self):
        return self._region_id
    @region_id.setter
    def region_id(self, value):
        self._region_id = value
    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, value):
        self._city = value
    @property
    def postal_code(self):
        return self._postal_code
    @postal_code.setter
    def postal_code(self, value):
        self._postal_code = value

@dataclass
class Region:
    id: int
    name: str
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
