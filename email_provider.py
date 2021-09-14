from email_message import EmailMessage


class EmailProvider:
    def __init__(self, company, address):
        self.company = company
        self.address = address
        self.inbox = []
        self.outbox = []

    def __show_password(self):
        return "minhasenha"

    def protect_password(self):
        password = self.__show_password()
        print(password[:3])


    def send_email(self, subject, body, receiver):
        email = EmailMessage(
            subject,
            body,
            self.address,
            receiver
        )
        email.subject()
        email.get_subject()
        email.set_subject("assunto novo")

        self.outbox.append(email)

    def open_outbox(self):
        for email in self.outbox:
            print("[*]", email.subject)