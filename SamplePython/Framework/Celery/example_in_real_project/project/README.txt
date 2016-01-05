Before we can do that let’s make sure our RabbitMQ server and Celery daemon are up and running.
Testing Our New Task
Launch RabbitMQ

Launch your RabbitMQ server in the background from the shell

    $ rabbitmq-server -detached

You can ensure it’s running the background by inspecting your processes

    $ ps aux | grep rabbit --color

Which should yield three things

    A very, very long output (this is the rabbitmq-server we just launched)
    The RabbitMQ daemon always running silently“hairycode 27491 0.0 0.0 599680 156 ?? S 5:24PM 0:00.33 /usr/local/Cellar/rabbitmq/3.1.3/erts-5.10.1/bin/../../erts-5.10.1/bin/epmd -daemon”
    And, the grep command you just executed“hrybacki 35327 1.2 0.0 2432768 596 s000 S+ 2:25PM 0:00.00 grep rabbit –color”

Note: If you see one or more additional of the “long” processes running you will run into issues. If this is the case stop all RabbitMQ servers

    $ rabbitmqctl-stop

and start over. I will provide an example of what can go wrong if there are multiple brokers or Celery daemons running at once.
Launch the Celery daemon

From the project/ directory launch the Celery daemon

    $ celery -A framework.celery.celery worker -l debug

which should give you a daemon monitor without put along the lines of

     -------------- celery@Harrys-MacBook-Air.local v3.0.21 (Chiastic Slide)
    ---- **** ----- 
    --- * ***  * -- Darwin-12.4.1-x86_64-i386-64bit
    -- * - **** --- 
    - ** ---------- [config]
    - ** ---------- .> broker:      amqp://guest@localhost:5672//
    - ** ---------- .> app:         __main__:0x10f5355d0
    - ** ---------- .> concurrency: 4 (processes)
    - *** --- * --- .> events:      OFF (enable -E to monitor this worker)
    -- ******* ---- 
    --- ***** ----- [queues]
     -------------- .> celery:      exchange:celery(direct) binding:celery

    [Tasks]
      . framework.email.email_tasks.send_email

…

    [2013-07-23 15:46:55,342: DEBUG/MainProcess] consumer: Ready to accept tasks!

    
===============================================================================
Launch the Celery daemon
=========================================================================
From the project/ directory launch the Celery daemon

    $ celery -A framework.celery.celery worker -l debug
    
nanti akan muncul bintang2 dan diakhiri dengan status celery is ready

- A framework.celery.celery worker: informs Celery which the app instance to use and that it will be creating workers.
  Workers take tasks from the queue, process them, and return the result to the message broker.

- l debug : tells Celery that you want it to display log level debug output for testing purposes. 
  Normally you would execute -l info for a log level info output.

Now, let’s make sure we have some Celery workers up and running

    $ ps aux | grep celery --color
    
Note the concurrency number when we launched the Celery daemon. This is the number of processors and in turn 
workers which should have been launched. The grep output from the previous command should leave you with that 
many outputs similar to: 

    hairycode       37992   0.1  0.4  2495644  33448 s001  S+    3:20PM   0:00.74 /Users/hairycode/git/staging-celery/venv/bin/python /Users/hairycode/git/staging-celery/venv/bin/celery -A framework.celery.celery worker -l debug

Detailed information about launching the Celery daemon can be found here or from the shell

    $ celery --help
    
===============================================================================================    
Executing our Task

    # import celery
    import celery

    # import our send_email task
    from framework.email.email_tasks import send_email

    # call our email function
    # pemanggilan yang salah karena memasukkan fungsi call ke dalam variabel(result) sehingga program akan menunggu fungsi call sampai beres, padahal fungsi dari celery adalah agar program berjalan async, sedangkan dengan memasukannya ke dalam vaiabel menjadikan program kembali jadi synchonus  
    result = send_email.delay('', 'all your smtp are belong to us', 'somebody set up us the bomb')
	#The task has now been processed by the worker you started earlier, and you can verify that by looking at the workers console output.
    type(result)

If you look at your Celery daemon you can see the task coming in, being processed, returning the result, and even how long it took to execute. For example the call above gave me the following output

    [2013-07-23 15:48:29,145: DEBUG/MainProcess] Task accepted: framework.email.email_tasks.send_email[09dad9cf-c9fa-4aee-933f-ff54dae39bdf] pid:39336
    [2013-07-23 15:48:30,600: DEBUG/MainProcess] Start from server, version: 0.9, properties: {u'information': u'Licensed under the MPL.  See http://www.rabbitmq.com/', u'product': u'RabbitMQ', u'copyright': u'Copyright (C) 2007-2013 VMware, Inc.', u'capabilities': {u'exchange_exchange_bindings': True, u'consumer_cancel_notify': True, u'publisher_confirms': True, u'basic.nack': True}, u'platform': u'Erlang/OTP', u'version': u'3.1.3'}, mechanisms: [u'AMQPLAIN', u'PLAIN'], locales: [u'en_US']
    [2013-07-23 15:48:30,601: DEBUG/MainProcess] Open OK!
    [2013-07-23 15:48:30,602: DEBUG/MainProcess] using channel_id: 1
    [2013-07-23 15:48:30,604: DEBUG/MainProcess] Channel open
    [2013-07-23 15:48:30,607: INFO/MainProcess] Task framework.email.email_tasks.send_email[09dad9cf-c9fa-4aee-933f-ff54dae39bdf] succeeded in 1.46279215813s: True

===============================================================================================

some_task.delay() vs some_task.apply_async()

some_task.delay() is a convenient method of calling your function as it looks like a regular function. 
However, it is short hand for calling some_task.apply_async(); apply_async() is a more powerful and 
flexible method for calling your tasks.


