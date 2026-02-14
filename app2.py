import streamlit as st
import views2 
import database 
from models2 import *

st.set_page_config(page_title="سامانه مدیریت پروژه", layout="wide", page_icon="⚡")

def main():
    database.init_db()

    st.markdown("""
        <div style='background-color:#5677fc;padding:15px;border-radius:0px;margin-bottom:10px;direction:rtl'>
            <h3 style='color:white;text-align:center;font-family:tahoma;margin:0'>سامانه مدیریت پروژه</h3>
        </div>
    """, unsafe_allow_html=True)

    selected_menu = views2.render_kerman_sidebar()

    if selected_menu == "کارتابل":
        with st.sidebar:
            st.markdown("---")
            st.markdown("📂 **زیرمجموعه کارتابل:**")
            cartable_type = st.radio("نوع نمایش:", ["نامه‌های اداری", "درخواست‌های پشتیبانی"], label_visibility="collapsed", key="cartable_radio")
            
        if cartable_type == "نامه‌های اداری":
            views2.render_cartable([]) 
        else:
            views2.render_support_table([]) 
            
    elif selected_menu == "زیر ساخت های مهندسی":
        
        # --- مقداردهی متغیرهای Session State ---
        if 'economic_data' not in st.session_state:
            st.session_state.economic_data = [
                EconomicBaseData("1", "1402", "300", "200"),
                EconomicBaseData("2", "1403", "300", "200"),
                EconomicBaseData("3", "1404", "300", "200")
            ]
        
        if 'price_weights' not in st.session_state:
            st.session_state.price_weights = [
                PriceListWeight("فهرست بهای داخلی 1404- تست 1"),
                PriceListWeight("فهرست بهای پایه سال 1404")
            ]

        # --- داده‌های اطلاعات عمومی طراحی (19 جدول) ---
        if 'design_regions' not in st.session_state:
            st.session_state.design_regions = [DesignRegion("آب بر", "1000", "40", "-1", "25", "30", "1"), DesignRegion("آبادان", "1000", "40", "-1", "25", "30", "1")]
        if 'design_affairs' not in st.session_state:
            st.session_state.design_affairs = [DesignAffair("ارزوئیه"), DesignAffair("بافت"), DesignAffair("بردسیر")]
        if 'design_factors' not in st.session_state:
            st.session_state.design_factors = [DesignUtilizationFactor("A", "ارتفاع", "1000-", "1000", "1"), DesignUtilizationFactor("A", "دما", "100-", "25-", "1.37")]
        if 'design_voltages' not in st.session_state:
            st.session_state.design_voltages = [DesignVoltage("0/40"), DesignVoltage("20/00")]
        if 'design_customers' not in st.session_state:
            st.session_state.design_customers = [DesignCustomerType("خانگی شهری", "4/50", "0/90"), DesignCustomerType("تجاری شهری", "4/00", "0/90")]
        if 'design_def_titles' not in st.session_state:
            st.session_state.design_def_titles = [DesignDefaultTitle("26", "پیش فرض های طرح", "کد رژیم آب و هوایی")]
        if 'design_def_values' not in st.session_state:
            st.session_state.design_def_values = [DesignDefaultValue("35", "پیش فرض طرح", "همه", "هادی فشار متوسط", "905", "سیم")]
        if 'design_earths' not in st.session_state:
            st.session_state.design_earths = [DesignEarthType("1", "اتصال زمین"), DesignEarthType("2", "ارت الکتریکی")]
        if 'design_regimes' not in st.session_state:
            st.session_state.design_regimes = [DesignClimateRegime("2", "منطقه سبک"), DesignClimateRegime("3", "منطقه متوسط")]
        if 'design_levels' not in st.session_state:
            st.session_state.design_levels = [DesignClimateLevel("1", "باد سنگین"), DesignClimateLevel("2", "باد و یخ")]
        if 'design_climate_vals' not in st.session_state:
            st.session_state.design_climate_vals = [DesignClimateValue("1", "سبک", "باد و یخ", "25", "15", "0", "10", "20", "2.5")]
        if 'design_descriptions' not in st.session_state:
            st.session_state.design_descriptions = [DesignCommonDesc("2", "حریم شبکه 20 کیلوولت 210 سانتیمتر است")]
        if 'design_gis_data' not in st.session_state:
            st.session_state.design_gis_data = [DesignGISEquivalent("2", "هوایی ف م", "سیم آلومینیوم 35", "---", "AL", "AL25", "کد معادل")]
        if 'design_load_factors' not in st.session_state:
            st.session_state.design_load_factors = [DesignLoadFactor("8", "خانگی شهری", "دیماندی", "60", "10000", "0.273", "---")]
        if 'design_zonings' not in st.session_state:
            st.session_state.design_zonings = [DesignElectricalZoning("3", "بردسیر", "بردسیر"), DesignElectricalZoning("7", "بافت", "بافت")]
        if 'design_affair_loads' not in st.session_state:
            st.session_state.design_affair_loads = [DesignAffairLoad("4", "ارزوئیه", "خانگی شهری", "2", "0.9")]

        # --- داده‌های نقشه (جدید - برای حل مشکل خالی بودن) ---
        if 'map_symbols_db' not in st.session_state:
            st.session_state.map_symbols_db = [MapSymbol("1", "سکسیونر", "gis:discnt", "59", "Point", "10", "SF6")]
        if 'map_groups_db' not in st.session_state:
            st.session_state.map_groups_db = [MapSymbolGroup("2", "طرح فشار متوسط")]
        if 'map_settings_db' not in st.session_state:
            st.session_state.map_settings_db = [MapDisplaySetting("1", "Default")]

        # --- داده‌های بازار و گروه‌بندی ---
        if 'market_price_db' not in st.session_state:
            st.session_state.market_price_db = [MarketPriceList("فهرست بهای داخلی 1404", "فهرست بهای بازار", "تایید", "1404", "-1")]
        
        if 'main_groups' not in st.session_state:
            st.session_state.main_groups = [PriceGroupMain("1", "پایه - فونداسیون", "15"), PriceGroupMain("2", "تجهیزات تابلو", "5")]
        
        if 'groups_list' not in st.session_state:
            st.session_state.groups_list = [PriceGroup("364", "پایه - فونداسیون", "پایه های فشار ضعیف", "2")]
            
        if 'group_details' not in st.session_state:
            st.session_state.group_details = [PriceGroupDetail("3937", "پایه های فشار ضعیف", "انواع لامپ", "-")]

        if 'checklists_db' not in st.session_state:
            st.session_state.checklists_db = database.fetch_all_checklists()

        # --- منوی زیرساخت ---
        with st.sidebar:
            st.markdown("---")
            st.markdown("🏗️ **تنظیمات پایه:**")
            
            infra_sub_menu = st.radio(
                "زیرمجموعه:",
                [
                    "گروه بندی فهرست بها",
                    "اطلاعات پایه محاسبات اقتصادی طرح ها",
                    "فهرست بها",
                    "پنل مدیریت چک لیست ها",
                    "فهرست بها بازار",
                    "مدیریت آیتم های نقشه",
                    "اطلاعات عمومی طراحی", 
                    "اطلاعات و کاربرد آرایش ها",
                    "مشخصات فنی تجهیزات",
                    "چک لیست تجهیزات",
                    "تنظیمات نسخه های چاپی",
                    "ناظرین قرارداد"
                ],
                label_visibility="collapsed",
                key="infra_radio"
            )
            
        # --- نمایش صفحات ---
        if infra_sub_menu == "اطلاعات عمومی طراحی":
            views2.render_general_design_info(
                st.session_state.design_regions,
                st.session_state.design_affairs,
                st.session_state.design_factors,
                st.session_state.design_voltages,
                st.session_state.design_customers,
                st.session_state.design_def_titles,
                st.session_state.design_def_values,
                st.session_state.design_earths,
                st.session_state.design_regimes,
                st.session_state.design_levels,
                st.session_state.design_climate_vals,
                [], [], [], 
                st.session_state.design_descriptions,
                st.session_state.design_gis_data,
                st.session_state.design_load_factors,
                st.session_state.design_zonings,
                st.session_state.design_affair_loads
            )
        
        elif infra_sub_menu == "گروه بندی فهرست بها":
            views2.render_price_list_grouping(
                st.session_state.main_groups, 
                st.session_state.groups_list, 
                st.session_state.group_details
            )
            
        elif infra_sub_menu == "اطلاعات پایه محاسبات اقتصادی طرح ها":
            views2.render_economic_calculations(st.session_state.economic_data)

        elif infra_sub_menu == "فهرست بها":
            views2.render_price_list_tabs(st.session_state.price_weights)

        elif infra_sub_menu == "پنل مدیریت چک لیست ها":
            views2.render_checklist_management(st.session_state.checklists_db)

        elif infra_sub_menu == "فهرست بها بازار":
            views2.render_market_price_list(st.session_state.market_price_db)
            
        elif infra_sub_menu == "مدیریت آیتم های نقشه":
            # اصلاح شده: حالا داده‌ها را پاس می‌دهد
            views2.render_map_item_management(
                st.session_state.map_symbols_db,
                st.session_state.map_groups_db,
                st.session_state.map_settings_db
            )
            
        else:
            st.subheader(f"🏗️ {infra_sub_menu}")
            st.write("---")
            st.info("فرم‌های این بخش هنوز طراحی نشده است.")

    else:
        st.subheader(f"📂 {selected_menu}")
        st.write("---")
        st.info("محتوای این بخش هنوز بارگذاری نشده است.")

if __name__ == "__main__":
    main()