from flask import Flask, render_template, flash, url_for, redirect, request
import yikes

app = Flask(__name__, static_url_path='/static')

category = ""
@app.route("/", methods=['GET', 'POST'])
def layout():
    if request.method == 'POST':
        global category
        category = request.form['category']

        return redirect(url_for('waiting_screen'))
    else:
        return render_template('layout.html', title = 'Recipe Generator')

@app.route("/wait", methods=['GET', 'POST'])
def waiting_screen():
    random_recipe = yikes.get_recipes_txt(category)
    return render_template('LoadingScreen.html', title = 'Waiting Screen', url = random_recipe[0], 
            name = random_recipe[1])

if __name__ == "__main__":
    app.run()
