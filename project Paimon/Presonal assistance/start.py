import input_module as im
import process_module as pm
import output_module as om
import welcome
import os
os.system("cls")
 
running = True

welcome.greet()
while(running):
    i = im.take_input()
    if i == "t":
        running = False
    
    o = pm.process(i)
    om.output(o)

