#!/usr/bin/env python
import logging

#Level logging
#1. debug
#2. info
#3. Warning
#4. error
#5  critical

logging.basicConfig(filename='logfile.log', level=logging.DEBUG)

def main():
    try:
        logging.DEBUG("we are in the main try loop")
        mathFail = 9/0
        if 1>2:
            logging.info('enter to first main if statement')
            print "if"
        else:
            logging.info('enter to first main else statement')
            print "else"
            
    except Exception, e: 
        logging.critical(str(e))
        
main()

"""
    #Untuk membuat format sesuai dengan waktu bawaan komputer
    logging.Formatter.converter = time.gmtime
    log_level = logging.getLevelName(self.config.get("general", "log_level"))
        log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(lineno)s:%(message)s'
"""