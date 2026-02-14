import streamlit as st
import pandas as pd
from models2 import *

# --- 1. سایدبار ---
def render_kerman_sidebar():
    st.sidebar.image("https://cdn-icons-png.flaticon.com/512/4140/4140048.png", width=60)
    st.sidebar.markdown("### سامانه مدیریت پروژه")
    st.sidebar.markdown("---")
    
    menu_options = [
        "کارتابل", 
        "زیر ساخت های مهندسی",
        "پروژه و دستورکار",
        "کنترل کیفی تجهیزات",
        "پنل پیمانکاران/مشاوران",
        "پنل تامین کنندگان کالا",
        "پنل مناقصات",
        "پنل مشخصات نیروهای متخصص",
        "گزارشات",
        "صورت وضعیت تجمیعی",
        "پنل مدیریت دارایی",
        "حساب کاربری",
        "پنل مدیریت سامانه"
    ]
    return st.sidebar.radio("منو:", menu_options)

# --- 2. کارتابل ---
def render_cartable(projects: list):
    st.markdown("### 📨 کارتابل نامه‌های اداری")
    columns_structure = ["شماره نامه", "امور", "عنوان", "موضوع", "فرستنده", "گیرنده", "تاریخ", "نوع درخواست", "گروه درخواست", "وضعیت"]
    t1, t2 = st.tabs(["جهت اقدام", "جهت استحضار"])
    with t1:
        st.info("📭 هیچ نامه‌ای در کارتابل موجود نیست.")
        st.dataframe(pd.DataFrame(columns=columns_structure), use_container_width=True, hide_index=True)

# --- 3. پشتیبانی ---
def render_support_table(tickets: list):
    c1, c2 = st.columns([9, 1])
    c1.markdown("### ⚡ درخواست های پشتیبانی")
    c2.button("➕", help="افزودن درخواست جدید")
    columns_structure = ["شماره سیستمی درخواست", "کاربر فعلی", "مرحله فعلی", "کاربر ثبت کننده", "کد کاربر ثبت کننده", "نوع درخواست", "شرح درخواست", "دارای فایل پیوست", "شماره پروژه", "شماره سیستمی رکورد موردنظر", "لینک صفحه", "راهبر سامانه", "شماره همراه", "میزان اهمیت", "توضیحات راهبر سامانه", "نیاز به مجوز ستاد", "نوع گیرنده", "ارسال/عدم ارسال به شرکت پشتیبان", "تاریخ ارسال به راهبر", "تاریخ ارسال به شرکت ماکان", "تاریخ انجام توسط شرکت ماکان", "تاریخ پایان تیکت", "نفر ساعت", "انجام دهنده درخواست"]
    st.info("🎫 هیچ تیکت پشتیبانی ثبت نشده است.")
    st.dataframe(pd.DataFrame(columns=columns_structure), use_container_width=True, hide_index=True)

