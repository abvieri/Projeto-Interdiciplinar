# Importando do módulo flask a classe Flask realizando um requerimento a render_template
from flask import Flask, request, render_template

# Criando uma instância da classe Flask chamada "app"
# O parametro "(__name__)" é uma váriavel pré-definida que representa o nome do módulo atual. 
app = Flask(__name__)

# Criando uma função para converter as bases numéricas
def converter(numero, base_inicial, base_final):
    try:
        # Convertendo para decimal primeiro
        decimal = int(numero, base_inicial)

        # Convertendo de decimal para a base final
        if base_final == 2:
            resultado = bin(decimal)
        elif base_final == 8:
            resultado = oct(decimal)
        elif base_final == 10:
            resultado = decimal
        elif base_final == 16:
            resultado = hex(decimal)

        # Retorna o valor da conversão se estiver correta, se não, mostra um aviso de erro
        return resultado
    except ValueError:
        return "Erro: Certifique-se de que o número e as bases estão corretos."

# Criando um decorador em flask que é usado para vincular uma função a uma URL especifica
# Neste caso essa função decorada será chamada sempre que acessarem a URL principal
@app.route('/')
def index():
    return render_template("index.html")

# Criando um decorador em flask que é usado para vincular uma função a uma URL especifica
# Neste caso depois da conversão será entregue o resultado na URL de resultados 
@app.route('/converter', methods=['POST'])
def converter_base():
    numero = request.form['numero']
    base_inicial = int(request.form['base_inicial'])
    base_final = int(request.form['base_final'])

    resultado = converter(numero, base_inicial, base_final)

    return render_template("resultado.html", resultado=resultado)

# Criando uma construção que verifica se o script está sendo executado diretamente
# O parametro "(debug=Time)" ativa o modo de depuração, que fornece informações detalhadas sobre os erros e recarrega automaticamente quando você faz alterações no codigo 
if __name__ == '__main__':
    app.run(debug=True)
