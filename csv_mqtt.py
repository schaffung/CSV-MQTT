import csv
import json
import time
import paho.mqtt.client as mqtt

# Configuration Parameters.
CSV_FILE_NAME = "sample.csv"
MQTT_TOPIC = "sample_topic"
MQTT_PORT = 1883
MQTT_BROKER = "sample_broker"

# Global variables.
data_value = {}
key_values = []
key_value_count = 0

# On connect MQTT Callback.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code : "+str(rc))

# on publish MQTT Callback.
def on_publish(client, userdata, mid):
    print("Message Published.")


# Reading the csv file to extract the data.
with open(CSV_FILE_NAME, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            key_values = row
            key_value_count = len(key_values)
            line_count +=1
        else:
            temp_val = {}
            data_val = row
            count = 0
            for value in key_values:
                temp_val[value] = data_val[count]
                count +=1
            data_value[line_count] = temp_val
            line_count +=1

# Connecting to MQTT for publishing.
client = mqtt.Client()
client.on_connect = on_connect # On Connect Callback.
client.on_publish = on_publish # On Publish Callback.
client.connect(MQTT_BROKER, 1883, 60) # Connecting to the MQTT Broker.

while 1:
    for value in data_value:
        temp_data_val = str(data_value[value]).replace("'", '"')
        try:
            client.publish(MQTT_TOPIC, temp_data_val)
            time.sleep(1)
        except:
            print("Publish Failed.")