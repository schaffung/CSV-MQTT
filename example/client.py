import signal
import sys
import paho.mqtt.client as mqtt

def signal_handler(sig, frame):
    """
    Signal handler for handling sigint
    """
    sys.exit(0)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("mcrn/avenger")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("broker.emqx.io", 1883, 60)
    client.loop_forever()
