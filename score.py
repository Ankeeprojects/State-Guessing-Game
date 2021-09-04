class Score:
    def __init__(self):
        self.pontuacao = 0

    def incrementa_pontuacao(self):
        self.pontuacao += 1

    def get_pontuacao(self):
        return self.pontuacao