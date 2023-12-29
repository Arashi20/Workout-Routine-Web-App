from flask import Flask, render_template, request, redirect, url_for
# Add your email sending library import here, for example Flask-Mail

app = Flask(__name__)

# Configure your email settings here

@app.route('/')
def index():
    return render_template('index.html')  # The form will be here

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get form data
        email = request.form['email']
        experience = request.form['experience']
        workout_frequency = int(request.form['workout_frequency'])

        # Logic to determine which workout plan to send based on experience and frequency
        workout_plan = determine_workout_plan(experience, workout_frequency)

        # Send the email with the workout plan (You will need to implement this)
        send_email(email, workout_plan)

        return redirect(url_for('thank_you'))

def determine_workout_plan(experience, workout_frequency):
    if experience == 'Newbie':
        if workout_frequency == 2:
            return '2-day HIT workout plan'
        elif workout_frequency >= 3:
            return '3-day PPL workout plan'
    elif experience == 'Intermediate':
        if workout_frequency == 2:
            return '2-day HIT workout plan'
        elif workout_frequency == 3:
            return '3-day PPL workout plan'
        elif workout_frequency > 3:
            return '4-day PPL+arms&shoulders workout plan'
    elif experience == 'Advanced':
        if workout_frequency == 2:
            return '2-day HIT workout plan'
        elif 3 <= workout_frequency <= 5:
            return '4-day PPL+arms&shoulders workout plan'
        elif workout_frequency == 6:
            return '6-day PPL workout plan'
    elif experience == 'Expert':
        if workout_frequency == 2:
            return '2-day HIT workout plan'
        elif workout_frequency == 3:
            return '3-day Upper/Lower+arms/shoulders workout plan'
        elif workout_frequency >= 4:
            return '4-day upper/lower routine'

def send_email(app, mail, recipient, workout_plan):
    # Define your email sender
    sender_email = 'your-email@example.com'  # Replace with your email

    # Create a message object
    msg = Message("Your Personalized Workout Plan", sender=sender_email, recipients=[recipient])

    # Email body
    msg.body = f"""
    Hi (new) gymrat!

    I am thrilled that you have decided to indulge yourself in the world of fitness and weightlifting. With this, I would like to send you the promised workout plan that you can follow to become the greatest version of yourself! Feel free to make any minor changes to your routine or ask for a new one, in case your preferences have changed!

    I would like to thank you for your time and trust in me, I can assure you that the plan will be of great use to you ;)

    Greetings,
    Arash
    """

    # Logic to determine the path of the PDF file based on the workout_plan variable
    pdf_mappings = {
    "2-day HIT workout plan": "/home/www/HIT-2-days.pdf",
    "3-day PPL workout plan": "/home/www/PPL-3-days.pdf",
    "6-day PPL workout plan": "/home/www/PPL-6-days.pdf",
    "4-day PPL+Arms+Shoulder workout plan": "/home/www/PPL-Arms-Shoulder-4-days.pdf",
    "4-day Upper/Lower workout plan": "/home/www/Upper-Lower-4-days.pdf",
    "3-day Upper/Lower+Shoulders+Arms workout plan": "/home/www/Upper-Lower-Shoulders-arms-3-days.pdf",
    # Continue adding mappings for other workout plans
}

    pdf_file_path = pdf_mappings.get(workout_plan, "/home/www/default_plan.pdf")  # Replace with the actual default PDF path

    # Ensure the application context is pushed before sending the email
    with app.app_context():
        # Check if the file exists
        if os.path.isfile(pdf_file_path):
            with app.open_resource(pdf_file_path) as fp:
                msg.attach("workout_plan.pdf", "application/pdf", fp.read())
        
        # Send the email
        mail.send(msg)


@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')  # A thank you page

if __name__ == '__main__':
    app.run(debug=True)
