import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import scrolledtext

class Melk: 
    def __init__(self , name , family , phone_number , nooe_melk, forosh , name_of_street , adress , metrazh,price_koll ,  telephone = None ,metrazh_mofid = None , tedad_tabaghe = None , tedad_vahed = None ,anbari = None ,tedad_khab = None , ashpazkhane = None , asansoor = None , parking = None , ab = None , bargh = None , gaz = None, telephone_melk = None , sand_malkiat = None , ghedmat = None , gheimat_metr_square = None , vam_banki = None , tozihat_ezafi =None  ):
        
        self.name = name
        self.family = family
        self.phone_number = phone_number
        self.nooe_melk = nooe_melk
        self.forosh = forosh
        self.name_of_street = name_of_street
        self.adress = adress
        self.metrazh = metrazh
        self.price_koll = price_koll    
        self.telephone = telephone
        self.metrazh_mofid = metrazh_mofid  
        self.tedad_tabaghe = tedad_tabaghe
        self.tedad_vahed = tedad_vahed
        self.anbari = anbari
        self.tedad_khab = tedad_khab
        self.ashpazkhane = ashpazkhane
        self.asansoor = asansoor
        self.parking = parking
        self.ab = ab
        self.bargh = bargh
        self.gaz = gaz
        self.telephone_melk = telephone_melk
        self.sand_malkiat = sand_malkiat
        self.ghedmat = ghedmat
        self.gheimat_metr_square = gheimat_metr_square      
        self.vam_banki = vam_banki
        self.tozihat_ezafi = tozihat_ezafi

    
