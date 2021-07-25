#/usr/bin/python
import logging
from fastapi import FastAPI
import sys
import socket
import uvicorn
from socket import gaierror

## Creating a Flask app

class dnsapi(object):
   """
        Class to host the API to get domain name and give IPs as response
   """
   
   app=FastAPI()
   def __init__(self):
      self.logger = logging.getLogger("DNSAPI")
      if not self.logger.hasHandlers():
        self.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler(sys.stdout)
        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)
  
   def route(self,domain):
       try:  
          self.x=socket.gethostbyname_ex(domain)
          return {'ipaddress': self.x[2]}
          self.logger.info("IP address is retrieved")
       except gaierror:
          self.logger.info("Invalid domain")
          return {'ipaddress': "Non existent domain"}

   
#driver function
if __name__=='__main__':
   a = dnsapi()
   app1=dnsapi.app
   @app1.get("/{domain}")
   async def route(domain):
       return a.route(domain)
   uvicorn.run(app1, host="127.0.0.1", port=5000)
