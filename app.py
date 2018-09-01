from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<query>', methods=['GET'])
def get_pokemon(query):	
	info = requests.get('https://pokeapi.co/api/v2/pokemon/' + query).json()	
	pokemon = info['forms'][0]['name']
	return render_template('pokemon.html', query=query, pokemon=pokemon)



if __name__ == '__main__':
    app.run()
