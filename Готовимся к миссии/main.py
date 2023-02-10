from flask import Flask, render_template

app = Flask(__name__)
prof = input()

if "инженер" in prof.lower() or "строитель" in prof.lower():
    @app.route('/')
    @app.route('/training/<prof>.')
    def index():
        return render_template('base1.html', prof=prof)
else:
    @app.route('/')
    @app.route('/training/<prof>.')
    def index():
        return render_template('base.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')