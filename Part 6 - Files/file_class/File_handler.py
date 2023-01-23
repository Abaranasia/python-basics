class File_handler:

  file_type=''
  text=''
  
  def __init__(self, file_type):
    self.file_type= file_type
  
  def create_route (self):
    return 'Part 6 - Files/file_class/'+ self.file_type +'/'+ self.file_type+'.txt'



  def writer(self, text):
    route= self.create_route()
    try: 
      file = open (route, 'a', encoding= 'utf8')
      file.write (f'{text} \n')

    except Exception as e: 
      print (e)

    finally:
      print ('file saved!')
      file.close()



  def reader(self):
    route= self.create_route()
    try:
      file = open (route, 'r', encoding= 'utf8')
      print (f'File content: \n{file.read()}')
    except Exception as e: 
      print (e)

    finally:
      file.close()


  def delete(self):
    import os
    route= self.create_route()

    if os.path.exists(route):
      os.remove(route) 
    else:
      print("The file does not exist") 