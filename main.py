from flask import Flask, render_template, request, redirect, url_for, flash
import os
import vercel_blob 

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form.get('email')
        
        # Basic email validation
        if not email or '@' not in email:
            flash('Please enter a valid email address.', 'error')
            return redirect(url_for('home'))
        
        # Append to blob storage
        try:
            # Try to download existing content
            try:
                existing_content = vercel_blob.get('email_signups.csv').download().decode('utf-8')
            except:
                existing_content = 'Email\n'
            
            # Append new email
            updated_content = existing_content + f"{email}\n"
            
            # Upload updated content
            vercel_blob.put('email_signups.csv', updated_content.encode('utf-8'))
            
            flash('Thank you for signing up!', 'success')
        except Exception as e:
            flash(f'An error occurred: {str(e)}', 'error')
        
        return redirect(url_for('home'))
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)