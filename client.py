#Adam Ayala
#Santiago Bruno Gonzalez
from socket import *
from datetime import datetime
serverName = 'mininet-vm'
serverPort = 12000
clientSocket = socket(AF_INET,SOCK_DGRAM)
# Sets the timeout for 1sec
clientSocket.settimeout(1)
print
message = raw_input('Input lowercase sentence: ')
print
# Creating empty list to store RTT values
times = []
# Used to ping 10 times
for i in range (10):
        # Captures time when packet is sent
        startTime = datetime.now()
        clientSocket.sendto(message.encode(),(serverName, serverPort))
        try:
                modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
                # Captures time when packet is recieved
                stopTime = datetime.now()
                # Calculate Round Trip Time(RTT) in micro seconds and append it to the list
                rtt = stopTime.microsecond - startTime.microsecond
                times.append(rtt)
		#Calculate estimated rtt with alpha at 0.125 and initial estimated rtt at 0
		print "Estimated RTT: " + str(0.125 * rtt)
		#Calculate deviation
		print "Deviation: " + str(0.25 * (0.125 * rtt))
                print modifiedMessage.decode() + " " + str(i+1) + " " + str(rtt) + "microseconds "
        except:
                # If packet is lost a time out message is returned
                print "Request timed out"
                continue
print
print "Min RTT: " + str(min(times)) + "microseconds. Max RTT: " + str(max(times)) + "microseconds. Average RTT: " + str(sum(times)/len(times)) + "microseconds"
print str((10-len(times))*10) + "% packet loss"
print
