from flask import Flask, render_template, request, redirect, url_for, flash
import os
import requests
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

# Your Baserow API token should be stored as an environment variable
BASEROW_TOKEN = os.environ.get('BASEROW_TOKEN', 'YOUR_DATABASE_TOKEN')
BASEROW_TABLE_ID =  os.environ.get('BASEROW_TABLE_ID')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    try:
        email = request.form.get('email')
        print(f"Received email: {email}") 
    
        baserow_response = requests.post(
            f"https://api.baserow.io/api/database/rows/table/{BASEROW_TABLE_ID}/?user_field_names=true",
            headers={ 
                "Authorization": f"Token {BASEROW_TOKEN}",
                "Content-Type": "application/json"
        },
    json={
        "email": email,
    }
)
        if baserow_response.status_code in (200, 201):
            flash('Thank you for subscribing!', 'success')    
        else:
            flash('Failed to add your email. Please try again later.', 'danger')
    except Exception as e:
        flash(f'An error occurred: {str(e)}', 'error')
    
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True)