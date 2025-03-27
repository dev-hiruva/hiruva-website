# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
import csv
import os

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']  # Change this to a random secret key

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form.get('email')
        
        # Basic email validation
        if not email or '@' not in email:
            flash('Please enter a valid email address.', 'error')
            return redirect(url_for('home'))
        
        # Append to CSV
        try:
            with open('email_signups.csv', 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([email])
            
            flash('Thank you for signing up!', 'success')
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
        
        return redirect(url_for('home'))
    
    return render_template('index.html')

if __name__ == '__main__':
    # Ensure CSV file exists
    if not os.path.exists('email_signups.csv'):
        with open('email_signups.csv', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Email'])
    
    app.run(debug=True)