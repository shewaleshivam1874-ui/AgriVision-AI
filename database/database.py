import os
import sqlite3
import pymysql
from pymysql.cursors import DictCursor
from config import Config

class DatabaseManager:
    """
    Database Manager managing MySQL agrivision_db and SQLite fallback.
    Provides schema migration and safe database logging.
    """
    def __init__(self):
        self.use_sqlite = False
        self._init_connection()

    def _init_connection(self):
        try:
            conn = pymysql.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                database=Config.DB_NAME,
                cursorclass=DictCursor,
                connect_timeout=3
            )
            conn.close()
            self.use_sqlite = False
            self._migrate_mysql()
            print("[DatabaseManager] Successfully connected to MySQL database.")
        except Exception as e:
            print(f"[DatabaseManager] MySQL connection unavailable ({e}). Using SQLite database fallback.")
            self.use_sqlite = True
            self._setup_sqlite()

    def get_connection(self):
        if not self.use_sqlite:
            try:
                return pymysql.connect(
                    host=Config.DB_HOST,
                    port=Config.DB_PORT,
                    user=Config.DB_USER,
                    password=Config.DB_PASSWORD,
                    database=Config.DB_NAME,
                    cursorclass=DictCursor,
                    autocommit=True
                )
            except Exception as e:
                print(f"[DatabaseManager] Re-routing to SQLite due to error: {e}")
                self.use_sqlite = True
                self._setup_sqlite()

        conn = sqlite3.connect(Config.SQLITE_DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn

    def _migrate_mysql(self):
        """Ensure MySQL tables contain all required columns."""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute("DESCRIBE prediction_history")
            columns = [row['Field'] for row in cursor.fetchall()]
            
            migrations = [
                ('confidence_level', 'VARCHAR(50)'),
                ('image_quality', 'VARCHAR(50)'),
                ('affected_area_pct', 'FLOAT'),
                ('severity_band', 'VARCHAR(50)'),
                ('full_analysis', 'TEXT')
            ]

            for col_name, col_type in migrations:
                if col_name not in columns:
                    print(f"[DatabaseManager] Migrating MySQL prediction_history: ADD {col_name}")
                    cursor.execute(f"ALTER TABLE prediction_history ADD COLUMN {col_name} {col_type}")

            conn.close()
        except Exception as e:
            print(f"[DatabaseManager] MySQL migration notice: {e}")

    def _setup_sqlite(self):
        """Create SQLite schema and migrate missing columns if table pre-existed."""
        os.makedirs(os.path.dirname(Config.SQLITE_DB_PATH), exist_ok=True)
        conn = sqlite3.connect(Config.SQLITE_DB_PATH)
        cursor = conn.cursor()

        cursor.executescript("""
        CREATE TABLE IF NOT EXISTS crops (
            crop_id INTEGER PRIMARY KEY AUTOINCREMENT,
            crop_name TEXT NOT NULL UNIQUE,
            scientific_name TEXT,
            description TEXT,
            image TEXT
        );

        CREATE TABLE IF NOT EXISTS diseases (
            disease_id INTEGER PRIMARY KEY AUTOINCREMENT,
            crop_id INTEGER NOT NULL,
            disease_name TEXT NOT NULL,
            pathogen_type TEXT,
            description TEXT,
            symptoms TEXT,
            causes TEXT,
            prevention TEXT,
            management TEXT,
            organic_solution TEXT,
            conventional_solution TEXT,
            nutrient_information TEXT,
            fertilizer_information TEXT,
            environmental_conditions TEXT,
            monitoring_guidance TEXT,
            reference_image TEXT,
            FOREIGN KEY (crop_id) REFERENCES crops(crop_id)
        );

        CREATE TABLE IF NOT EXISTS prediction_history (
            prediction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_path TEXT NOT NULL,
            crop_name TEXT NOT NULL,
            disease_name TEXT NOT NULL,
            confidence REAL NOT NULL,
            confidence_level TEXT,
            image_quality TEXT,
            affected_area_pct REAL,
            severity_band TEXT,
            heatmap_path TEXT,
            full_analysis TEXT,
            prediction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        # Migration: Ensure prediction_history has all columns
        cursor.execute("PRAGMA table_info(prediction_history)")
        columns = [row[1] for row in cursor.fetchall()]
        
        sqlite_migrations = [
            ('confidence_level', 'TEXT'),
            ('image_quality', 'TEXT'),
            ('affected_area_pct', 'REAL'),
            ('severity_band', 'TEXT'),
            ('full_analysis', 'TEXT')
        ]


        for col_name, col_type in sqlite_migrations:
            if col_name not in columns:
                print(f"[DatabaseManager] Migrating SQLite prediction_history: ADD {col_name}")
                cursor.execute(f"ALTER TABLE prediction_history ADD COLUMN {col_name} {col_type}")

        conn.commit()

        # Seed data if diseases table is empty
        cursor.execute("SELECT COUNT(*) FROM diseases")
        if cursor.fetchone()[0] == 0:
            print("[DatabaseManager] Seeding SQLite database with verified agricultural records...")
            cursor.executemany(
                "INSERT INTO crops (crop_id, crop_name, scientific_name, description, image) VALUES (?, ?, ?, ?, ?)",
                [
                    (1, 'Tomato', 'Solanum lycopersicum', 'Solanaceous vegetable crop vulnerable to fungal and bacterial blights.', 'images/sample_dataset/tomato___healthy.jpg'),
                    (2, 'Potato', 'Solanum tuberosum', 'Major tuber crop prone to Phytophthora late blight and Alternaria early blight.', 'images/sample_dataset/potato___healthy.jpg'),
                    (3, 'Pepper', 'Capsicum annuum', 'Sweet and chili pepper species susceptible to bacterial spot.', 'images/sample_dataset/pepper,_bell___healthy.jpg'),
                    (4, 'Apple', 'Malus domestica', 'Deciduous tree foliage prone to apple scab and black rot.', 'images/sample_dataset/apple___healthy.jpg'),
                    (5, 'Corn', 'Zea mays', 'Cereal crop vulnerable to gray leaf spot and common rust.', 'images/sample_dataset/corn_(maize)___healthy.jpg'),
                    (6, 'Grape', 'Vitis vinifera', 'Woody vine crop susceptible to black rot and powdery mildew.', 'images/sample_dataset/grape___healthy.jpg')
                ]
            )

            diseases_seed = [
                (
                    1, 1, 'Tomato Healthy', 'Healthy',
                    'Optimal foliage structure with no visible necrotic lesions or fungal spore structures.',
                    'Vibrant green color, smooth margins, flexible cell structure, absence of chlorosis.',
                    'Favorable environmental conditions, balanced NPK nutrition, clean irrigation.',
                    'Maintain regular watering, proper row spacing, and weekly monitoring.',
                    'Continue standard field management. Prune lower sucker shoots.',
                    'Monthly neem oil application as a preventative bio-barrier.',
                    'No chemical fungicide treatment required for healthy foliage.',
                    'Maintain Nitrogen 120-150 kg/ha, Phosphorus 60-80 kg/ha, Potassium 150-200 kg/ha.',
                    'Apply balanced N-P-K (10-10-10) during growth phase.',
                    'Optimal Temp: 20-28°C | Humidity: 50-70% | Low Disease Spread Risk.',
                    'Inspect leaves weekly for early signs of insect pests or leaf spots.',
                    'images/sample_dataset/tomato___healthy.jpg'
                ),
                (
                    2, 1, 'Tomato Early Blight', 'Fungal',
                    'Early Blight is caused by Alternaria solani forming characteristic target-spot lesions on older leaves.',
                    'Concentric bullseye dark brown spots surrounded by chlorotic yellow halos. Leaves yellow and dry.',
                    'Alternaria solani fungal spores surviving in soil debris, activated by rain splash and humidity (>80%).',
                    'Use certified disease-free seeds, practice 3-year crop rotation, stake plants, avoid overhead watering.',
                    '1. Remove severely infected lower leaves. 2. Ensure drip irrigation. 3. Avoid foliage wetness.',
                    'Foliar spray with Copper Octanoate or Bacillus subtilis bio-fungicide every 7-10 days.',
                    'Copper Hydroxide or Mancozeb protective fungicides applied according to local product label.',
                    'Potassium deficiency increases cell wall vulnerability. Calcium aids structural resistance.',
                    'Apply balanced N-P-K with extra Calcium and Magnesium; avoid excessive Nitrogen.',
                    'Optimum Temp: 24-29°C | Humidity: High (>80%) | Moderate Spread Risk.',
                    'Inspect lower foliage every 3-5 days after rain events.',
                    'images/sample_dataset/tomato___early_blight.jpg'
                ),
                (
                    3, 1, 'Tomato Late Blight', 'Fungal',
                    'Water mold Phytophthora infestans causing rapid water-soaked leaf collapse and fruit rot.',
                    'Large dark water-soaked lesions turning brown/black with white fuzzy fungal growth on undersides in morning.',
                    'Phytophthora infestans oomycete spread by wind-borne sporangia during cool, wet weather.',
                    'Plant resistant varieties, eliminate volunteer plants, space rows for rapid canopy drying.',
                    '1. Quarantine or destroy infected plants immediately. 2. Halt sprinkler irrigation.',
                    'Bordeaux mixture (Copper Sulfate + Lime) or Trichoderma viride bio-agent.',
                    'Systemic oomycete fungicides (Metalaxyl, Cymoxanil) under local agricultural guidance.',
                    'Zinc and Magnesium support foliage stress response; avoid excess free Nitrogen.',
                    'Shift to high-Potassium, low-Nitrogen liquid fertilizers during humid risk periods.',
                    'Optimum Temp: 15-22°C | Humidity: Very High (>90%) | High Rapid Spread Risk.',
                    'Inspect foliage daily during foggy, rainy weather periods.',
                    'images/sample_dataset/tomato___late_blight.jpg'
                ),
                (
                    4, 2, 'Potato Healthy', 'Healthy',
                    'Healthy potato foliage with uniform green leaf blades and sturdy erect stems.',
                    ' Crisp green leaves, sturdy stem branches, uniform texture, no spots or mildew.',
                    'Proper soil moisture, pH 5.5-6.5, balanced fertilization, clean tubers.',
                    'Rotate crops every 2-3 years, hill soil properly, inspect weekly.',
                    'Standard field upkeep, hilling, and controlled drip irrigation.',
                    'Apply compost tea foliar sprays and maintain weed-free borders.',
                    'No chemical fungicide application necessary.',
                    'High Potassium requirement for tuber cell turgor and translocation.',
                    'Apply N-P-K 10-20-20 at planting; side-dress with Potassium Sulfate.',
                    'Optimum Temp: 18-24°C | Humidity: Moderate | Low Disease Spread Risk.',
                    'Inspect foliage weekly for early beetle pests or leaf lesions.',
                    'images/sample_dataset/potato___healthy.jpg'
                ),
                (
                    5, 2, 'Potato Early Blight', 'Fungal',
                    'Alternaria solani fungal infection causing concentric ring lesions on potato foliage.',
                    'Dark brown circular lesions with concentric target rings and yellow chlorotic margins.',
                    'Overwintered Alternaria spores in crop residue splash-spread by rain and wind.',
                    'Plant certified seed tubers, rotate with non-solanaceous crops, avoid sprinkler irrigation.',
                    '1. Prune affected leaves. 2. Apply protective fungicides early in season.',
                    'Foliar spray with Copper Sulfate or Neem Seed Extract.',
                    'Contact fungicides (Chlorothalonil or Mancozeb) following label instructions.',
                    'Potassium and Phosphorus support host defense response against fungal enzymes.',
                    'Use N-P-K 8-15-15 with Magnesium and Zinc foliar supplements.',
                    'Optimum Temp: 22-28°C | Humidity: High (>75%) | Moderate Spread Risk.',
                    'Monitor lower canopy leaves every 4 days.',
                    'images/sample_dataset/potato___early_blight.jpg'
                ),
                (
                    6, 2, 'Potato Late Blight', 'Fungal',
                    'Destructive Phytophthora infestans pathogen causing foliage blight and tuber rot.',
                    'Water-soaked grey-black lesions on leaves and stems, white sporulation on leaf undersides.',
                    'Wind-blown Phytophthora sporangia activated by cool, wet weather.',
                    'Plant certified tubers, destroy cull piles, apply protective bio-fungicides.',
                    '1. Kill infected vines prior to harvest if infection exceeds 5%. 2. Keep tubers covered.',
                    'Copper hydroxide bio-fungicide or Potassium silicate sprays.',
                    'Targeted systemic fungicides applied strictly according to label instructions.',
                    'Calcium deficiency weakens tuber skin and foliage cell structure.',
                    'Avoid late Nitrogen applications; provide Potassium Sulfate and Calcium Nitrate.',
                    'Optimum Temp: 15-22°C | Humidity: High (>85%) | High Rapid Spread Risk.',
                    'Inspect fields daily during cool, rainy weather spells.',
                    'images/sample_dataset/potato___late_blight.jpg'
                ),
                (
                    7, 3, 'Pepper Healthy', 'Healthy',
                    'Healthy sweet or hot pepper leaf foliage with glossy green structure and sturdy stems.',
                    'Glossy dark green leaves, sturdy stem branches, uniform texture, no spot lesions.',
                    'Optimal soil drainage, warm temperature (20-30°C), clean irrigation water.',
                    'Ensure 45-60 cm spacing, mulching, routine pest inspection.',
                    'Routine weeding, balanced drip irrigation, gentle pruning.',
                    'Foliar spray of seaweed extract and neem oil.',
                    'No chemical treatment required.',
                    'Balanced Nitrogen and Calcium to prevent fruit blossom end rot.',
                    'Apply balanced N-P-K (12-12-17) with Calcium and Magnesium.',
                    'Optimum Temp: 20-30°C | Humidity: 50-70% | Low Disease Spread Risk.',
                    'Inspect leaves weekly for aphids or thrips.',
                    'images/sample_dataset/pepper,_bell___healthy.jpg'
                ),
                (
                    8, 3, 'Pepper Bacterial Spot', 'Bacterial',
                    'Bacterial foliage infection caused by Xanthomonas campestris pv. vesicatoria.',
                    'Small water-soaked dark green-brown spots turning necrotic with yellow halos; early leaf drop.',
                    'Xanthomonas bacteria carried on seed, splashed by rain or overhead sprinkler water.',
                    'Use disease-free seed, hot water seed treatment, rotate out of solanaceous crops 2 years.',
                    '1. Destroy severely infected plants. 2. Avoid handling wet plants.',
                    'Copper octanoate bactericide combined with Pseudomonas fluorescens.',
                    'Copper hydroxide combined with Mancozeb under local agricultural extension guidance.',
                    'Boron and Calcium support leaf cell wall integrity.',
                    'Apply N-P-K (10-10-10) with Copper, Boron, and Zinc micronutrients.',
                    'Optimum Temp: 24-32°C | Humidity: High (>80%) | Moderate-High Spread Risk.',
                    'Inspect pepper foliage every 3 days during rainy weather.',
                    'images/sample_dataset/pepper,_bell___bacterial_spot.jpg'
                )
            ]

            cursor.executemany(
                """INSERT INTO diseases (
                    disease_id, crop_id, disease_name, pathogen_type, description, symptoms, causes, 
                    prevention, management, organic_solution, conventional_solution, 
                    nutrient_information, fertilizer_information, environmental_conditions, monitoring_guidance, reference_image
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                diseases_seed
            )
            conn.commit()

        conn.close()

    def get_all_crops(self):
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM crops ORDER BY crop_name ASC")
            rows = cursor.fetchall()
            return [dict(r) if isinstance(r, sqlite3.Row) else r for r in rows]
        finally:
            conn.close()

    def get_all_diseases(self, crop_id=None):
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            if crop_id:
                placeholder = "?" if self.use_sqlite else "%s"
                sql = f"SELECT d.*, c.crop_name FROM diseases d JOIN crops c ON d.crop_id = c.crop_id WHERE d.crop_id = {placeholder} ORDER BY d.disease_name ASC"
                cursor.execute(sql, (crop_id,))
            else:
                sql = "SELECT d.*, c.crop_name FROM diseases d JOIN crops c ON d.crop_id = c.crop_id ORDER BY d.disease_name ASC"
                cursor.execute(sql)
            rows = cursor.fetchall()
            return [dict(r) if isinstance(r, sqlite3.Row) else r for r in rows]
        finally:
            conn.close()


    def get_disease_by_id(self, disease_id):
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            placeholder = "?" if self.use_sqlite else "%s"
            sql = f"SELECT d.*, c.crop_name FROM diseases d JOIN crops c ON d.crop_id = c.crop_id WHERE d.disease_id = {placeholder}"
            cursor.execute(sql, (disease_id,))
            row = cursor.fetchone()
            return dict(row) if isinstance(row, sqlite3.Row) else row
        finally:
            conn.close()

    def get_disease_by_name(self, disease_name):
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            placeholder = "?" if self.use_sqlite else "%s"
            sql = f"SELECT d.*, c.crop_name FROM diseases d JOIN crops c ON d.crop_id = c.crop_id WHERE LOWER(d.disease_name) = LOWER({placeholder})"
            cursor.execute(sql, (disease_name,))
            row = cursor.fetchone()
            if not row:
                sql_partial = f"SELECT d.*, c.crop_name FROM diseases d JOIN crops c ON d.crop_id = c.crop_id WHERE LOWER(d.disease_name) LIKE {placeholder}"
                cursor.execute(sql_partial, (f"%{disease_name.lower()}%",))
                row = cursor.fetchone()
            return dict(row) if isinstance(row, sqlite3.Row) else row
        finally:
            conn.close()

    def save_prediction(self, image_path, crop_name, disease_name, confidence, confidence_level=None, image_quality=None, affected_area_pct=None, severity_band=None, heatmap_path=None, full_analysis=None):
        """
        Safely insert prediction log into prediction_history.
        Catches any database error without raising an exception to caller.
        """
        conn = None
        try:
            import json
            full_analysis_json = None
            if full_analysis is not None:
                if isinstance(full_analysis, (dict, list)):
                    full_analysis_json = json.dumps(full_analysis, ensure_ascii=False)
                elif isinstance(full_analysis, str):
                    full_analysis_json = full_analysis

            conn = self.get_connection()
            cursor = conn.cursor()
            placeholder = "(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)" if self.use_sqlite else "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            sql = f"""
                INSERT INTO prediction_history (image_path, crop_name, disease_name, confidence, confidence_level, image_quality, affected_area_pct, severity_band, heatmap_path, full_analysis)
                VALUES {placeholder}
            """
            cursor.execute(sql, (
                image_path,
                crop_name,
                disease_name,
                float(confidence) if isinstance(confidence, (int, float)) else 90.0,
                confidence_level or "High Confidence",
                image_quality or "Good",
                float(affected_area_pct) if affected_area_pct is not None else 0.0,
                severity_band or "Moderate",
                heatmap_path,
                full_analysis_json
            ))
            if hasattr(conn, 'commit'):
                conn.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"[DatabaseManager WARNING] Could not save prediction history log: {e}")
            return None
        finally:
            if conn:
                try:
                    conn.close()
                except Exception:
                    pass

    def get_prediction_by_id(self, prediction_id):
        conn = self.get_connection()
        try:
            import json
            cursor = conn.cursor()
            placeholder = "?" if self.use_sqlite else "%s"
            sql = f"SELECT * FROM prediction_history WHERE prediction_id = {placeholder}"
            cursor.execute(sql, (prediction_id,))
            row = cursor.fetchone()
            if not row:
                return None
            res = dict(row) if isinstance(row, sqlite3.Row) else dict(row)
            if res.get('full_analysis') and isinstance(res['full_analysis'], str):
                try:
                    res['full_analysis_dict'] = json.loads(res['full_analysis'])
                except Exception:
                    res['full_analysis_dict'] = None
            else:
                res['full_analysis_dict'] = None
            return res
        finally:
            conn.close()

db_manager = DatabaseManager()
