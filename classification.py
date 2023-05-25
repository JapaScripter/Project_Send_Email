# =====Imports===== #
import ssl
import smtplib
from email.message import EmailMessage
# =====Imports===== #




# =====Classe de Dados - Data Class===== #
class DadosEmail:
    def __init__(self, nome, sdemail, password, rcemail, ccemail, ccoemail, text, anexo):
        self.nome = nome
        self.sdemail = sdemail
        self.password = password
        self.rcemail = rcemail
        self.ccemail = ccemail
        self.ccoemail = ccoemail
        self.text = text
        self.anexo = anexo
# =====Classe de Dados - Data Class===== #




# =====Herança de Envio - Send Heritage===== #
class DadosEnvio(DadosEmail):
    def __init__(self, nome, sdemail, password, rcemail, ccemail, ccoemail, text, anexo):
        # Remetente, recebedor e senha
        super().__init__(nome, sdemail, password, rcemail, ccemail, ccoemail, text, anexo)
        email_sender = f'{sdemail}'
        email_password = f'{password}'
        email_receiver = f'{rcemail}'
        email_receivercc = f'{ccemail}'
        email_receivercco = f'{ccoemail}'
        # =====Herança de Envio - Send Heritage===== #

        # =====Assunto e Corpo de Texto - Subject and Text Body===== #
        subject = f'Parabéns {nome}'
        body = f"""{text}"""
        # =====Assunto e Corpo de Texto - Subject and Text Body===== #

        # =====Cabeçalho Email - Email Header===== #
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Cc'] = email_receivercc
        em['Cco'] = email_receivercco
        em['Subject'] = subject
        em.set_content(body)
        # =====Cabeçalho Email - Email Header===== #

        # =====Anexar Documento - Doc Attachment===== #
	# Enviar texto descrito no anexo - Send description text inside at attach
        with open('Receba.txt') as myfile:
            data = myfile.read()
            em.set_content(data)

	# Enviar anexo - Send attach
        if self.anexo == "1":
            with open('Receba.txt', 'rb') as attachment:
                file_data = attachment.read()
                print("File data in binary", file_data)
                file_name = attachment.name
                print("File name is", file_name)
                em.add_attachment(file_data, maintype="application", subtype="txt", filename=file_name)

                context = ssl.create_default_context()
        # =====Anexar Documento - Doc Attachment===== #

        # =====Envio - Sender===== #
        try:
            email_receivers = [email_receiver] + [email_receivercc] + [email_receivercco]
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receivers, em.as_string())
                print('E-mail enviado com sucesso... será? Verifique, não tenho certeza.')
        except Exception as e:
            print(f'Deu erro, procura ai filho! \n{e}')
# =====Envio - Sender===== #
