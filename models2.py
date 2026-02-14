from datetime import datetime

# --- کلاس‌های پایه و کارتابل ---
class Project:
    def __init__(self, tracking_id, region, title, subject, sender):
        self.tracking_id = tracking_id
        self.region = region
        self.title = title
        self.subject = subject
        self.sender = sender
        self.receiver = "Admin(Admin--1)"
        self.date = datetime.now().strftime("%Y/%m/%d")
        self.request_type = "جهت تایید ارسال پرونده به EGS"
        self.request_group = "جهت تایید"
        self.status = "جهت تعیین تکلیف در فرایند دیگر"

class SupportTicket:
    def __init__(self):
        self.system_id = ""
        self.current_user = ""
        self.current_stage = ""
        self.creator_user = ""
        self.creator_code = ""
        self.req_type = ""
        self.description = ""
        self.has_attachment = False
        self.project_number = ""
        self.record_sys_id = ""
        self.page_link = ""
        self.system_admin = ""
        self.mobile = ""
        self.importance = ""
        self.admin_comment = ""
        self.need_hq_permit = False
        self.receiver_type = ""
        self.send_to_support = ""
        self.date_send_admin = ""
        self.date_send_makan = ""
        self.date_done_makan = ""
        self.date_end_ticket = ""
        self.person_hours = ""
        self.performer = ""

# --- کلاس‌های اقتصادی و فهرست بها ---
class EconomicBaseData:
    def __init__(self, sys_code, year, prod_cost, sale_price):
        self.sys_code = sys_code
        self.year = year
        self.prod_cost = prod_cost
        self.sale_price = sale_price
        self.reg_date = datetime.now().strftime("%Y/%m/%d")
        self.last_edit_date = datetime.now().strftime("%Y/%m/%d")

class PriceListWeight:
    def __init__(self, description, year="-", number="-"):
        self.description = description
        self.year = year
        self.number = number

class MarketPriceList:
    def __init__(self, description, active_process, status, year, code):
        self.description = description
        self.active_process = active_process
        self.status = status
        self.year = year
        self.code = code

class PriceGroupMain:
    def __init__(self, sys_code, title, weight):
        self.sys_code = sys_code
        self.title = title
        self.weight = weight

class PriceGroup:
    def __init__(self, sys_code, main_group, title, order):
        self.sys_code = sys_code
        self.main_group = main_group
        self.title = title
        self.order = order

class PriceGroupDetail:
    def __init__(self, sys_code, group, title, desc):
        self.sys_code = sys_code
        self.group = group
        self.title = title
        self.desc = desc

# --- کلاس‌های نقشه و چک‌لیست ---
class MapSymbol:
    def __init__(self, sys_id, title, layer_title, layer_code, elem_type, z_order, symbol_icon):
        self.sys_id = sys_id
        self.title = title
        self.layer_title = layer_title
        self.layer_code = layer_code
        self.elem_type = elem_type
        self.z_order = z_order
        self.symbol_icon = symbol_icon

class MapSymbolGroup:
    def __init__(self, sys_id, title):
        self.sys_id = sys_id
        self.title = title

class MapDisplaySetting:
    def __init__(self, sys_id, title):
        self.sys_id = sys_id
        self.title = title

class ChecklistItem:
    def __init__(self, question, score="0"):
        self.question = question
        self.score = score
        self.type = "بله/خیر"

class ChecklistHeader:
    def __init__(self, title):
        self.title = title
        self.items = []
    def add_item(self, question, score="0"):
        self.items.append(ChecklistItem(question, score))

class Checklist:
    def __init__(self, sys_id, title, view_capability):
        self.sys_id = sys_id
        self.title = title
        self.view_capability = view_capability
        self.headers = []
    def add_header(self, title):
        header = ChecklistHeader(title)
        self.headers.append(header)
        return header

# ==========================================
# کلاس‌های اطلاعات عمومی طراحی (19 مورد)
# ==========================================

class DesignRegion:
    def __init__(self, name, altitude, max_temp, min_temp, wind, humidity, factor):
        self.name = name
        self.altitude = altitude
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.wind = wind
        self.humidity = humidity
        self.factor = factor

class DesignAffair:
    def __init__(self, name):
        self.name = name

class DesignUtilizationFactor:
    def __init__(self, title, std_type, min_val, max_val, factor):
        self.title = title
        self.std_type = std_type
        self.min_val = min_val
        self.max_val = max_val
        self.factor = factor

class DesignVoltage:
    def __init__(self, value):
        self.value = value

class DesignCustomerType:
    def __init__(self, title, peak_load, cos_phi):
        self.title = title
        self.peak_load = peak_load
        self.cos_phi = cos_phi

class DesignDefaultTitle:
    def __init__(self, sys_id, project_class, title):
        self.sys_id = sys_id
        self.project_class = project_class
        self.title = title

class DesignDefaultValue:
    def __init__(self, sys_id, project_class, region, title, value, unit):
        self.sys_id = sys_id
        self.project_class = project_class
        self.region = region
        self.title = title
        self.value = value
        self.unit = unit

class DesignEarthType:
    def __init__(self, row_num, title):
        self.row_num = row_num
        self.title = title

class DesignClimateRegime:
    def __init__(self, row_num, title):
        self.row_num = row_num
        self.title = title

class DesignClimateLevel:
    def __init__(self, row_num, title):
        self.row_num = row_num
        self.title = title

class DesignClimateValue:
    def __init__(self, row_num, regime, level, wire_temp, sec_temp, ice_dia, wind_speed, uts, flash):
        self.row_num = row_num
        self.regime = regime
        self.level = level
        self.wire_temp = wire_temp
        self.sec_temp = sec_temp
        self.ice_dia = ice_dia
        self.wind_speed = wind_speed
        self.uts = uts
        self.flash = flash

class DesignReason:
    def __init__(self, sys_code, title):
        self.sys_code = sys_code
        self.title = title

class DesignHandover:
    def __init__(self, sys_code, title):
        self.sys_code = sys_code
        self.title = title

class DesignDemandFactor:
    def __init__(self, sys_code, ampere, max_count, phases, factor):
        self.sys_code = sys_code
        self.ampere = ampere
        self.max_count = max_count
        self.phases = phases
        self.factor = factor

class DesignCommonDesc:
    def __init__(self, sys_code, description):
        self.sys_code = sys_code
        self.description = description

class DesignGISEquivalent:
    def __init__(self, sys_code, line_type, gis_name, gis_section, gis_material, gis_code, equiv_code):
        self.sys_code = sys_code
        self.line_type = line_type
        self.gis_name = gis_name
        self.gis_section = gis_section
        self.gis_material = gis_material
        self.gis_code = gis_code
        self.equiv_code = equiv_code

class DesignLoadFactor:
    def __init__(self, sys_code, cust_type, demand_type, min_count, max_count, sync_factor, part_factor):
        self.sys_code = sys_code
        self.cust_type = cust_type
        self.demand_type = demand_type
        self.min_count = min_count
        self.max_count = max_count
        self.sync_factor = sync_factor
        self.part_factor = part_factor

class DesignElectricalZoning:
    def __init__(self, sys_code, affair_title, region_title):
        self.sys_code = sys_code
        self.affair_title = affair_title
        self.region_title = region_title

class DesignAffairLoad:
    def __init__(self, sys_code, affair, cust_type, peak_load, cos_phi):
        self.sys_code = sys_code
        self.affair = affair
        self.cust_type = cust_type
        self.peak_load = peak_load
        self.cos_phi = cos_phi