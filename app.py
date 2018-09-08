from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/pokemon/<query>', methods=['GET'])
def get_pokemon(query):	
	info = requests.get('https://pokeapi.co/api/v2/pokemon/' + query).json()	
	#check if the input is an int
	try: 
		#if this works then we already have id
		id = int(query)
		name = info['name'].capitalize()
		order = 'id'

	#if it is an exception, query is the pokemon name 
	except ValueError:
		#so extract id
		id = info['id']
		name = query.capitalize()
		order = 'name'
	
	return render_template('pokemon.html', id=id, name=name, order=order)


if __name__ == '__main__':
    app.run()
