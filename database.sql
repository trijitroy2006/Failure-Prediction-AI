CREATE TABLE IF NOT EXISTS projects (
 id SERIAL PRIMARY KEY,
 startup_name VARCHAR(150) NOT NULL,
 industry VARCHAR(100) NOT NULL,
 business_model VARCHAR(100) NOT NULL,
 target_market VARCHAR(150),
 budget NUMERIC(15,2),
 project_description TEXT,
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS swot_analysis (
    swot_id SERIAL PRIMARY KEY,
    project_id INT REFERENCES projects(id) ON DELETE CASCADE,
    strengths TEXT,
    weaknesses TEXT,
    opportunities TEXT,
    threats TEXT,
    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS risk_assessments (
    risk_id SERIAL PRIMARY KEY,
    project_id INT REFERENCES projects(id) ON DELETE CASCADE,
    risk_category VARCHAR(100),
    risk_score NUMERIC(5,2),
    risk_description TEXT,
    priority_level VARCHAR(50)
);