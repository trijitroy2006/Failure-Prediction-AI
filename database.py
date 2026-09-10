import psycopg2
from psycopg2.extras import RealDictCursor

DB_CONFIG = {
    "dbname": "ml_project",
    "user": "postgres",
    "password": "12345678",
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

def insert_swot_analysis(project_id, swot_data):
    conn = get_db_connection()
    cur = conn.cursor()

   
    strengths_list = swot_data.get('Strengths', [])
    weaknesses_list = swot_data.get('Weaknesses', [])
    opportunities_list = swot_data.get('Opportunities', [])
    threats_list = swot_data.get('Threats', [])

    strengths = ", ".join(strengths_list) if strengths_list else "N/A"
    weaknesses = ", ".join(weaknesses_list) if weaknesses_list else "N/A"
    opportunities = ", ".join(opportunities_list) if opportunities_list else "N/A"
    threats = ", ".join(threats_list) if threats_list else "N/A"

    cur.execute('''
        INSERT INTO swot_analysis (project_id, strengths, weaknesses, opportunities, threats)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING swot_id;
    ''', (project_id, strengths, weaknesses, opportunities, threats))

    swot_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return swot_id
def insert_risk_assessment(project_id, risk_category, risk_score, risk_description, priority_level):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO risk_assessments (project_id, risk_category, risk_score, risk_description, priority_level)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING risk_id;
    ''', (project_id, risk_category, risk_score, risk_description, priority_level))
    risk_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return risk_id
