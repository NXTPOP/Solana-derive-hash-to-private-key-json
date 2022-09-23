import subprocess
import time
import pandas as pd
import csv


#CLI Commander
def run(cmd):
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE
                            )
    stdout, stderr = proc.communicate()
    return proc.returncode, stdout, stderr

# BEGIN THE BURN


#Amount of NFT to burn (type int)
amount = 2

#Counter (do not touch)
reached = 0

#Array
array = []

#Read Accounts token from CSV file
with open('alienx_gt.csv', newline='') as f:
  reader = csv.reader(f)
  for row in reader:
      array.append(row[0])
    

for accounts in array:
      print('----- BURNING IN PROGRESS -----')

      code, out, err = run(["spl-token", "burn", accounts, "1"])
      if code == 0:
                    print(out)
                    output = out.decode('utf-8')
                    print(output)
                    print('SUCCESS')
                    reached += 1
                    print(f"{reached} NFT HAVE BEEN BURNT")
                    if reached == amount:
                        print("ALL NFT HAVE BEEN BURNT")
                        break
                    
                
      else:
                    err_msg = err.decode('utf-8')
                    print(err_msg)
                    print('FAILED')
                    time.sleep(5)
                    continue



