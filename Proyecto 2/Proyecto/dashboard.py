from flask import Flask, render_template # Flask es un framework para desarrollar paginas web
import pandas as pd
import matplotlib.pyplot as plt

# Asegúrate de que esta línea esté aquí
app = Flask(__name__)  # __name__ es una variable especial de python que contiene el nombre
                       # del módulo actual, es decir aqui se crea la app
                       # dicho de otra forma crea una instancia de la app web

# @ es un decorador, que le dice a flask cuando visite la url, ejecuta la ruta
# Una Ruta es la dirección en la url, que das para acceder a una parte de la aplicación web
@app.route('/')        
def somos():                # def, es para definir la función en python
    return render_template('somos.html')   # render_template, envia al usuario a una pagina html

@app.route('/datos')
def datos():
    df = pd.read_json("productos.json")
    # to_html Convierte ese DataFrame en una tabla HTML. Index false es para que no incluya los indices de las filas
    tabla_html = df.to_html(classes='table table-striped', index=False) 
    return render_template('datos.html', tabla=tabla_html)

@app.route('/dashboard')
def dashboard():
    df = pd.read_json("productos.json")
    top5 = df.sort_values(by="vendidos", ascending=False).head(5) # Ordena de mayor a menor

    plt.figure(figsize=(10, 6)) # crea el espacio del gráfico en matplotlib indicando el ancho y alto
    plt.bar(top5["producto"], top5["vendidos"], color='salmon')
    plt.title("Top 5 Productos Más Vendidos")
    plt.xlabel("Producto")
    plt.ylabel("Unidades Vendidas")
    plt.grid(axis='y')
    plt.tight_layout()

    # Guardar la gráfica
    plt.savefig("static/top5_productos.png")
    return render_template('dashboard.html')

# 👇 ESTE BLOQUE ES IMPORTANTE Y DEBE ESTAR AL FINAL DEL ARCHIVO 👇
if __name__ == '__main__':
    print("Iniciando servidor Flask...")
    app.run(debug=True)  # empiece a escuchar peticiones en el puerto 5000
    # debug Muestra errores detallados en el navegador (muy útil para desarrollo)
