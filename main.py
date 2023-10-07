from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

def get_token():
    path_script = os.path.dirname(os.path.abspath(__file__))
    token_file = os.path.join(path_script, '..', 'token.txt')
    if os.path.exists(token_file):
        with open(token_file, 'r') as f:
            token = f.read()
    else:
        token = os.environ.get('GITHUB_TOKEN')
    return token


def myrepos():
    token = get_token()
    headers = {'Authorization': f'token {token}'}
    response = requests.get('https://api.github.com/user/repos', headers=headers)
    return response.json()

@app.route('/')
def index():
    # Chame a função myrepos para buscar os repositórios do GitHub
    repos = myrepos()
    
    # e passe os dados para o template HTML
    return render_template('repos.html', repos=repos)

if __name__ == '__main__':
    print('Server started!')
    app.run(debug=True, port=80)
