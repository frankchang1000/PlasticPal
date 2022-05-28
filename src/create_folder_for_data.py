#<p class="chakra-text ec0uryp0 css-1kr6buh"><font style="vertical-align: inherit;"><font style="vertical-align: inherit;">Plastic (PP/PE)</font></font></p>
import os


newpath = "data/"

for i in range(54, 100):
  #add folders for each count
  os.makedirs(newpath + str(i))
