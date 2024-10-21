from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'patitoxd'

# contraseñas
usuarios = {
    'geo': '123',
    'jhos': '1234'
}

@app.route('/')
def inicio():
    if 'nombre_usuario' in session:
        return redirect(url_for('bienvenida'))
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['username']  
        contrasena = request.form['password'] 
        
        # Autenticación simple
        if usuario in usuarios and usuarios[usuario] == contrasena:
            session['nombre_usuario'] = usuario  # Guardar en la sesión
            return redirect(url_for('bienvenida'))
        error = 'Usuario o contraseña incorrectos'
        return render_template('login.html', error=error)
    return render_template('login.html')
 

@app.route('/bienvenida')
def bienvenida():
    if 'nombre_usuario' in session:
        return render_template('bienvenida.html', mostrar_usuario=session['nombre_usuario'])
    return redirect(url_for('login'))

@app.route('/eliminar')
def eliminar():
    session.pop('nombre_usuario', None)  # Eliminar el usuario de la sesión
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
