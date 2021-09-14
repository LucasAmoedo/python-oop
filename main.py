# encoding=utf-8
from email_provider import EmailProvider


def main():
    stop = True
    email_provider = EmailProvider("Google", "lucas.advc@gmail.com")
    email_provider.__show_password()

    while not stop:
        subject = input("Digite o assunto: ")
        body = input("Digite a mensagem: ")
        receiver = input("Digite o destinatário: ")

        email_provider.send_email(subject, body, receiver)

        resposta = input("Você deseja enviar outro e-mail? (s/n) ")

        if resposta != "s":
            stop = True

    email_provider.open_outbox()


main()