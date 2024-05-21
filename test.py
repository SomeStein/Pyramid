import logging

def worker():
   try:
      1/0
      # Your thread's code here
   except Exception as e:
      logging.exception("An error occurred: %s", str(e))        
      
worker()