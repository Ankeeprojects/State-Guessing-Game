import turtle
import pandas
import score

FONT = ("Arial", 18, "bold")

screen = turtle.Screen()
pontos = score.Score()

screen.bgpic("blank_states_img.gif")

dados = pandas.read_csv("50_states.csv")
estados = dados.state.to_list()
continua = True
acertadas = []

while continua:
    if pontos.get_pontuacao() == 0:
        resposta = screen.textinput(title="Guess a state", prompt="Write the name of a state:").title()
    else:
        resposta = screen.textinput(title=f"{pontos.get_pontuacao()}/50 states guessed", prompt="Write the name of a state:").title()




    if resposta == "Exit":
        continua = False
    elif resposta in estados and resposta not in acertadas:
        coords = dados[dados.state == resposta]
        estado = turtle.Turtle()
        estado.penup()
        estado.hideturtle()
        estado.goto(int(coords.x), int(coords.y))
        estado.write(resposta,False,"center", FONT)

        acertadas.append(resposta)
        pontos.incrementa_pontuacao()

        if len(acertadas) == 50:
            continua = False


falhadas = {"state": [estado for estado in estados if estado not in acertadas]}

pandas.DataFrame(falhadas).to_csv("falhadas.csv")

screen.exitonclick()
