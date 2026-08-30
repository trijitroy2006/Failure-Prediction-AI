import psycopg2
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
    "dbname": "ml_project",
    "user": "postgres",
    "password": "YOUR_POSTGRES_PASSWORD",
    "host": "localhost",
    "port": "5432"
}

def get_db_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn

def insert_project(data):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO projects (startup_name, industry, business_model, target_market, budget, project_description)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id;
    ''', (
        data['startup_name'],
        data['industry'],
        data['business_model'],
        data['target_market'],
        data['budget'],
        data['project_description']
    ))
    project_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return project_id

def get_project(project_id):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM projects WHERE id = %s;', (project_id,))
    project = cur.fetchone()
    cur.close()
    conn.close()
    return project
