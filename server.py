from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/map')
def show_map():
    with open('web/map.html', 'r') as file:
        html = file.read()
    return render_template_string(html)

if __name__ == '__main__':
    app.run(port=5000)