# --- 4. گروه بندی فهرست بها ---
def render_price_list_grouping(main_groups, groups, details):
    st.markdown("### 📑 گروه بندی فهرست بها")
    t1, t2, t3, t4 = st.tabs(["گروه اصلی", "گروه ها", "جزئیات گروه ها", "اقلام فهرست بها"])
    
    with t1:
        with st.expander("➕ افزودن گروه اصلی", expanded=False):
            with st.form("add_main_group"):
                c1, c2 = st.columns(2)
                title = c1.text_input("عنوان گروه اصلی")
                weight = c2.text_input("وزن")
                if st.form_submit_button("💾 ذخیره"):
                    new_code = str(len(main_groups) + 1)
                    main_groups.append(PriceGroupMain(new_code, title, weight))
                    st.success("اضافه شد")
                    st.rerun()

        if main_groups:
            data = [{"کد سیستمی": i.sys_code, "عنوان گروه اصلی": i.title, "وزن": i.weight} for i in main_groups]
            st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)
        else:
            st.info("داده ای نیست.")

    with t2:
        with st.expander("➕ افزودن گروه", expanded=False):
            with st.form("add_group"):
                c1, c2, c3 = st.columns(3)
                mg = c1.selectbox("گروه اصلی", [m.title for m in main_groups] if main_groups else ["-"])
                title = c2.text_input("عنوان گروه")
                order = c3.text_input("شماره ترتیب")
                if st.form_submit_button("💾 ذخیره"):
                    new_code = str(len(groups) + 1)
                    groups.append(PriceGroup(new_code, mg, title, order))
                    st.success("اضافه شد")
                    st.rerun()
        
        if groups:
            data = [{"کد سیستمی": i.sys_code, "گروه اصلی": i.main_group, "عنوان گروه": i.title, "شماره ترتیب": i.order} for i in groups]
            st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)

    with t3:
        with st.expander("➕ افزودن جزئیات", expanded=False):
            with st.form("add_detail"):
                c1, c2, c3 = st.columns(3)
                g_title = c1.selectbox("عنوان گروه", [g.title for g in groups] if groups else ["-"])
                title = c2.text_input("عنوان")
                desc = c3.text_input("توضیحات")
                if st.form_submit_button("💾 ذخیره"):
                    new_code = str(len(details) + 1)
                    details.append(PriceGroupDetail(new_code, g_title, title, desc))
                    st.success("اضافه شد")
                    st.rerun()
        
        if details:
            data = [{"کد سیستمی": i.sys_code, "عنوان گروه": i.group, "عنوان": i.title, "توضیحات": i.desc} for i in details]
            st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)

    with t4:
        c1, c2 = st.columns([9, 1])
        c2.button("➕", key="add_item_dummy")
        st.dataframe(pd.DataFrame(columns=["موجود در آرایش", "دارای گروه", "کد سیستمی", "عنوان", "واحد", "کد اموال", "تجهیز معادل در انبار", "عنوان اختصاری", "عنوان گروه اصلی", "عنوان گروه", "نوع", "پاور", "نیاز به Asset Id"]), use_container_width=True, hide_index=True)

# --- 5. اطلاعات پایه اقتصادی ---
def render_economic_calculations(data_list: list):
    st.markdown("### 💰 اطلاعات پایه محاسبات اقتصادی طرح ها")
    
    with st.expander("➕ افزودن اطلاعات سال جدید", expanded=False):
        with st.form("add_eco_form"):
            c1, c2, c3 = st.columns(3)
            new_year = c1.text_input("سال", value="1405")
            new_prod = c2.text_input("قیمت تولید (ریال)", value="300")
            new_sale = c3.text_input("قیمت فروش (ریال)", value="200")
            
            if st.form_submit_button("💾 ذخیره"):
                new_code = str(len(data_list) + 1)
                data_list.append(EconomicBaseData(new_code, new_year, new_prod, new_sale))
                st.success(f"ثبت شد.")
                st.rerun()

    if data_list:
        table_data = [{"کد سیستمی": item.sys_code, "سال": item.year, "قیمت تولید هر کیلو وات": item.prod_cost, "قیمت فروش هر کیلو وات": item.sale_price, "تاریخ ثبت": item.reg_date, "آخرین تاریخ ویرایش": item.last_edit_date} for item in data_list]
        st.dataframe(pd.DataFrame(table_data), use_container_width=True, hide_index=True)
    else:
        st.info("داده‌ای نیست.")

# --- 6. فهرست بها ---
def render_price_list_tabs(weights_list: list):
    st.markdown("### 📑 فهرست بها")
    t1, t2 = st.tabs(["وزن های فهرست بها", "آیتم های فهرست بها"])
    with t1:
        with st.expander("➕ افزودن فهرست بهای جدید", expanded=False):
            with st.form("add_weight_form"):
                desc = st.text_input("توضیحات")
                c_year, c_num = st.columns(2)
                year = c_year.text_input("سال", value="1404")
                num = c_num.text_input("شماره", value="-")
                
                if st.form_submit_button("💾 ذخیره"):
                    weights_list.append(PriceListWeight(desc, year, num))
                    st.success("اضافه شد.")
                    st.rerun()

        if weights_list:
            data = [{"توضیحات": item.description, "سال": item.year, "شماره": item.number} for item in weights_list]
            st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)
        else:
            st.info("موردی یافت نشد.")
            
    with t2:
        cols = ["ردیف", "شماره ورژن", "عنوان گروه", "کد کالا یا خدمات", "عنوان کالا", "واحد", "قیمت پایه کالا", "دستمزد", "ضریب مستعمل", "ضریب اسقاط", "ضریب عملیات", "ضریب جا به جایی", "ضریب عملیات اسقاط"]
        st.info("ردیفی برای نمایش وجود ندارد")
        st.dataframe(pd.DataFrame(columns=cols), use_container_width=True, hide_index=True)

