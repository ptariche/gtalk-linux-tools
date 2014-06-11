#!/usr/bin/python
# -*- coding: utf-8 -*-

# PyGtalkRobot: A simple jabber/xmpp bot framework using Regular Expression Pattern as command controller
# Copyright (c) 2008 Demiao Lin <ldmiao@gmail.com>

import sys
import time
import os

from PyGtalkRobot import GtalkRobot
from xml.etree import ElementTree
############################################################################################################################

class SampleBot(GtalkRobot):
    
    #This method is used to change the state and status text of the bot.
    def command_001_setState(self, user, message, args):
        '''(available|online|on|busy|dnd|away|idle|out|off|xa)( +(.*))?$(?i)'''
        show = args[0]
        status = args[1]
        jid = user.getStripped()

        # Verify if the user is the Administrator of this bot
        if jid == administrator:
            print jid, " ---> ",bot.getResources(jid), bot.getShow(jid), bot.getStatus(jid)
            self.setState(show, status)
            self.replyMessage(user, "State settings changed！")

    #This method is used to send email for users.
    def command_002_SendEmail(self, user, message, args):
        #email ldmiao@gmail.com hello dmeiao, nice to meet you, bla bla ...
        '''[email|mail|em|m]\s+(.*?@.+?)\s+(.*?),\s*(.*?)(?i)'''
        email_addr = args[0]
        subject = args[1]
        body = args[2]
        #call_send_email_function(email_addr, subject,  body) 
        self.replyMessage(user, "\nEmail sent to "+ email_addr +" at: "+time.strftime("%Y-%m-%d %a %H:%M:%S", time.gmtime()))

   #This method is used to response users.
    def command_100_Default(self, user, message, args):
        '''.*?(?s)(?m)'''
        print user, "executed command: wildcard"
        msg = os.popen("/usr/games/fortune")
        self.replyMessage(user, msg.read())

####################### aQuinaS ########################################

    def command_003_Fortune(self, user, message, args):
        '''(random|quote)'''
        print user, "executed command: Fortune"
        msg = os.popen("/usr/games/fortune")
        self.replyMessage(user, msg.read())

    def command_004_Who(self, user, message, args):
        '''(whoison)'''
        print user, "executed command: who"
        msg = os.popen("/usr/bin/who")
        self.replyMessage(user, msg.read())
    def command_005_NMAP(self, user, message, args):
        '''(nmap|scan\s+(.*)(?i))'''
        url =args[1]
        print user, "executed command: nmap"
        msg = os.popen("nmap -v -v -sS -O -P0 "+url)
        self.replyMessage(user, msg.read())
    def command_006_Ping(self, user, message, args):
        '''(ping|isup\s+(.*)(?i))'''
        url =args[1]
        print user, "executed command: ping"
        msg = os.popen("ping -c 5 "+url)
        self.replyMessage(user, msg.read())
    def command_007_DumpSockets(self, user, message, args):
        '''(dumpsockets)'''
        print user, "executed command: dumpsockets"
        msg = os.popen("ss")
        self.replyMessage(user, msg.read())
    def command_008_ProcessList(self, user, message, args):
        '''(processlist)'''
        print user, "executed command: process list tree"
        msg = os.popen("ps -ejH")
        self.replyMessage(user, msg.read())
    def command_009_MemoryPageInformation(self, user, message, args):
        '''(memorypages)'''
        print user, "executed command: memory information"
        msg = os.popen("vmstat -a")
        self.replyMessage(user, msg.read())
    def command_010_getIP(self, user, message, args):
        '''(getip)'''
        print user, "executed command: get ip"
        msg = os.popen("curl ifconfig.me/ip")
        self.replyMessage(user, msg.read())
############################################################################################################################
if __name__ == "__main__":
    GoogleSession = ElementTree.parse('authentication.xml')
    try:
 	administrator = GoogleSession.find('Administrator').text
        email = GoogleSession.find('Username').text
        password = GoogleSession.find('Password').text
	status = GoogleSession.find('Status').text
    except:
        print "Error in XML file format: authentication.xml."
    bot = SampleBot()
    bot.setState('available', status)
    bot.start(email, password)
