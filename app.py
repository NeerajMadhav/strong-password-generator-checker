from flask import Flask, render_template
import random as r
from password_strength import PasswordStats

app = Flask(__name__)

def passwordGenerator():
    alpha_lo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alpha_hg = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    integers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    spl_char = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
    ans = []

    for i in range(3):
        ans.append(r.choice(alpha_hg))
        ans.append(r.choice(alpha_lo))
        ans.append(r.choice(integers))
        ans.append(r.choice(spl_char))
        ans.append(r.choice(spl_char))
        ans.append(r.choice(alpha_lo))
        ans.append(r.choice(integers))
    r.shuffle(ans)
    password = ""

    for x in range(len(ans)):
        password += ans[x]
        
    return password

@app.route('/')
def home():
    password = passwordGenerator()
    stats = PasswordStats(password)
    strength = stats.strength()
    str=(strength*100)/1
    return render_template('index.html', password=password, strength=str)

if __name__ == '__main__':
    app.run(debug=True)
    