# =====Imports===== #
import classification
# =====Imports===== #


# =====Dados - Data===== #
nome = "JapaScripter"  # input("Coloque nome do remetente: ")
sdemail = "seuemail@gmail.com"  # input("Coloque seu e-mail: ")
password = "suasenha"  # input("Coloque a senha do seu e-mail: ")
rcemail = "ciclano@gmail.com"  # input("Coloque o e-mail destinatário: ")
ccemail = "fulano@gmail.com", "beltrano@gmail.com"  # input("Coloque o(s) e-mail(s) em cópia: ")
ccoemail = ""
text = "Parabéns o teste foi um teste"
anexo = "1"
# =====Dados - Data===== #


# =====Pegar Classe - Get Class===== #
try:
    classification.DadosEnvio(nome, sdemail, password, rcemail, ccemail, ccoemail, text, anexo)

except Exception as e:
    print(f'Deu erro, procura ai filho! \n{e}')
# =====Pegar Classe - Get Class===== #
