from flask import Flask
from flask import render_template, request
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        input1 = request.form
        env = Environment(loader=FileSystemLoader('./templates'), trim_blocks=True, lstrip_blocks=True,)
        template = env.get_template('tempinterface.j2')
        result = template.render(input1)
        return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)