# --- 7. چک لیست ها ---
def render_checklist_management(checklists: list):
    st.markdown("### 📋 پنل مدیریت چک لیست ها")
    checklist_names = [f"{c.sys_id} - {c.title}" for c in checklists]
    selected_option = st.selectbox("انتخاب:", ["-- لیست کلی --"] + checklist_names)

    if selected_option == "-- لیست کلی --":
        if checklists:
            data = [{"شماره سیستمی": c.sys_id, "عنوان": c.title, "قابلیت مشاهده در": c.view_capability, "تعداد سرفصل": len(c.headers)} for c in checklists]
            st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)
    else:
        selected_id = selected_option.split(" - ")[0]
        current_checklist = next((c for c in checklists if c.sys_id == selected_id), None)
        if current_checklist:
            st.markdown(f"#### 🔸 {current_checklist.title}")
            for header in current_checklist.headers:
                with st.expander(f"🔹 {header.title}", expanded=False):
                    if header.items:
                        st.table(pd.DataFrame([{"سوال": i.question, "نمره": i.score} for i in header.items]))

# --- 8. فهرست بها بازار (اصلاح شده: افزودن فرم) ---
def render_market_price_list(market_data: list):
    st.markdown("### 📊 فهرست بها بازار")
    t1, t2 = st.tabs(["وزن های فهرست بها بازار", "آیتم های فهرست بها بازار"])
    
    with t1:
        # فرم افزودن (جایگزین دکمه‌های ساده)
        with st.expander("➕ ایجاد فهرست بهای بازار جدید", expanded=False):
            with st.form("add_market_price"):
                c1, c2 = st.columns(2)
                desc = c1.text_input("توضیحات (عنوان)")
                year = c2.text_input("سال", value="1404")
                if st.form_submit_button("💾 ذخیره"):
                    market_data.append(MarketPriceList(desc, "فهرست بهای بازار", "ثبت اولیه", year, "-1"))
                    st.success("اضافه شد")
                    st.rerun()

        if market_data:
            data = [{"توضیحات": i.description, "فرایند فعال": i.active_process, "وضعیت": i.status, "سال": i.year, "کد": i.code} for i in market_data]
            st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)
        else:
            st.info("رکوردی موجود نیست.")

    with t2:
        st.dataframe(pd.DataFrame(columns=["ردیف", "عنوان کالا", "قیمت"]), use_container_width=True, hide_index=True)

# --- 9. مدیریت آیتم‌های نقشه (اصلاح شده: افزودن فرم) ---
def render_map_item_management(symbols, groups, settings):
    st.markdown("### 🗺️ مدیریت آیتم های نقشه")
    
    t1, t2, t3 = st.tabs(["سمبل های نقشه", "گروه بندی سمبل ها", "تنظیمات نمایشی"])
    
    # --- تب 1: سمبل ها ---
    with t1:
        c1, c2, c3, c4 = st.columns(4)
        c1.button("اتصالات مجاز", use_container_width=True)
        c2.button("ایجاد المان ترکیبی", use_container_width=True)
        c3.button("آنالیز مصالح", use_container_width=True)
        c4.button("ذخیره کلی", type="primary", use_container_width=True)
        st.write("---")
        
        # فرم افزودن سمبل
        with st.expander("➕ افزودن سمبل جدید", expanded=False):
            with st.form("add_map_symbol"):
                col1, col2, col3 = st.columns(3)
                title = col1.text_input("عنوان")
                layer = col2.text_input("نام لایه GIS")
                code = col3.text_input("کد لایه")
                if st.form_submit_button("💾 ذخیره"):
                    new_id = str(len(symbols) + 1)
                    symbols.append(MapSymbol(new_id, title, layer, code, "Point", "10", "📍"))
                    st.success("اضافه شد")
                    st.rerun()

        if symbols:
            data = []
            for s in symbols:
                data.append({
                    "شماره سیستمی": s.sys_id,
                    "عنوان": s.title,
                    "عنوان لایه": s.layer_title,
                    "کد لایه": s.layer_code,
                    "نوع المان": s.elem_type,
                    "ZOrder": s.z_order,
                    "سمبل": s.symbol_icon
                })
            st.dataframe(pd.DataFrame(data), use_container_width=True, hide_index=True)
        else:
            st.info("سمبلی تعریف نشده است.")

    # --- تب 2: گروه‌بندی ---
    with t2:
        with st.expander("➕ افزودن گروه جدید", expanded=False):
            with st.form("add_map_group"):
                title = st.text_input("عنوان گروه")
                if st.form_submit_button("💾 ذخیره"):
                    new_id = str(len(groups) + 1)
                    groups.append(MapSymbolGroup(new_id, title))
                    st.success("اضافه شد")
                    st.rerun()

        if groups:
            data_g = [{"شماره سیستمی": g.sys_id, "عنوان": g.title} for g in groups]
            st.dataframe(pd.DataFrame(data_g), use_container_width=True, hide_index=True)
        else:
            st.info("گروهی تعریف نشده است.")

    # --- تب 3: تنظیمات ---
    with t3:
        with st.expander("➕ افزودن تنظیمات جدید", expanded=False):
            with st.form("add_map_setting"):
                title = st.text_input("عنوان تنظیمات")
                if st.form_submit_button("💾 ذخیره"):
                    new_id = str(len(settings) + 1)
                    settings.append(MapDisplaySetting(new_id, title))
                    st.success("اضافه شد")
                    st.rerun()

        if settings:
            data_s = [{"شماره سیستمی": s.sys_id, "عنوان": s.title} for s in settings]
            st.dataframe(pd.DataFrame(data_s), use_container_width=True, hide_index=True)
        else:
            st.info("تنظیماتی تعریف نشده است.")

