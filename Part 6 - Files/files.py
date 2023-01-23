
def writer():
# Writing a file
# Write creates a file if it doesn't exists and if exists it overwrites
  try: # It is recommended to manage files inside a try-catch block
    file = open ('Part 6 - Files/doc.txt', 'w', encoding= 'utf8')
    file.write ('Adding some text to the file\n')
    file.write ('Adiós!')

  except Exception as e: 
    print (e)

  finally:
    print ('file saved!')
    file.close()

def reader():
  try:
    file = open ('Part 6 - Files/doc.txt', 'r', encoding= 'utf8')
    print (f'File content: \n {file.read()}')
  except Exception as e: 
    print (e)

  finally:
    file.close()


writer()
reader()