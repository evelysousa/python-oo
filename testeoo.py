def cc(titular, numero, saldo, limite):
    conta = {"titular":titular,"numero":numero, "saldo":saldo,"limite":limite}
    return conta
def deposita(conta, valor): 
    conta["saldo"] += valor

def saca(conta, valor): 
    conta["saldo"] -= valor

def extrato(conta):
    print("Saldo é:{}".format(conta["saldo"]))




