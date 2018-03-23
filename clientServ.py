import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

def Push(payload):
	if(payload[0] > 50):
		GPIO.ouput(4, 1)
	else:
		GPIO.output(4, 0)


def PullReq(payload):

def PullRep(payload):

def DataSend(payload):

def DataCollect(payload):


def Service(parsePacket):
	servType = parsePacket['Type']
	payload = parsePacket['Payload']

	if(servType == b'\x00'):
		Push(payload)
	elif(servType == b'\x01'):
		PullReq(payload)
	elif(servType == b'\x02'):
		PullRep(payload)
	elif(servType == b'\x03'):
		DataSend(payload)
	elif(servType == b'\x04'):
		DataCollect(payload)