Executing our task — more realistically

The AsyncResult is the Celery object that the backend (RabbitMQ) returned after the worker (Celery) completed 
the task. The long string following it is the task_id. More often you won’t assign the function 
call to a variable. Doing so would hold up our app until the task had completed. 
That wouldn’t make much sense would it? Rather, you will simply call the delay or apply_async function 
and let your code continue on like this

    # import celery
    import celery

    # import our send_email task
    from framework.email.email_tasks import send_email

    # call our email function
    send_email.delay('', 'all your smtp are belong to us', 'somebody set up us the bomb')

Remember, we still have the task id. If you want to check the status or result of what we just submitted you can do so by asking the task queue

    # grab the AsyncResult 
    result = celery.result.AsyncResult('09dad9cf-c9fa-4aee-933f-ff54dae39bdf')

    # print the task id
    print result.task_id
    09dad9cf-c9fa-4aee-933f-ff54dae39bdf

    # print the AsyncResult's status
    print result.status
    SUCCESS

    # print the result returned 
    print result.result
    True
    
========================================================================================================================
Headache Number Two: My Celery daemon is only receiving every other task? Wat.

This little bug took me entirely too long to solve. At some point I started noticing that exactly half of the .
delay() calls I was making were permanently in a state of PENDING.

For example, running this

 

    from framework.email.email_tasks import send_email

    send_email.delay('', 'all your smtp are belong to us', 'somebody set up us the bomb')
	#give the result ==> 0e55bfed-1f05-4700-90fe-af3dba34ced5
    send_email.delay('', 'all your smtp are belong to us', 'somebody set up us the bomb')
	#give the result ==> af3846a9-4a31-4a8d-99a4-0d990d51ef22
Gave the following output from the Celery daemon

    [2013-07-22 18:18:44,576: DEBUG/MainProcess] Task accepted: tasks.test[0e55bfed-1f05-4700-90fe-af3dba34ced5] pid:7663
    [2013-07-22 18:18:44,583: DEBUG/MainProcess] Start from server, version: 0.9, properties: {u'information': u'Licensed under the MPL.  See http://www.rabbitmq.com/', u'product': u'RabbitMQ', u'copyright': u'Copyright (C) 2007-2012 VMware, Inc.', u'capabilities': {u'exchange_exchange_bindings': True, u'consumer_cancel_notify': True, u'publisher_confirms': True, u'basic.nack': True}, u'platform': u'Erlang/OTP', u'version': u'2.8.4'}, mechanisms: [u'PLAIN', u'AMQPLAIN'], locales: [u'en_US']
    [2013-07-22 18:18:44,585: DEBUG/MainProcess] Open OK!
    [2013-07-22 18:18:44,585: DEBUG/MainProcess] using channel_id: 1
    [2013-07-22 18:18:44,586: DEBUG/MainProcess] Channel open
    [2013-07-22 18:18:44,589: INFO/MainProcess] Task framework.email.email_tasks.send_email[0e55bfed-1f05-4700-90fe-af3dba34ced5] succeeded in 2.0180089473724s: True

0e55bfed-1f05-4700-90fe-af3dba34ced5 was there but af3846a9-4a31-4a8d-99a4-0d990d51ef22 wasn’t.

I restarted my Celery daemon. Same thing.

I restarted my RabbitMQ server. Same thing.

I created an entire new project and followed the First Steps with Celery docs. Same thing.

Confused I searched around but I could only find one other person who had encountered something similar 
and that issue was over a year old. Note: I tried his solution but it didn’t resolve the issue.

The trick was that somewhere along the line I had another set of Celery workers running in the background 
that were not part of the daemon I had just started running. These workers were taking tasks from the queue 
and I wasn’t getting them back. I was able to recreate the same bug by having a second instance 
of RabbitMQ server running.

Remember when I told you to ensure you only had one RabbitMQ server and the correct number of concurrent 
Celery workers running by checking your processes? This is why. Don’t do this.

Let’s Improve our Setup

Adding logs

Adding logs was pretty straightforward. First, we need to modify our celeryconfig.py to specify where we want 
our logs:

    # celeryconfig.py

    # default RabbitMQ broker
    BROKER_URL = 'amqp://'

    # default RabbitMQ backend
    CELERY_RESULT_BACKEND = 'amqp://'

    # specify location of log files
    CELERYD_LOG_FILE="/path/to/your/logs/celery.log"
Now, we implement logging within the task itself.

After importing the required function, we grab the logger associated with our Celery app

    logger = get_task_logger(__name__)
Then, at the desired point log a custom message to log level info. Note: If you desired to log to another level e.g. debug you would use logger.debug(…)

    logger.info('Sending email from: %r, to: %r' % (fro, to))
The resulting email_tasks.py looks like:

    from email.mime.text import MIMEText
    from framework.celery.celery import celery
    # import the Celery log getter
    from celery.utils.log import get_task_logger

    # grab the logger for the Celery app
    logger = get_task_logger(__name__)

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
        s.login('', '')
        s.sendmail('hairycode-noreply@hairycode.org, [to], msg.as_string())
        s.quit()
        return True
And that’s it! After implementing logging, tasks should be adding your messages to their respective log files e.g.:

    [2013-07-23 15:48:29,145: INFO/MainProcess] Sending email from: hairycode-noreply@hairycode.org, to: 'testymctester@test.com'
Conclusion

Learning Celery has been… frustrating. The above examples barely begin to scratch the surface of what it’s capable of. It is an incredibly powerful and configurable tool I would however, like to see a more responsive community but, I understand we all busy people. Queuing tasks is a necessity for any major application and I’m beginning to develop a love-hate relationship with Celery. More to follow?

-H.


  
  