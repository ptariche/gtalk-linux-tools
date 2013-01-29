gtalk-tools
===========

There are many of times I wish to not login to my Linux box. This gtalk-bot is built to run specific commands.

DEPENDENCIES:
         - Python; Fortune; NMAP

COMMAND LIST:
        - |portscan| / run by entering a URL or IP address; this returns an nmap report.
        - |whoison| / returns who is logged into the Linux Box.
        - |ping| / run by entering a URL or IP address; this returns a ping report. 
        - |dumpsockets| / returns the socket statistics.
        - |memorypages| / returns the active/inactive memory page information.
        - |processlist| / returns the process list tree.
        
TO USE:
        - Google Account
        - Modify the Authentication.xml file; in between the username tag, enter your gmail email;
        and, enter your password for the gmail account in the password tag. 

TO RUN: 
        - Execute Robot.py

NOTES: 
        - In the case a command not recognized is entered, the bot will return a Fortune.  
