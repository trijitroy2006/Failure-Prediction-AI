from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import database
import market_analysis
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        project_data = {
            'startup_name': request.form.get('startup_name'),
            'industry': request.form.get('industry'),
            'business_model': request.form.get('business_model'),
            'target_market': request.form.get('target_market'),
            'budget': request.form.get('budget'),
            'project_description': request.form.get('project_description')
        }
        try:
            project_id = database.insert_project(project_data)
            session['project_id'] = project_id
        except Exception as e:
            print(f"Database error: {e}")
            session['fallback_project_data'] = project_data
            
        return redirect(url_for('dashboard'))
        
    project_id = session.get('project_id')
    project = session.get('fallback_project_data')
    
    if project_id:
        try:
            db_project = database.get_project(project_id)
            if db_project:
                project = db_project
        except Exception as e:
            print(f"Database error fetching project: {e}")

    industry = "Technology"
    startup_name = ""
    target_market = ""
    budget = 0
    business_model = "SaaS"

    if project:
        industry = project.get('industry', 'Technology')
        startup_name = project.get('startup_name', '')
        target_market = project.get('target_market', '')
        business_model = project.get('business_model', 'SaaS')
        try:
            budget = float(project.get('budget', 0))
        except:
            budget = 0

    market_data = market_analysis.get_market_data(industry, target_market, budget)
    competitors = market_analysis.get_competitor_data(startup_name, industry, business_model)
    
    return render_template('dashboard.html', market_data=market_data, competitors=competitors, project=project)

@app.route('/risk_assessment')
def risk_assessment():
    project_id = session.get('project_id')
    project = session.get('fallback_project_data')
    
    if project_id:
        try:
            db_project = database.get_project(project_id)
            if db_project:
                project = db_project
        except Exception as e:
            print(f"Database error fetching project: {e}")

    import risk_analysis
    scores = risk_analysis.calculate_risk_scores(project)
    swot = risk_analysis.generate_swot(project)

    return render_template('risk_assessment.html', project=project, scores=scores, swot=swot)

@app.route('/api/analyze', methods=['POST'])
def api_analyze():
    data = request.json
    industry = data.get('industry', 'Technology')
    startup_name = data.get('startup_name', '')
    target_market = data.get('target_market', '')
    business_model = data.get('business_model', 'SaaS')
    try:
        budget = float(data.get('budget', 0))
    except:
        budget = 0
        
    market_data = market_analysis.get_market_data(industry, target_market, budget)
    competitors = market_analysis.get_competitor_data(startup_name, industry, business_model)
    
    return jsonify({
        "market_data": market_data,
        "competitors": competitors
    })

@app.route('/placeholder')
def placeholder():
    return render_template('placeholder.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
