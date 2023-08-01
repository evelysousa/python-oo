class Conta:
    def __init__ (self,numero,titular,saldo,limite):
       print("Contruindo obejto{}". format(self))
       self.__numero = numero
       self.__titular = titular
       self.__saldo = saldo
       self.__limite = limite
       self.__codigobanco = "001"

    def extrato(self):
        print("Saldo de {} do Titular {}". format(self.__saldo,self.__titular))
        
    def deposita(self, valor):
        self.__saldo += valor 

    def podesacar(self, valor_a_sacar):
        valorsaque = self.__saldo + self.__limite
        return valor_a_sacar <= valorsaque
    
    def saca(self, valor):
        if(self.podesacar(valor)):
          self.__saldo -= valor 
        else:
            print("Você nao possui limite, o valor{}".format(valor))  

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)     

    def get_saldo(Self):
        return Self.__saldo
    
    def get_titular(Self):
        return Self.__titular 
    
    @property    
    def limite(Self):
        return Self.__limite 
    
    @limite.setter
    def set_limite(self,limite):
        self.__limite = limite

    @staticmethod
    def codigobanco():
        return "001"
    
    @staticmethod
    def codigosbancos():
        return {'BB':'001', 'CAIXA':'104', 'BRADESCO':'237'}
    
