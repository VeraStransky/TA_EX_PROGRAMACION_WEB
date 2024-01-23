from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = (request.form['nombre'])
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])
        precio_tarro = 9000
        total_sin_descuento = tarros * precio_tarro

        # Condiciones de Compras

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        # Calculo de Compras

        total_con_descuento = total_sin_descuento * (1 - descuento)

        resultado = True


        # Definir la variable resultado


        return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, total_con_descuento=total_con_descuento, resultado=resultado, descuento=descuento)

    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():

    nombres = {
        "juan": "admin123",
        "pepe": "usuario456"
    }
    mensaje = None

    if request.method == 'POST':
        # Obtener Los datos del Formulario

        nombre = (request.form['nombre'])
        contraseña = str(request.form['contraseña'])


        # Verificar las credenciales
        if nombre == 'juan' and contraseña == nombres['juan']:
            mensaje = f"Bienvenido Administrador {nombre.capitalize()}"
        elif nombre == 'pepe' and contraseña == nombres['pepe']:
            mensaje = f"Bienvenido Usuario {nombre.capitalize()}"
        else:
            mensaje = "Usuario o contraseña incorrectos."


    return render_template('ejercicio2.html', mensaje=mensaje)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
