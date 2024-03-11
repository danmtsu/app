class Gas_station():
    def __init__(self, name:str, address:str, city:str, state:str, preco_etanol:float=None, preco_gasolina:float=None,preco_diesel:float=None):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.preco_etanol = preco_etanol
        self.preco_gasolina = preco_gasolina
        self.preco_diesel = preco_diesel

    def __repr__(self):
        return f"<Posto {self.name}>"
