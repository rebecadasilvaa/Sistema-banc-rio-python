menu= """

-------------------MENU------------------
|                                       |    
| [d] Depositar                         |  
| [s] Sacar                             |  
| [e] Extrato                           |  
| [q] Sair                              |
-----------------------------------------                         
"""



saldo=0
limite=500
extrato= ""
numero_saque=0
LIMITE_SAQUES=3

while True:
    print(menu)
    opcao=(input("Digite a opção desejada: "))
    
  
    if opcao=="d":
        deposito=float(input("Digite o valor do depósito:"))

        if deposito > 0:
            saldo+=deposito
            extrato+=f"O depósito de R$ {deposito:.2f} foi efetuado com sucesso\n"
            print(extrato)                                                          
        else:
            print("Não foi possível concluir a operação. O valor fornecido não é válido.")


    elif opcao=="s":
        saque=float(input("informe o valor do saque:"))

        if saque > limite: 
            print("O valor informado excede o limite autorizado para saques") 

        elif saque > saldo:
            print("Erro na operação: saldo disponível insuficiente")   

        elif numero_saque >= LIMITE_SAQUES:
            print("A operação não foi concluída! O valor informado é inválido")  

        elif saque > 0:
            saldo-=saque
            extrato+= f"Saque R$:{saque:.2f}\n"
            numero_saque+=1
            print("Saque realizado com sucesso")
        

    elif opcao=="e":
        print("\n:::::::::::Extrato::::::::::::::")
        print("Não foram realizadas transações." if not extrato else extrato)
        print(f"Saldo R$:{saldo:.2f}")
        print(":::::::::::::::::::::::::::::::\n")

    elif opcao=="q":
        break       

    else:
        print("Operação não reconhecida. Por favor, selecione uma opção válida.")    




    

    
        