class Database:

    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.connection.create_function("normalize_fa", 1, self._normalize_fa)
        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS melkha (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                name TEXT,
                family TEXT,
                telephone TEXT,
                phone_number TEXT,

                nooe_melk TEXT,
                forosh TEXT,
                name_of_street TEXT,
                adress TEXT,

                metrazh REAL,
                metrazh_mofid TEXT,
                tedad_tabaghe TEXT,
                tedad_vahed TEXT,
                tedad_khab TEXT,

                ashpazkhane TEXT,
                asansoor TEXT,
                parking TEXT,
                anbari TEXT,

                ab TEXT,
                bargh TEXT,
                gaz TEXT,
                telephone_melk TEXT,

                sand_malkiat TEXT,
                ghedmat TEXT,
                gheimat_metr_square TEXT,
                vam_banki TEXT,

                price_koll REAL,
                tozihat_ezafi TEXT
            )
            """
        )

        self.connection.commit()
    def _normalize_fa(self, value):
        if value is None:
            return ""
    
        value = str(value)
    
        value = value.replace("ي", "ی")
        value = value.replace("ك", "ک")
    
        value = value.replace("آ", "ا")
        value = value.replace("أ", "ا")
        value = value.replace("إ", "ا")
    
        value = value.replace("ؤ", "و")
        value = value.replace("ة", "ه")
    
        value = value.replace("‌", " ")
        value = value.strip()
    
        return value
    
    
    def add_melk(self , melk : Melk):
        self.cursor.execute(

            """

            INSERT INTO melkha (

                name,

                family,

                telephone,

                phone_number,

                nooe_melk,

                forosh,

                name_of_street,

                adress,

                metrazh,

                metrazh_mofid,

                tedad_tabaghe,

                tedad_vahed,

                tedad_khab,

                ashpazkhane,

                asansoor,

                parking,
                anbari,

                ab,

                bargh,

                gaz,

                telephone_melk,

                sand_malkiat,

                ghedmat,

                gheimat_metr_square,

                price_koll,

                vam_banki,

                tozihat_ezafi

                

            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

            """,

            (

                melk.name,

                melk.family,

                melk.telephone,

                melk.phone_number,

                melk.nooe_melk,

                melk.forosh,

                melk.name_of_street,

                melk.adress,

                melk.metrazh,

                melk.metrazh_mofid,

                melk.tedad_tabaghe,

                melk.tedad_vahed,

                melk.tedad_khab,

                melk.ashpazkhane,

                melk.asansoor,

                melk.parking,
                melk.anbari,

                melk.ab,

                melk.bargh,

                melk.gaz,

                melk.telephone_melk,

                melk.sand_malkiat,

                melk.ghedmat,

                melk.gheimat_metr_square,

                melk.price_koll,

                melk.vam_banki,

                melk.tozihat_ezafi

            )
        )


        

        self.connection.commit()
        return self.cursor.lastrowid

    def close(self):

        self.connection.close()

    def edit_melk(self, melk_id: int, melk: Melk):
        self.cursor.execute(
            """
            UPDATE melkha
            SET name = ?,
                family = ?,
                telephone = ?,
                phone_number = ?,
                nooe_melk = ?,
                forosh = ?,
                name_of_street = ?,
                adress = ?,
                metrazh = ?,
                metrazh_mofid = ?,
                tedad_tabaghe = ?,
                tedad_vahed = ?,
                tedad_khab = ?,
                ashpazkhane = ?,
                asansoor = ?,
                parking = ?,
                anbari = ?,
                ab = ?,
                bargh = ?,
                gaz = ?,
                telephone_melk = ?,
                sand_malkiat = ?,
                ghedmat = ?,
                gheimat_metr_square = ?,
                price_koll = ?,
                vam_banki = ?,
                tozihat_ezafi = ?
            WHERE id = ?
            """,
            (
                melk.name,
                melk.family,
                melk.telephone,
                melk.phone_number,
                melk.nooe_melk,
                melk.forosh,
                melk.name_of_street,
                melk.adress,
                melk.metrazh,
                melk.metrazh_mofid,
                melk.tedad_tabaghe,
                melk.tedad_vahed,
                melk.tedad_khab,
                melk.ashpazkhane,
                melk.asansoor,
                melk.parking,
                melk.anbari,
                melk.ab,
                melk.bargh,
                melk.gaz,
                melk.telephone_melk,
                melk.sand_malkiat,
                melk.ghedmat,
                melk.gheimat_metr_square,
                melk.price_koll,
                melk.vam_banki,
                melk.tozihat_ezafi,
                melk_id,
            )
        )
    
        self.connection.commit()
        return self.cursor.rowcount
    def delete_melk(self, melk_id: int):
        self.cursor.execute(
            """
            DELETE FROM melkha
            WHERE id = ?
            """,
            (melk_id,)
        )
        self.connection.commit()                                                                   
        return self.cursor.rowcount
    def get_melk_page(self, page: int = 1, page_size: int = 50):
        if page < 1:
            page = 1
    
        if page_size < 1:
            page_size = 50
    
        offset = (page - 1) * page_size
    
        self.cursor.execute(
            """
            SELECT id, name, family, phone_number, nooe_melk, name_of_street, metrazh, price_koll
            FROM melkha
            ORDER BY id DESC
            LIMIT ? OFFSET ?
            """,
            (page_size, offset)
        )
    
        return self.cursor.fetchall()
    def count_melk(self):
        self.cursor.execute("SELECT COUNT(*) FROM melkha")
        return self.cursor.fetchone()[0]
    def search_melk(self, keyword: str, limit: int = 50):
        keyword = self._normalize_fa(keyword)
    
        words = keyword.split()
    
        if not words:
            return []
    
        searchable_columns = [
            "name",
            "family",
            "phone_number",
            "nooe_melk",
            "name_of_street",
            "adress",
            "metrazh",
            "price_koll",
        ]
    
        where_parts = []
        params = []
    
        for word in words:
            pattern = f"%{word}%"
    
            one_word_conditions = []
    
            for column in searchable_columns:
                one_word_conditions.append(
                    f"normalize_fa(CAST({column} AS TEXT)) LIKE ?"
                )
                params.append(pattern)
    
            where_parts.append("(" + " OR ".join(one_word_conditions) + ")")
    
        where_sql = " AND ".join(where_parts)
    
        sql = f"""
            SELECT id, name, family, phone_number, nooe_melk, name_of_street, metrazh, price_koll
            FROM melkha
            WHERE {where_sql}
            ORDER BY id DESC
            LIMIT ?
        """
    
        params.append(limit)
    
        self.cursor.execute(sql, params)
        return self.cursor.fetchall()
    def get_melk_by_id(self, melk_id: int):
        self.cursor.execute(
            """
            SELECT
                id,
                name,
                family,
                telephone,
                phone_number,
                nooe_melk,
                forosh,
                name_of_street,
                adress,
                metrazh,
                metrazh_mofid,
                tedad_tabaghe,
                tedad_vahed,
                tedad_khab,
                ashpazkhane,
                asansoor,
                parking,
                anbari,
                ab,
                bargh,
                gaz,
                telephone_melk,
                sand_malkiat,
                ghedmat,
                gheimat_metr_square,
                vam_banki,
                price_koll,
                tozihat_ezafi
            FROM melkha
            WHERE id = ?
            """,
            (melk_id,)
        )
    
        return self.cursor.fetchone()
class ServiceLogic:

    def __init__(self, database: Database):
        self.database = database

    def _create_melk_from_form(self, form_data: dict):
        data = form_data.copy()

        data["name"] = data["name"].strip()
        data["family"] = data["family"].strip()
        data["phone_number"] = data["phone_number"].strip()

        if not data["name"]:
            raise ValueError("نام نباید خالی باشد")

        if not data["phone_number"]:
            raise ValueError("شماره تماس نباید خالی باشد")

        data["metrazh"] = self._to_float(data["metrazh"], "متراژ")
        data["price_koll"] = self._to_float(data["price_koll"], "قیمت کل")

        return Melk(**data)

    def _to_float(self, value, field_name):
        value = str(value).replace(",", "").strip()

        if not value:
            raise ValueError(f"{field_name} نباید خالی باشد")

        try:
            return float(value)
        except ValueError:
            raise ValueError(f"{field_name} باید عددی باشد")

    def add_melk(self, form_data: dict):
        melk = self._create_melk_from_form(form_data)
        return self.database.add_melk(melk)

    def edit_melk(self, melk_id: int, form_data: dict):
        melk = self._create_melk_from_form(form_data)
        return self.database.edit_melk(melk_id, melk)

    def delete_melk(self, melk_id: int):
        deleted_count = self.database.delete_melk(melk_id)
    
        if deleted_count == 0:
            raise ValueError("ملکی با این شناسه پیدا نشد")
    
        return deleted_count
    def search_melk(self, keyword: str, limit: int = 50):
        keyword = keyword.strip()

        if not keyword:
            return []

        return self.database.search_melk(keyword, limit)

    def get_melk_page(self, page: int = 1, page_size: int = 50):
        return self.database.get_melk_page(page, page_size)

    def count_melk(self):
        return self.database.count_melk()
    

    def get_melk_by_id(self, melk_id: int):
    
        return self.database.get_melk_by_id(melk_id)
#ui baraye vared kardan etelaat 
class View:
    def __init__(self, root, service: ServiceLogic):
        self.root = root
        self.service = service

        self.current_page = 1
        self.page_size = 50
        self.selected_melk_id = None

        self.root.title("  نرم‌افزار مدیریت املاک  ")
        self.root.geometry("1400x750")

        self.create_widgets()
        self.load_page()


    def create_widgets(self):
        header_frame = ttk.Frame(self.root)
        header_frame.pack(fill="x", padx=20, pady=10)
        
        header_frame.grid_columnconfigure(0, weight=1)
        header_frame.grid_columnconfigure(1, weight=2)
        header_frame.grid_columnconfigure(2, weight=1)
        
        empty_label = ttk.Label(header_frame, text="")
        empty_label.grid(row=0, column=0, sticky="w")
        
        title = ttk.Label(
            header_frame,
            text="نرم‌افزار مدیریت املاک  ",
            font=("Arial", 20, "bold")
        )
        title.grid(row=0, column=1)
        
        brand_label = ttk.Label(
            header_frame,
            text="طراحی و پشتیبانی:  ",
            font=("Arial", 12, "bold")
        )
        brand_label.grid(row=0, column=2, sticky="e")
    
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=15, pady=10)
    
        # مهم: چپ و راست با تغییر اندازه پنجره تغییر اندازه بدهند
        main_frame.grid_rowconfigure(0, weight=1)
    
        # نسبت عرض:
        # ستون 0 = فرم ویرایش
        # ستون 1 = جست‌وجو و لیست
        main_frame.grid_columnconfigure(0, weight=2)
        main_frame.grid_columnconfigure(1, weight=3)
    
        self.form_frame = ttk.LabelFrame(main_frame, text="جزئیات کامل ملک / ثبت و ویرایش")
        self.form_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)
    
        self.table_frame = ttk.LabelFrame(main_frame, text="جست‌وجو و لیست خلاصه")
        self.table_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=5)
    
        self.create_form()
        self.create_table_area()
    def create_form(self):
        self.entries = {}

        self.notebook = ttk.Notebook(self.form_frame)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        owner_tab = ttk.Frame(self.notebook)
        property_tab = ttk.Frame(self.notebook)
        facilities_tab = ttk.Frame(self.notebook)
        price_tab = ttk.Frame(self.notebook)

        self.notebook.add(owner_tab, text="اطلاعات مالک")
        self.notebook.add(property_tab, text="مشخصات ملک")
        self.notebook.add(facilities_tab, text="امکانات")
        self.notebook.add(price_tab, text="قیمت و توضیحات")

        owner_fields = [
            ("name", "نام مالک"),
            ("family", "نام خانوادگی"),
            ("phone_number", "شماره موبایل"),
            ("telephone", "تلفن ثابت مالک"),
        ]

        property_fields = [
            ("nooe_melk", "نوع ملک"),
            ("forosh", "فروش / اجاره"),
            ("name_of_street", "نام خیابان"),
            ("adress", "آدرس"),
            ("metrazh", "متراژ"),
            ("metrazh_mofid", "متراژ مفید"),
            ("tedad_tabaghe", "تعداد طبقه"),
            ("tedad_vahed", "تعداد واحد"),
            ("tedad_khab", "تعداد خواب"),
            ("ashpazkhane", "آشپزخانه"),
            ("ghedmat", "قدمت"),
        ]

        facilities_fields = [
            ("asansoor", "آسانسور"),
            ("parking", "پارکینگ"),
            ("anbari", "انباری"),
            ("ab", "آب"),
            ("bargh", "برق"),
            ("gaz", "گاز"),
            ("telephone_melk", "تلفن ملک"),
            ("sand_malkiat", "سند مالکیت"),
        ]

        price_fields = [
            ("gheimat_metr_square", "قیمت هر متر مربع"),
            ("vam_banki", "وام بانکی"),
            ("price_koll", "قیمت کل"),
        ]

        self.create_fields(owner_tab, owner_fields)
        self.create_fields(property_tab, property_fields)
        self.create_fields(facilities_tab, facilities_fields)
        self.create_fields(price_tab, price_fields)

        # توضیحات اضافی فضای بزرگ‌تر دارد
        ttk.Label(price_tab, text="توضیحات اضافی").grid(
            row=len(price_fields),
            column=0,
            sticky="nw",
            padx=8,
            pady=8
        )

        self.entries["tozihat_ezafi"] = scrolledtext.ScrolledText(
            price_tab,
            width=50,
            height=5,
            font=("Tahoma", 16),
            wrap="word"
        )
        self.entries["tozihat_ezafi"].grid(
            row=len(price_fields),
            column=1,
            sticky="nsew",
            padx=8,
            pady=8
        )

        price_tab.grid_columnconfigure(1, weight=1)
        price_tab.grid_rowconfigure(len(price_fields), weight=1)

 
        button_frame = ttk.Frame(self.form_frame)
        button_frame.pack(fill="x", padx=10, pady=10)
        
        for col in range(3):
            button_frame.grid_columnconfigure(col, weight=1)
        
        self.add_button = ttk.Button(
            button_frame,
            text="ثبت ملک جدید",
            command=self.on_add_click
        )
        self.add_button.grid(row=0, column=0, sticky="ew", padx=4, pady=4)
        
        self.edit_button = ttk.Button(
            button_frame,
            text="ویرایش ملک انتخاب‌شده",
            command=self.on_edit_click
        )
        self.edit_button.grid(row=0, column=1, sticky="ew", padx=4, pady=4)
        
        self.clear_button = ttk.Button(
            button_frame,
            text="پاک کردن فرم",
            command=self.clear_form
        )
        self.clear_button.grid(row=0, column=2, sticky="ew", padx=4, pady=4)
        
        self.prev_melk_button = ttk.Button(
            button_frame,
            text="ملک قبلی",
            command=self.select_prev_melk
        )
        self.prev_melk_button.grid(row=1, column=0, sticky="ew", padx=4, pady=4)
        
        self.next_melk_button = ttk.Button(
            button_frame,
            text="ملک بعدی",
            command=self.select_next_melk
        )
        self.next_melk_button.grid(row=1, column=1, sticky="ew", padx=4, pady=4)
    def create_fields(self, parent, fields):
        for row, (key, label_text) in enumerate(fields):
            label = ttk.Label(parent, text=label_text)
            label.grid(row=row, column=0, sticky="w", padx=8, pady=6)

            entry = ttk.Entry(parent, width=30)
            entry.grid(row=row, column=1, sticky="ew", padx=8, pady=6)

            self.entries[key] = entry

        parent.grid_columnconfigure(1, weight=1)

    def create_table_area(self):
        search_frame = ttk.Frame(self.table_frame)
        search_frame.pack(fill="x", padx=10, pady=8)

        ttk.Label(search_frame, text="جست‌وجو:").pack(side="top", anchor="w", padx=5)

        self.search_entry = ttk.Entry(search_frame, width=35)
        self.search_entry.pack(side="top", fill="x", padx=5, pady=5)

        button_frame = ttk.Frame(search_frame)
        button_frame.pack(side="top", fill="x", padx=5, pady=5)

        search_button = ttk.Button(
            button_frame,
            text="جست‌وجو",
            command=self.on_search_click
        )
        search_button.pack(side="left", padx=3)

        refresh_button = ttk.Button(
            button_frame,
            text="نمایش همه",
            command=self.on_refresh_click
        )
        refresh_button.pack(side="left", padx=3)

        columns = (
            "id",
            "name",
            "family",
            "phone_number",
            "nooe_melk",
            "name_of_street",
            "metrazh",
            "price_koll",
        )

        tree_container = ttk.Frame(self.table_frame)
        tree_container.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(
            tree_container,
            columns=columns,
            show="headings",
            height=22
        )

        y_scroll = ttk.Scrollbar(tree_container, orient="vertical", command=self.tree.yview)
        x_scroll = ttk.Scrollbar(tree_container, orient="horizontal", command=self.tree.xview)

        self.tree.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        y_scroll.grid(row=0, column=1, sticky="ns")
        x_scroll.grid(row=1, column=0, sticky="ew")

        tree_container.grid_rowconfigure(0, weight=1)
        tree_container.grid_columnconfigure(0, weight=1)

        self.tree.heading("id", text="شناسه")
        self.tree.heading("name", text="نام")
        self.tree.heading("family", text="خانوادگی")
        self.tree.heading("phone_number", text="موبایل")
        self.tree.heading("nooe_melk", text="نوع")
        self.tree.heading("name_of_street", text="خیابان")
        self.tree.heading("metrazh", text="متراژ")
        self.tree.heading("price_koll", text="قیمت")

        self.tree.column("id", width=55, anchor="center")
        self.tree.column("name", width=90, anchor="center")
        self.tree.column("family", width=110, anchor="center")
        self.tree.column("phone_number", width=120, anchor="center")
        self.tree.column("nooe_melk", width=90, anchor="center")
        self.tree.column("name_of_street", width=110, anchor="center")
        self.tree.column("metrazh", width=70, anchor="center")
        self.tree.column("price_koll", width=120, anchor="center")

        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        bottom_frame = ttk.Frame(self.table_frame)
        bottom_frame.pack(fill="x", padx=10, pady=8)

        prev_button = ttk.Button(
            bottom_frame,
            text="قبلی",
            command=self.prev_page
        )
        prev_button.pack(side="left", padx=3)

        next_button = ttk.Button(
            bottom_frame,
            text="بعدی",
            command=self.next_page
        )
        next_button.pack(side="left", padx=3)

        delete_button = ttk.Button(
            bottom_frame,
            text="حذف",
            command=self.on_delete_click
        )
        delete_button.pack(side="left", padx=3)

        self.status_label = ttk.Label(bottom_frame, text="")
        self.status_label.pack(side="right", padx=5)

    def get_widget_value(self, key):
        widget = self.entries[key]

        if isinstance(widget, tk.Text):
            return widget.get("1.0", tk.END).strip()

        return widget.get()

    def set_widget_value(self, key, value):
        if key not in self.entries:
            return

        if value is None:
            value = ""

        widget = self.entries[key]

        if isinstance(widget, tk.Text):
            widget.delete("1.0", tk.END)
            widget.insert("1.0", str(value))
        else:
            widget.delete(0, tk.END)
            widget.insert(0, str(value))

    def clear_widget(self, key):
        widget = self.entries[key]

        if isinstance(widget, tk.Text):
            widget.delete("1.0", tk.END)
        else:
            widget.delete(0, tk.END)

    def get_form_data(self):
        return {
            "name": self.get_widget_value("name"),
            "family": self.get_widget_value("family"),
            "phone_number": self.get_widget_value("phone_number"),
            "telephone": self.get_widget_value("telephone"),
            "nooe_melk": self.get_widget_value("nooe_melk"),
            "forosh": self.get_widget_value("forosh"),
            "name_of_street": self.get_widget_value("name_of_street"),
            "adress": self.get_widget_value("adress"),
            "metrazh": self.get_widget_value("metrazh"),
            "metrazh_mofid": self.get_widget_value("metrazh_mofid"),
            "tedad_tabaghe": self.get_widget_value("tedad_tabaghe"),
            "tedad_vahed": self.get_widget_value("tedad_vahed"),
            "tedad_khab": self.get_widget_value("tedad_khab"),
            "ashpazkhane": self.get_widget_value("ashpazkhane"),
            "asansoor": self.get_widget_value("asansoor"),
            "parking": self.get_widget_value("parking"),
            "anbari": self.get_widget_value("anbari"),
            "ab": self.get_widget_value("ab"),
            "bargh": self.get_widget_value("bargh"),
            "gaz": self.get_widget_value("gaz"),
            "telephone_melk": self.get_widget_value("telephone_melk"),
            "sand_malkiat": self.get_widget_value("sand_malkiat"),
            "ghedmat": self.get_widget_value("ghedmat"),
            "gheimat_metr_square": self.get_widget_value("gheimat_metr_square"),
            "vam_banki": self.get_widget_value("vam_banki"),
            "price_koll": self.get_widget_value("price_koll"),
            "tozihat_ezafi": self.get_widget_value("tozihat_ezafi"),
        }

    def clear_form(self):
        for key in self.entries:
            self.clear_widget(key)

        self.selected_melk_id = None

    def on_add_click(self):
        form_data = self.get_form_data()

        try:
            new_id = self.service.add_melk(form_data)
            messagebox.showinfo("موفق", f"ملک جدید ثبت شد. شناسه: {new_id}")
            self.clear_form()
            self.load_page()
        except ValueError as error:
            messagebox.showerror("خطا", str(error))
        except Exception as error:
            messagebox.showerror("خطای غیرمنتظره", str(error))

    def on_edit_click(self):
        if self.selected_melk_id is None:
            messagebox.showwarning("هشدار", "اول یک ملک را از جدول انتخاب کنید.")
            return

        form_data = self.get_form_data()

        try:
            updated_count = self.service.edit_melk(self.selected_melk_id, form_data)

            if updated_count == 0:
                messagebox.showwarning("هشدار", "هیچ ملکی ویرایش نشد.")
            else:
                messagebox.showinfo("موفق", "ملک انتخاب‌شده ویرایش شد.")

            self.clear_form()
            self.load_page()

        except ValueError as error:
            messagebox.showerror("خطا", str(error))
        except Exception as error:
            messagebox.showerror("خطای غیرمنتظره", str(error))

    def on_delete_click(self):
        if self.selected_melk_id is None:
            messagebox.showwarning("هشدار", "اول یک ملک را از جدول انتخاب کنید.")
            return

        answer = messagebox.askyesno(
            "تأیید حذف",
            "آیا مطمئن هستید که می‌خواهید این ملک را حذف کنید؟"
        )

        if not answer:
            return

        try:
            self.service.delete_melk(self.selected_melk_id)
            messagebox.showinfo("موفق", "ملک حذف شد.")
            self.clear_form()
            self.load_page()
        except ValueError as error:
            messagebox.showerror("خطا", str(error))
        except Exception as error:
            messagebox.showerror("خطای غیرمنتظره", str(error))

    def on_search_click(self):
        keyword = self.search_entry.get().strip()

        if not keyword:
            self.current_page = 1
            self.load_page()
            return

        try:
            rows = self.service.search_melk(keyword, limit=50)
            self.show_rows(rows)
            self.status_label.config(text=f"نتیجه: {len(rows)} مورد")
        except Exception as error:
            messagebox.showerror("خطا", str(error))

    def on_refresh_click(self):
        self.search_entry.delete(0, tk.END)
        self.current_page = 1
        self.load_page()

    def load_page(self):
        rows = self.service.get_melk_page(self.current_page, self.page_size)
        self.show_rows(rows)

        total = self.service.count_melk()
        self.status_label.config(
            text=f"صفحه {self.current_page} | کل: {total}"
        )

    def show_rows(self, rows):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for row in rows:
            self.tree.insert("", tk.END, values=row)

    def on_tree_select(self, event):
        selected_items = self.tree.selection()

        if not selected_items:
            return

        item = selected_items[0]
        values = self.tree.item(item, "values")

        if not values:
            return

        self.selected_melk_id = int(values[0])
        self.load_selected_melk_into_form(self.selected_melk_id)

    def load_selected_melk_into_form(self, melk_id):
        row = self.service.get_melk_by_id(melk_id)

        if row is None:
            messagebox.showerror("خطا", "ملک پیدا نشد.")
            return

        self.clear_form()
        self.selected_melk_id = melk_id

        values_map = {
            "name": row[1],
            "family": row[2],
            "telephone": row[3],
            "phone_number": row[4],
            "nooe_melk": row[5],
            "forosh": row[6],
            "name_of_street": row[7],
            "adress": row[8],
            "metrazh": row[9],
            "metrazh_mofid": row[10],
            "tedad_tabaghe": row[11],
            "tedad_vahed": row[12],
            "tedad_khab": row[13],
            "ashpazkhane": row[14],
            "asansoor": row[15],
            "parking": row[16],
            "anbari": row[17],
            "ab": row[18],
            "bargh": row[19],
            "gaz": row[20],
            "telephone_melk": row[21],
            "sand_malkiat": row[22],
            "ghedmat": row[23],
            "gheimat_metr_square": row[24],
            "vam_banki": row[25],
            "price_koll": row[26],
            "tozihat_ezafi": row[27],
        }

        for key, value in values_map.items():
            self.set_widget_value(key, value)

    def next_page(self):
        self.current_page += 1
        self.load_page()

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1

        self.load_page()
    def select_next_melk(self):
        items = self.tree.get_children()
    
        if not items:
            messagebox.showwarning("هشدار", "هیچ ملکی در لیست وجود ندارد.")
            return
    
        selected_items = self.tree.selection()
    
        if not selected_items:
            next_item = items[0]
        else:
            current_item = selected_items[0]
            current_index = items.index(current_item)
    
            if current_index >= len(items) - 1:
                messagebox.showinfo("پایان لیست", "به آخرین ملک در این صفحه رسیدید.")
                return
    
            next_item = items[current_index + 1]
    
        self.tree.selection_set(next_item)
        self.tree.focus(next_item)
        self.tree.see(next_item)
    
    
    def select_prev_melk(self):
        items = self.tree.get_children()
    
        if not items:
            messagebox.showwarning("هشدار", "هیچ ملکی در لیست وجود ندارد.")
            return
    
        selected_items = self.tree.selection()
    
        if not selected_items:
            prev_item = items[0]
        else:
            current_item = selected_items[0]
            current_index = items.index(current_item)
    
            if current_index <= 0:
                messagebox.showinfo("ابتدای لیست", "به اولین ملک در این صفحه رسیدید.")
                return
    
            prev_item = items[current_index - 1]
    
        self.tree.selection_set(prev_item)
        self.tree.focus(prev_item)
        self.tree.see(prev_item)