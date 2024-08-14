# Imports
from flask import Flask, render_template, request, redirect

# Create app Flask
app = Flask(__name__)

# ROUTES 
@app.route('/')
def homepage():
    return render_template('homepage.html')

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@app.route('/prime', methods=['GET', 'POST'])
def prime_number():
    result = None
    divisible2 = ""  # Iniciar divisible2 como string vazia

    if request.method == 'POST':
        number = request.form.get('number')
        if number:
            try:
                number = int(number)
                result = is_prime(number)
                if number % 2 == 0:
                    divisible2 = "divisible by 2"
                elif not result and number % 3 == 0:
                    divisible2 = "divisible by 3"
            except ValueError:
                result = "Please enter a valid number."
        else:
            result = "No number provided."

    return render_template('prime.html', result=result, divisible2=divisible2)


@app.route('/delete', methods=['POST'])
def delete():
    return redirect('/prime')



@app.route('/sort', methods=['GET', 'POST'])
def sort_number():
    sorted_numbers = None
    if request.method == 'POST':
        numbers = [
            request.form.get('number1', type=int),
            request.form.get('number2', type=int),
            request.form.get('number3', type=int),
            request.form.get('number4', type=int),
            request.form.get('number5', type=int),
            request.form.get('number6', type=int),
            request.form.get('number7', type=int),
            request.form.get('number8', type=int),
            request.form.get('number9', type=int),
            request.form.get('number10', type=int),
        ]
        sorted_numbers = sorted(filter(None, numbers))  # Filtrar valores none e ordenaR os números
    return render_template('sort.html', sorted_numbers=sorted_numbers)

@app.route('/clear', methods=['POST'])
def clear_form():
    return redirect('/sort')


if __name__ == '__main__': #significa que caso esteja sendo usado por outro arquivo não vai ser usado
    app.run(debug=True) #ativar debugar




