import os
import smtplib
import socket
from email.mime.text import MIMEText

from jinja2 import Environment, FileSystemLoader
from . import minifier
from .config import mailerConfigs


class Mailer:

    PREFIX = mailerConfigs.MAIL_APP_NAME
    TEMPLATES_DIR = mailerConfigs.MAIL_TEMPLATES_DIR
    TEMPLATE_USER_REGISTERED = 'user_registered.minify.html'
    TEMPLATE_ORDER_CREATED = 'order_created.minify.html'
    TEMPLATE_NEWSLETTER = 'newsletter.minify.html'
    TEMPLATE_FORGOT_PASSWORD = 'forgot_password.minify.html'

    @staticmethod
    def send_demo_smtp_mail():
        try:
            sender = "Standard Mail <from@example.com>"
            receiver = "A Test User <to@example.com>"
            message = MIMEText("This is a test e-mail message.")
            message["Subject"] = "Hi Mailtrap"
            message["From"] = sender
            message["To"] = receiver
            with smtplib.SMTP(mailerConfigs.MAIL_HOST, 2525) as server:
                if mailerConfigs.MAIL_TLS:
                    server.starttls()
                server.login(mailerConfigs.MAIL_USERNAME, mailerConfigs.MAIL_PASSWORD)
                server.sendmail(sender, receiver, message.as_string())
            return True
        except socket.error as e:
            print("[MAILER] Could not connect to smtp server")
            print(e)
            return False

    def send(self, sender: str, receiver: str, subject: str, body: str = '',
             template_name: str = '', template_params: dict = {},
             attachments: list = []):
        try:
            if template_name:
                body = self.render_from_template(data=template_params, template_name=template_name)
                message = MIMEText(body, 'html')
            else:
                message = MIMEText(body, 'plain')
            message["Subject"] = subject
            message["From"] = sender
            message["To"] = receiver
            with smtplib.SMTP(mailerConfigs.MAIL_HOST, int(mailerConfigs.MAIL_PORT)) as server:
                if mailerConfigs.MAIL_TLS:
                    server.starttls()
                server.login(mailerConfigs.MAIL_USERNAME, mailerConfigs.MAIL_PASSWORD)
                server.sendmail(sender, receiver, message.as_string())
            return True
        except socket.error as e:
            print("[MAILER] Could not connect to smtp server")
            print(e)
            return False

    def render_from_template(self, data, template_name, overwrite_minify: bool = False):
        # Minify templates file
        template_file = f'{self.TEMPLATES_DIR}/{template_name}.html'
        template_file_minified = f'{self.TEMPLATES_DIR}/{template_name}.min.html'

        if not os.path.isfile(template_file_minified) or overwrite_minify:
            minifier.minify(input_file=template_file, output_file=template_file_minified)

        # Parse templates data from minified templates
        file_loader = FileSystemLoader(self.TEMPLATES_DIR)
        env = Environment(loader=file_loader)
        template_min = f'{template_name}.min.html'
        template = env.get_template(template_min)
        output = template.render(data)
        return output
