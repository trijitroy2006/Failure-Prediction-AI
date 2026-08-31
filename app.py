from flask import Flask, render_template, request, redirect, url_for, session
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
            # Fallback if DB is not set up correctly by user
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

    if project:
        industry = project.get('industry', 'Technology')
        startup_name = project.get('startup_name', '')
        target_market = project.get('target_market', '')

    market_data = market_analysis.get_market_data(industry, target_market)
    competitors = market_analysis.get_competitor_data(startup_name, industry)
    
    return render_template('dashboard.html', market_data=market_data, competitors=competitors, project=project)

@app.route('/placeholder')
def placeholder():
    return render_template('placeholder.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
