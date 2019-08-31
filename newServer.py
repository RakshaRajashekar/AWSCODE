#**********************************************

 #Masters Thesis July 2019
 #Raksha Rajashekar
 #Speech Navigation tool server
 #SPEECH ENABLED NAVIGATION IN A VIRTUAL ENVIRONMENT

#******************************************
# first of all import the socket library 

import socket
import re
import time
import sys
import errno
import fcntl,os
import select
import Queue
# next create a socket object  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#.setblocking(0)
s1= socket.socket()
#s2= socket.socket()
print "Socket successfully created"
  
# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 55555 
port2= 55556
#port3= 55557 # Command for algorithm to be written to this port
# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('', port)) #port to read from the device
s1.bind(('',port2))

#fcntl.fcntl(s,fcntl.F_SETFL,os.O_NONBLOCK)

#s.setblocking(0)
#s2.bind(('',port3))
#reset =0
print "socket binded to %s" %(port) 
print"socket binded to %s" %(port2)  
#print"Socket binded to %s" %(port3)

# put the socket into listening mode 
s.listen(5)
print"socket is listening to port1"

s1.listen(5)
print " socket is listening to port2"
#s2.listen(5)
print "socket is listenin to port3"
reset =0
c1, addr2 =s1.accept()
#print 'Got connection from',addr2
print "works before reading from app"
input= [s]
output = []
message_queue ={}
#fcntl.fcntl(s,fcntl.F_SETFL,os.O_NONBLOCK)
s.settimeout(0.1)
while True:
	try:
		c, addr1 = s.accept()
            	data = c.recv(1024)
            	print"established connection with the server"
        except socket.timeout, e:
		err = e.args[0]
		if err == 'timed out':
			command = "do nothing"
			c1.send(command)
               		print 'sent:',command
               		continue   #c.setblocking(0
		else:
			print e
               		sys.exit(1)
			
			
	except socket.error, e:
		 print'something else led to error'
           	 sys.exit(1) 
               
        
        else:
		if len(data)==0:
			print'server shut down'
              		c1.send("do nothing")
		else:
			result1 = data.find('rotate')
		       	result2 = data.find('clockwise')
		       	result3 = data.find('anticlockwise')
		       	result4 = data.find('left')
		       	result5 = data.find('right')
		       	result6 = data.find('degrees')
		       	result7 = data.find('reset')
		       	result8 = data.find('timestamp')
		       	result9 = data.find('x axis')
		       	result10 = data.find('y axis')
		       	result11 = data.find('z axis')
		       	result12 = data.find('turn')
		       	result13 = data.find('scale')
		       	result14 = data.find('zoom')
	   #result15 = data.find('zoom')
		       	result16 = data.find('in')
		      	result17 = data.find('out')
		       	result18 = data.find('Z axis')
		       	result19 = data.find('Z-axis')
		       	result20 = data.find('x-axis')
		       	result21 = data.find('y-axis')
		       	result22 = data.find('panning')
		       	result23 = data.find('pan')
		       	result24 = data.find('z-axis')
		       	result25 = data.find('Zoom')
		       	result26 = data.find('algorithm')
		       	result27 = data.find('up')
		       	result28 = data.find('down')
		       	result29 = data.find('move')
		       	result30 = data.find('algorithm')
		       	result31 = data.find('cylinder')
		       	result32 = data.find('square')
		       	result33 = data.find('cube')
		       	result34 = data.find('sphere')
		       	result35 = data.find('globe')
		       	result36 = data.find('cone')
		       	result37 = data.find('radius')
		       	result38 = data.find('Radius')
		       	result39 = data.find('Height')
		       	result40 = data.find('height')
		       	result41 = data.find('length')
		       	result42 = data.find('Length')
		       	result43 = data.find('X')
		       	result44 = data.find('x')
		       	result45 = data.find('Y')
		       	result46 = data.find('y')
		       	result47 = data.find('angle')
		       	result48 = data.find('Angle')
		       	reslut49 = data.find('Change')
		       	result50 = data.find('change')
		       	result51 = data.find('set')
		       	result52 = data.find('Set')
			result53 = data.find('Color')
			result54 = data.find('color')
			result55 = data.find('red')
			result56 = data.find('Red')
			result57 = data.find('Blue')
			result58 = data.find('blue')
			result59 = data.find('green')
			result60 = dats.find('Green')
			
			
			res= [int(i) for i in data.split() if i.isdigit()]
               		print("The numbers list is :" +str(res))
               		l=str(res)

			#********************************************************************************************************************
			# Commands to Rotate
			#*********************************************************************************************************************

			if  result1 != -1 or result12 != -1:  # if the command contains rotate or turn command
				
				if  result2 != -1  or result5 != -1:  # if command contains rotate and if it is clockwise or to the right
					
					if result6 != -1: # if command contains the rotate command followed by degrees
						
						if ( result9 != -1 or result20 != -1):
							
							print("Command recieved to rotate clockwise by n degrees along x axis")
      			                		command = "R CL X"+" "+str(res[0])
			                		command1= "nothing";
							
						elif (result10 != -1 or result21 != -1):
							print("command recieved to rotate clockwise along y axis")
			                		command = "R CL Y"+" "+str(res[0])
                                        		command1 ="nothing";
							
						elif (result11 != -1 or result24 != -1 or result18 != -1 or result19 != -1):
							print("command to rotate clockwise aong z axis")
		                        		command = "R CL Z"+" "+str(res[0])
                                        		command1 = "nothing"
							
						else:
							command = "R CL X"+" "+str(res[0])
                                        		command1= "nothing"
							
					else:  # if command does not mention the term degrees
						print("please mention degrees at the end of the command")
						
				elif ( result3 or result4 != -1) : # if command contains rotate and if its for anticlockwise or thr the left
					
					if result6 != -1: # if command contains the rotate command followed by degrees
						
						if result9 != -1:
							print("Command recieved to rotate anticlockwise by n degrees")
   		                        		command = "R AN X"+" "+str(res[0])
                                        		command1= "nothing"
							
						elif result10 != -1:
							print("command recieved for anticlockwise rotation along Y axis")
			                		command = "R AN Y"+" "+str(res[0])
                                       			command1= "nothing"
						
						elif (result11 != -1 or result24 != -1 or result18 != -1 or result19!= -1):
							print("Command recieved for anticlockwise rotation along z axis")
			                		command = "R AN Z"+" "+str(res[0])
                                        		command1= "nothing"
							
						else:
							command = "R AN X"+" "+str(res[0])
                                        		command1= "nothing"
							
					else:  # if command does not mention the term degrees
						print("please mention degrees at the end of the command")
						
						
				else:
					print("Default Command for Rotation")
		             		command = "R CL X 10"
                             		command1 = "nothing"
							

			#***************************************************************************************
			#Command for panning
			#****************************************************************************************

               		elif result29 != -1:
				if result4 != -1:
					print("Command for pannig left obtained")
					if len(res) != 0:
						command = "P L"+" "+str(res[0])
                          			command1= "nothing"
                       			else:
                          			command = "P L 5"
                          			command1= "nothing"
                    		elif result5!= -1:
					print("Command for panning right obtained")
	               			if len(res) != 0:
	                  			command = "P R" +" "+ str(res[0])
                          			command1= "nothing"
	               			else:
                         			command = "P R 5"
                          			command1= "nothing"
                          			print("Command for panninf right")
				elif result27 != -1:
                       			print("Command for panning up")
	               			if len(res) != 0:
                       				command = "P U"+" "+str(res[0])
                        			command1= "nothing"
	               			else:
	                			command = "P U 5"
                        			command1 = "nothing"
                    		elif result28 != -1:
                       			print("Command for panning down")
	               			if len(res) != 0:
                        			command = "P D"+ " "+str(res[0])
                        			command1= "nothing"
                       			else:
                        			command = "P D 5"
                        			command1= "nothing"
                    		else:
					print("Default pan")
                       			if len(res) != 0:
                          			command = "P R" + " "+str(res[0])
                          			command1 = "nothing"
                       			else:
                          			command = "P R 5"
                          			command1 = "nothing"

			#***************************************************************************
			#comand for algorithms
			#**************************************************************************
               		elif result30 != -1:  # if algorithm
				
	               		if result31 != -1:  #if cylinder
                          		command = "ALG CYL"
	                  		prev = command
                          		rem= "CYL"	
	  
	               		elif (result32 or result33 != -1):   # if cube
                          		command = "ALG CUBE"
                          		prev = command
                          		rem = "CUBE"
	   
                      	 	elif (result34 or result35 != -1) :   # if sphere
                          		command = "ALG SPH"
                         		prev = command
                          		rem = "SPH" 
          
                       		elif result36 != -1:                  # if cone
                          		command = "ALG CONE"
                         		prev = command
                          		rem = "CONE"
                       		else:
                         		if prev == "":
                             			command = "ALG CYL"
                             			rem = "CYL"
             
                         		else:
                             			command = prev
          
        
             


			#********************************************************************************************************************************
			#Command for zooming  zoom/scale(13,14,25) in(16) out(17)
			#***************************************************************************************************************************************
               		elif (result13 or result14 or result25 != -1):  #if command is scale or zoom 

                  		if result16 != -1: # command for zooming in
					print("Command recieved for zooming in ")
                     			if len(res) != 0:
  	                			command = "S ZIN"+" "+str(res[0])
                       				command1= "nothing"
                     			else: 
                       				command = "S ZIN 5"
                        			command1= "nothing"
					
				if result17 != -1: # command for zooming out
					print("Command recieved for zooming out")
				
	             			if len(res) != 0:
                        			command = "S ZOUT"+" "+str(res[0])
                        			command1 = "nothing"
                     			else:
                        			command = "S ZOUT 5"
                        			command1 = "nothing"

			
			#*********************************************************************************************************
			#Command to process Algorithm commands
			#*********************************************************************************************************
			
			elif(result49 != 0 or result50 !=0 or result51 != 0 or result52 != 0):
				print("Command recieved to change parameter in Algorithm")
				if result54 !=0 : # command to change color
					print("Command recieved to change color");
					if result55 !=0 or result56 != 0:
						print("to red")
						command = "AlG COL R"
						
					elif result57 !=0 or result58 != 0:
						print("to Green")
						command = "ALG COL G"
						
					elif result59 !=0 or result60 !=0:
						print("to Blue")
						command = "ALG COL B"
					else:
						print(" setting default color to 0,0,0 ")
						command = "do nothing"
				else:
					command = "do nothing"
					
						
                  #   if (result37 !=0 or result38 !=0):
                   #     print("command recieved to change radius ")
                    #    command = "CYL RAD"+" "+str(res[0])
            #         elif (result39 != 0 or result40 !=0):
             #           print("command recieved to change height")
              #          command = "CYL HEI"+" "+str(res[0])
               #      else:
                #        command = "do nothing"
                 # elif rem == "CUBE":
                  #   print("Command recieved to change parameter in cube") 
                   #  if (result41 != 0 or result42 != 0):
                    #    if(result43 != 0 or result44 != 0):
                     #      print("command recieved to change length along x axis")
                      #     command = "CUBE LEN X"+" "+str(res[0])
                       # elif (result45 != 0 or result46 !=0):
                        #   print("command received to change length along y axis")
                         #  command = "CUBE LEN Y"+" "+str(len[0])
                       # else:
                          # command = "do nothing"
         #         elif rem == "Cone":
          #           print("Command received to change parameter in Cone")
           #          if(result37 != 0 or result38 != 0):
            #            printf("command received to change radius")
             #           command = "CONE RAD"+ " "+str(res[0])
              #       elif( result39 != 0 or result40 != 0):
               #         print("command recieved to change height")
                #        command = "CONE HEI"+" "+str(res[0])
                 #    elif( result47 != 0 or result48 != 0):
                  #      print("ocommand received to change angle")
                   #     command= "CONE ANG"+" "+str(res[0])
                    # else:
                     #   command = "do nothing"
				
				
			
			
			
			#*************************************************************************************************************
			# Command to reset
			#*****************************************************************************************************************
               		elif result7 != -1:
                  	command = "reset"
                  	reset =1;    

			
			#******************************************************************************************************************
			# Default if command not interpreted right
			#*******************************************************************************************************************
               		else:
                 		print ("Not familiar with this command, try again")
                       		command = "do nothing"
                  		command1="nothing"




               		print 'adding command:',command
              		c1.send(command)
               		c.close
        



      # elif(result49 != 0 or result50 !=0 or result51 != 0 or result52 != 0):
               #   
                #  







