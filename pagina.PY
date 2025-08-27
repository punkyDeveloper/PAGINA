#Siempre crear el entorno virtual para el proyecto. 
#Obj 
#Para crear entotno virtual: python -m venv venv
#Para activar entorno  virtual: venv\Scripts\activate
#para crear el archivo de requeriments: activate pip freeze > requirements.txt (para guardar las versiones del proyecto)

#Activar librerias:  pip install pandas openpyxl matplotlib 

#folder static
#folder es templates para organizar las paginas de html?????
    #Crear dentro de templates, archivo base.html para que sea la inicial

#PRPYECTO 3 PAG
    #PAG 1 somos
    #PAG 2 data
    #PAG 3 dashboard

#HTML escoger una opcion
#este lenguaje funciona por etiquetas:
    #DOCTYPE es etiqueta de apertura
    #/ es una etiqueta de cierre
    #head es la cabecera que describe la pag que se crea, etiquetas (es para desarrolladores)
    #atributos son las caracteristicas de la etiqueta ej: Lang= lenguaje
    #Cambiar titulo
    #Body es lo que será la pagina

#Se instaló Live Server.
#Base.hymlm click derecho ejecutar con live server (abre la pag en blanco en el navegador)

#h1 es para escribir titulos
    #cambiar style="color": escoger el color de las letras, background-color: para el fondo
#P Para parrafos
    #<p> Lorem (codigo automatico)
    #ej <p> Este proyecto busca poner en practica</p>

#Etiqueta semantica: nav, para poner el menu que se va a crear
#Etiquera de hipervinculo: a + enter, se crea href="El LINK">LO QUE QUIERO QUE SE VEA EJ CLICK AQUI</a>
#Ej  <a href="https://talentotech2.com.co/">click aqui</a>

#header Cabecera
#Nav menu
#MAin cuerpo
#Fouter Final

#pip install flask (libreria que conserva el header)
# app = Flask(__name__) (inicio del aplicativo)
# @app.route("/") (ruta)

#Cambiar la ruta x incluir flask
#En la terminal py index.py

#Para el ejercicio se usa:@app.route('/dashboard')
def Dashboard():
    df = pd.read_json("productos.json")
    top5 = df.sort_values(by="vendidos", ascending=False).head() # Ordena de mayor a menor
    plt.figure(figsize=(10,6)) # crea el espacio del gráfico en matplotlib indicando el ancho y alto
    plt.bar(top5["producto"], top5["vendidos"], color='salmon')
    plt.title("Top 5 Productos Más Vendidos")
    plt.xlabel("Producto")
    plt.ylabel("Unidades Vendidas")
    plt.grid(axis='y')
    plt.tight_layout()
  
    # Guardar la gráfica
    plt.savefig("Proyecto/Proyecto/static/top5.png")
    return render_template('Dashboard.html')

# se cambia con las graficas del proyecto