from standard.configs.app import appConfigs
from standard.apps.mailer.mailer import Mailer


class MailService:
    sender: str = appConfigs.APP_NAME
    mailer: Mailer

    def __init__(self):
        self.mailer = Mailer()

    def send_user_registered(self, fullname: str, email: str):
        try:
            data = {
                "user": {
                    "fullname": fullname
                }
            }
            self.mailer.send(
                sender=self.sender,
                receiver=email,
                subject='Thank you for register our website!',
                template_name='user_registered',
                template_params=data,
            )
            return True
        except Exception as e:
            raise e

    def send_newsletter(self, fullname: str, email: str):
        try:
            data = {
                "user": {
                    "fullname": fullname
                }
            }
            self.mailer.send(
                sender=self.sender,
                receiver=email,
                subject='[Newsletter] Content Publishing API, Standard Community Blog, and more',
                template_name='newsletter',
                template_params=data,
            )
            return True
        except Exception as e:
            raise e

    def send_order_created(self, fullname: str, email: str):
        try:
            data = {
                "user": {
                    "fullname": fullname
                }
            }
            self.mailer.send(
                sender=self.sender,
                receiver=email,
                subject='Order Confirmation',
                template_name='order_created',
                template_params=data,
            )
            return True
        except Exception as e:
            raise e
