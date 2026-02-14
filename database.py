import sqlite3
from models2 import Checklist, ChecklistHeader, ChecklistItem

DB_NAME = "kerman_pm.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    """ساخت جدول‌ها و پر کردن داده‌های اولیه اگر دیتابیس خالی باشد"""
    conn = get_connection()
    c = conn.cursor()
    
    # 1. ساخت جدول چک‌لیست‌ها
    c.execute('''CREATE TABLE IF NOT EXISTS checklists (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sys_id TEXT,
                    title TEXT,
                    view_capability TEXT
                )''')
    
    # 2. ساخت جدول سرفصل‌ها
    c.execute('''CREATE TABLE IF NOT EXISTS headers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    checklist_id INTEGER,
                    title TEXT,
                    FOREIGN KEY(checklist_id) REFERENCES checklists(id)
                )''')
    
    # 3. ساخت جدول سوالات
    c.execute('''CREATE TABLE IF NOT EXISTS items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    header_id INTEGER,
                    question TEXT,
                    score TEXT,
                    FOREIGN KEY(header_id) REFERENCES headers(id)
                )''')
    
    conn.commit()
    
    # چک کنیم اگر داده‌ای نیست، داده‌های اولیه (مشهد) را بریزیم
    c.execute("SELECT count(*) FROM checklists")
    if c.fetchone()[0] == 0:
        seed_data(conn)
        print("✅ دیتابیس با داده‌های اولیه پر شد.")
    
    conn.close()

def seed_data(conn):
    """تزریق داده‌های فایل ورد مشهد به دیتابیس"""
    c = conn.cursor()
    
    # لیست داده‌ها (خلاصه شده برای نمونه - اینجا تمام داده‌های شما قرار می‌گیرد)
    # شما می‌توانید تمام آن لیست بلندبالای قبلی را اینجا کپی کنید تا یکبار وارد دیتابیس شود
    
    # --- نمونه 1: ارزیابی پیمانکار ---
    c.execute("INSERT INTO checklists (sys_id, title, view_capability) VALUES (?, ?, ?)", 
              ("1001", "ارزیابی پیمانکار توسط متقاضی", "درخواست اتمام کار"))
    cl_id = c.lastrowid
    
    c.execute("INSERT INTO headers (checklist_id, title) VALUES (?, ?)", (cl_id, "عمومی"))
    h_id = c.lastrowid
    
    questions = [
        ("آیا از نحوه اجرای کار پیمانکار رضایت دارید؟", "0"),
        ("آیا پیمانکار در زمان مقرر پروژه را شروع و به پایان رسانده است؟", "0")
    ]
    for q, s in questions:
        c.execute("INSERT INTO items (header_id, question, score) VALUES (?, ?, ?)", (h_id, q, s))

    # --- نمونه 2: ارزیابی طراحی (چک لیست بزرگ) ---
    c.execute("INSERT INTO checklists (sys_id, title, view_capability) VALUES (?, ?, ?)", 
              ("1003", "چک لیست ارزیابی طراحی", "پنل طراحی"))
    cl_id = c.lastrowid
    
    # سرفصل 1
    c.execute("INSERT INTO headers (checklist_id, title) VALUES (?, ?)", (cl_id, "الزامات دفترچه ی طراحی پروژه"))
    h_id = c.lastrowid
    c.execute("INSERT INTO items (header_id, question, score) VALUES (?, ?, ?)", (h_id, "آرشیو تصاویر محل پیوست دفترچه می باشد", "3"))
    c.execute("INSERT INTO items (header_id, question, score) VALUES (?, ?, ?)", (h_id, "اطلاعات روجلدی پرونده مطابق دستورالعمل است", "3"))
    
    # سرفصل 2
    c.execute("INSERT INTO headers (checklist_id, title) VALUES (?, ?)", (cl_id, "محاسبات اقتصادی"))
    h_id = c.lastrowid
    c.execute("INSERT INTO items (header_id, question, score) VALUES (?, ?, ?)", (h_id, "قیمت ها و ضرایب به روز می باشد", "0"))

    conn.commit()

def fetch_all_checklists():
    """خواندن تمام چک‌لیست‌ها از دیتابیس و تبدیل به آبجکت‌های مدل"""
    conn = get_connection()
    c = conn.cursor()
    
    # گرفتن تمام چک‌لیست‌ها
    c.execute("SELECT id, sys_id, title, view_capability FROM checklists")
    db_checklists = c.fetchall()
    
    final_list = []
    
    for cl_row in db_checklists:
        cl_obj = Checklist(cl_row[1], cl_row[2], cl_row[3]) # sys_id, title, view
        cl_id = cl_row[0]
        
        # گرفتن سرفصل‌های این چک‌لیست
        c.execute("SELECT id, title FROM headers WHERE checklist_id=?", (cl_id,))
        headers = c.fetchall()
        
        for h_row in headers:
            h_obj = cl_obj.add_header(h_row[1]) # title
            h_id = h_row[0]
            
            # گرفتن سوالات این سرفصل
            c.execute("SELECT question, score FROM items WHERE header_id=?", (h_id,))
            items = c.fetchall()
            
            for item in items:
                h_obj.add_item(item[0], item[1]) # question, score
        
        final_list.append(cl_obj)
        
    conn.close()
    return final_list