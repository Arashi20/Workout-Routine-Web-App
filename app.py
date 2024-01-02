from flask import Flask, render_template, request, redirect, url_for,  send_from_directory


app = Flask(__name__)


@app.route('/')
def index():
    # The form will be here
    return "Hello, world! The Flask app is working!"  # Temporary message for testing


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get form data
        email = request.form['email']
        experience = request.form['experience']
        workout_frequency = int(request.form['workout_frequency'])

        # Logic to determine which workout plan to send based on experience and frequency
        workout_plan = determine_workout_plan(experience, workout_frequency)

         # The path to the workout plans
        workout_plan_directory = '.'   #same directory ass app.py


        # Mapping of workout plans to filenames
        workout_plan_files = {
            '2-day HIT workout plan': 'HIT-2-days.pdf',
            '3-day PPL workout plan': 'PPL-3-days.pdf',
            '4-day PPL+arms&shoulders workout plan': 'PPL-Arms-Shoulder-4-days.pdf',
            '3-day Upper/Lower+arms/shoulders workout plan': 'Upper-Lower-Shoulders-arms-3-days.pdf',
            '4-day upper/lower routine': 'Upper-Lower-4-days.pdf',
            '6-day PPL workout plan': 'PPL-6-days.pdf',
        }
             # Add any additional plans if necessary
        

        # Get the filename for the chosen workout plan
        workout_plan_filename = workout_plan_files.get(workout_plan, 'PPL-Arms-Shoulder-4-days.pdf')

        # Serve the file for download
        return send_from_directory(directory=workout_plan_directory, 
                                   filename=workout_plan_filename, 
                                   as_attachment=True)

        

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
        elif workout_frequency==3:
            return '3-day Upper/Lower+arms/shoulders workout plan'
        elif 4 <= workout_frequency <= 5:
            return '4-day PPL+arms&shoulders workout plan'
        elif workout_frequency == 6:
            return 'PPL-6-days'
    elif experience == 'Expert':
        if workout_frequency == 2:
            return '2-day HIT workout plan'
        elif workout_frequency == 3:
            return '3-day Upper/Lower+arms/shoulders workout plan'
        elif workout_frequency >= 4:
            return '4-day upper/lower routine'



@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')  # A thank you page

if __name__ == '__main__':
    app.run(debug=True)