# --- 10. اطلاعات عمومی طراحی (19 تب کامل) ---
def render_general_design_info(regions, affairs, factors, voltages, customers, 
                               def_titles, def_values, earths, regimes, levels, 
                               climate_vals, reasons, handovers, demands, 
                               descriptions, gis_data, load_factors, 
                               zonings, affair_loads):
    
    st.markdown("### ⚙️ اطلاعات عمومی طراحی")
    
    tabs = st.tabs([
        "مناطق نصب", "امور نصب", "ضریب بهره برداری", "سطوح ولتاژ", "نوع مشترک",
        "عناوین پیش فرض", "مقادیر پیش فرض", 
        "انواع ارت", "رژیم آب و هوایی", "سطوح آب و هوایی", "مقادیر آب و هوا",
        "دلایل طراحی", "شرایط واگذاری", "ضریب دیماند", "توضیحات مشترک", 
        "معادل GIS", "ضریب بار", "منطقه بندی الکتریکی", "بار مشترکین امورها"
    ])
    
    with tabs[0]:
        c1, c2 = st.columns([9, 1])
        c2.button("➕", key="add_reg")
        if regions:
            data = [{"نام شهر": r.name, "ارتفاع": r.altitude, "دما (max)": r.max_temp, "دما (min)": r.min_temp, "باد": r.wind, "رطوبت": r.humidity, "ضریب": r.factor} for r in regions]
            st.dataframe(pd.DataFrame(data), use_container_width=True)

    with tabs[1]:
        c1, c2 = st.columns([9, 1])
        c2.button("➕", key="add_aff")
        if affairs:
            st.dataframe(pd.DataFrame([{"نام امور": a.name} for a in affairs]), use_container_width=True)

    with tabs[2]:
        c1, c2 = st.columns([9, 1])
        c2.button("➕", key="add_fac")
        if factors:
            data = [{"عنوان": f.title, "نوع": f.std_type, "Min": f.min_val, "Max": f.max_val, "ضریب": f.factor} for f in factors]
            st.dataframe(pd.DataFrame(data), use_container_width=True)

    with tabs[3]:
        c1, c2 = st.columns([9, 1])
        c2.button("➕", key="add_vol")
        if voltages:
            st.dataframe(pd.DataFrame([{"ولتاژ (Kv)": v.value} for v in voltages]), use_container_width=True)

    with tabs[4]:
        c1, c2 = st.columns([9, 1])
        c2.button("➕", key="add_cus")
        if customers:
            data = [{"نوع مشترک": c.title, "پیک بار": c.peak_load, "CosPhi": c.cos_phi} for c in customers]
            st.dataframe(pd.DataFrame(data), use_container_width=True)

    with tabs[5]:
        if def_titles:
            data = [{"کد": t.sys_id, "کلاسه": t.project_class, "عنوان": t.title} for t in def_titles]
            st.dataframe(pd.DataFrame(data), use_container_width=True)

    with tabs[6]:
        if def_values:
            data = [{"کد": v.sys_id, "ناحیه": v.region, "عنوان": v.title, "مقدار": v.value, "واحد": v.unit} for v in def_values]
            st.dataframe(pd.DataFrame(data), use_container_width=True)

    with tabs[7]:
        c1, c2 = st.columns([9, 1])
        c2.button("➕", key="add_earth")
        if earths:
            st.dataframe(pd.DataFrame([{"ردیف": i.row_num, "عنوان": i.title} for i in earths]), use_container_width=True)

    with tabs[8]:
        c1, c2 = st.columns([9, 1])
        c2.button("➕", key="add_regime")
        if regimes:
            st.dataframe(pd.DataFrame([{"ردیف": i.row_num, "عنوان": i.title} for i in regimes]), use_container_width=True)

    with tabs[9]:
        c1, c2 = st.columns([9, 1])
        c2.button("➕", key="add_level")
        if levels:
            st.dataframe(pd.DataFrame([{"ردیف": i.row_num, "عنوان": i.title} for i in levels]), use_container_width=True)

    with tabs[10]:
        c1, c2 = st.columns([9, 1])
        c2.button("➕", key="add_clim")
        if climate_vals:
            data = [{"رژیم": i.regime, "سطح": i.level, "دما سیم": i.wire_temp, "یخ": i.ice_dia, "باد": i.wind_speed} for i in climate_vals]
            st.dataframe(pd.DataFrame(data), use_container_width=True)

    with tabs[11]:
        c1, c2 = st.columns([9, 1])
        c2.button("➕", key="add_reas")
        if reasons:
            st.dataframe(pd.DataFrame([{"کد": r.sys_code, "عنوان": r.title} for r in reasons]), use_container_width=True)
        else:
            st.dataframe(pd.DataFrame(columns=["کد", "عنوان"]), use_container_width=True)

    with tabs[12]:
        c1, c2 = st.columns([9, 1])
        c2.button("➕", key="add_hand")
        if handovers:
            st.dataframe(pd.DataFrame([{"کد": h.sys_code, "عنوان": h.title} for h in handovers]), use_container_width=True)
        else:
            st.dataframe(pd.DataFrame(columns=["کد", "عنوان"]), use_container_width=True)

    with tabs[13]:
        c1, c2 = st.columns([9, 1])
        c2.button("➕", key="add_dem")
        if demands:
            st.dataframe(pd.DataFrame([vars(d) for d in demands]), use_container_width=True)
        else:
            st.dataframe(pd.DataFrame(columns=["کد", "آمپر", "تعداد"]), use_container_width=True)

    with tabs[14]:
        c1, c2 = st.columns([9, 1])
        c2.button("➕", key="add_desc")
        if descriptions:
            st.dataframe(pd.DataFrame([{"کد": d.sys_code, "توضیحات": d.description} for d in descriptions]), use_container_width=True)

    with tabs[15]:
        c1, c2 = st.columns([9, 1])
        c2.button("➕", key="add_gis")
        if gis_data:
            data = [{"نوع خط": g.line_type, "نام GIS": g.gis_name, "کد معادل": g.equiv_code} for g in gis_data]
            st.dataframe(pd.DataFrame(data), use_container_width=True)

    with tabs[16]:
        c1, c2 = st.columns([9, 1])
        c2.button("➕", key="add_load")
        if load_factors:
            data = [{"نوع مشترک": l.cust_type, "ضریب همزمانی": l.sync_factor, "تعداد": l.max_count} for l in load_factors]
            st.dataframe(pd.DataFrame(data), use_container_width=True)

    with tabs[17]:
        c1, c2 = st.columns([9, 1])
        c2.button("➕", key="add_zone")
        if zonings:
            st.dataframe(pd.DataFrame([{"کد": z.sys_code, "امور": z.affair_title, "منطقه": z.region_title} for z in zonings]), use_container_width=True)
        else:
            st.info("داده ای نیست")

    with tabs[18]:
        c1, c2 = st.columns([9, 1])
        c2.button("➕", key="add_aff_load")
        if affair_loads:
            data = [{"امور": a.affair, "نوع مشترک": a.cust_type, "پیک بار": a.peak_load} for a in affair_loads]
            st.dataframe(pd.DataFrame(data), use_container_width=True)
        else:
            st.info("داده ای نیست")