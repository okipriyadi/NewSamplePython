"""
Making this function into a task is as simple as importing our Celery object and adding a decorator (almost).

Recall that when we instantiated our Celery daemon we handed it a list of relative paths. One of those was to this file 
'framework.email.email_tasks'. When Celery is started it will comb over any files in that list and look for
"""
from email.mime.text import MIMEText

# import our Celery object
from framework.celery.celery import celery

import smtplib
# import the Celery log getter
from celery.utils.log import get_task_logger

# grab the logger for the Celery app
logger = get_task_logger(__name__)

@celery.task
def send_email(to=None, subject=None, message=None):
    """sends email from hairycode-noreply to specified destination

    :param to: string destination address
    :param subject: subject of email
    :param message: body of message
    :return: True if successful
    """
    # prep message
    fro="hairycode-noreply@hairycode.org"
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = fro 
    msg['To'] = to

    # log desired message to info level log
    logger.info('Sending email from: %r, to: %r' % (fro, to))
    
    # send message
    s = smtplib.SMTP('mail.hairycode.org')
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('YOUR_USERNAME', 'YOUR_PASSWORD')
    s.sendmail('hairycode-noreply@hairycode.org', [to], msg.as_string())
    s.quit()
    return True

"""
If everything else is in order your app will be able to add these to the Queue 
by either calling the .delay() or .apply_async() functions. But, before we can do that let's make 
sure our RabbitMQ server and Celery daemon are up and running.
"""