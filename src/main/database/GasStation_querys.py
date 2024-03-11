from .connect_db import create_database

class GasStationQuery:
    def __init__(self,):
        self.mydb = create_database('localhost', 'root', 'root', 'gas_stations')
        self.cursor = self.mydb.cursor()

    def create_gas_station(self, data):
        if self.gas_station_exist(data['address'],data['city'],data['state']):
            return 'Endereço já cadastrado'
        else:
            sql = "INSERT INTO gas_station (nome, address, estado, cidade, preco_etanol, preco_gasolina, preco_diesel) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            self.cursor.execute(sql, (data['name'], data['address'], data['state'], data['city'], data['preco_etanol'], data['preco_gasolina'], data['preco_diesel']))
            self.mydb.commit()
            return 'Posto criado com sucesso'

    def update_gas_station(self,data, id:int):
        message = None
        if self.gas_station_listBy(id=id):
            sql = "UPDATE gas_station SET nome=%s, address=%s, estado=%s, cidade=%s, preco_etanol=%s, preco_gasolina=%s, preco_diesel=%s WHERE id=%s"
            self.cursor.execute(sql,(      
                data['name'],
                data['address'],
                data['state'],
                data['city'],
                data['preco_etanol'],
                data['preco_gasolina'],
                data['preco_diesel'],
                id))
            self.mydb.commit()
            message = 'Posto atualizado com sucesso'
        else:
            message = 'Posto não encontrado'
        return message
            
    def delete_gas_station(self, id: int):
        if self.gas_station_exist(id=id):
            sql = 'DELETE FROM gas_station WHERE id = %s'
            self.cursor.execute(sql, (id,))
            self.mydb.commit()
            return "Gas station has been deleted"
        return "Gas station not found"

        

    def gas_station_exist(self, address: str = None, cidade: str = None, estado: str = None, id=None):
        if id is not None:
            self.cursor.execute("SELECT * FROM gas_station WHERE id = %s", (id,))
            return self.cursor.fetchone() is not None
        else:
            self.cursor.execute("SELECT * FROM gas_station WHERE address = %s AND estado = %s AND cidade = %s", (address, estado, cidade))
            return self.cursor.fetchone() is not None


        
    def gas_station_listBy(self, id=None, city=None, state=None, address=None):
        sql = 'SELECT * FROM gas_station'
        conditions = []
        values = []

        if id is not None:
            conditions.append('id = %s')
            values.append(id)
        if city is not None:
            conditions.append('city = %s')
            values.append(city)
        if state is not None:
            conditions.append('state = %s')
            values.append(state)
        if address is not None:
            conditions.append('address = %s')
            values.append(address)

        if conditions:
            sql += ' WHERE ' + ' AND '.join(conditions)

        self.cursor.execute(sql, values)
        return self.cursor.fetchall()        