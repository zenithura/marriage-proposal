from flask import Flask, render_template, request, url_for 

app = Flask(__name__)

@app.route('/')
def index():
    # URL'den isimleri al, eğer yoksa varsayılan olarak 'Boy' ve 'Girl' kullan
    first_name = request.args.get('first', 'Boy')
    second_name = request.args.get('second', 'Girl')
    
    return render_template('index.html', first_name=first_name, second_name=second_name)

if __name__ == '__main__':
    app.run(debug=True)
