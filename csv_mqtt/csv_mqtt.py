import os
import time
import signal
import sys
import csv
import paho.mqtt.client as mqtt


def signal_handler(sig, frame):
    """
    Signal handler for handling sigint
    """
    sys.exit(0)

def on_connect(client, userdata, flags, rc_value):
    """
    On connect callback handler for MQTT.
    """
    print(f"Connected with result code : {rc_value}")

def on_publish(client, userdata, mid):
    """
    On Publish callback handler for MQTT.
    """
    print("Message Published.")

class CsvMqtt:
    """
    Class providing the methods for CSV-MQTT Connectors.
    """

    def __init__(self, broker, port=1883, timeout=60,
                 connect_cb=on_connect, publish_cb=on_publish):
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_connect = connect_cb
        self.mqtt_client.on_publish = publish_cb
        self.mqtt_client.connect(broker, port, timeout)

    def publish_csv_data(self, csv_path, mqtt_topic, interval=5):
        """
        The method to publish the contents of the csv in given
        interval.
        """
        if not os.path.exists(csv_path):
            return False
        data_value = {}
        key_values = []

        with open(csv_path, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    key_values = row
                    #key_value_count = len(key_values)
                    line_count += 1
                else:
                    temp_val = {}
                    data_val = row
                    count = 0
                    for value in key_values:
                        temp_val[value] = data_val[count]
                        count += 1
                    data_value[line_count] = temp_val
                    line_count += 1
        for value in data_value:
            temp_data_val = str(data_value[value]).replace("'", '"')
            try:
                self.mqtt_client.publish(mqtt_topic, temp_data_val)
                time.sleep(interval)
            except Exception as excep_v:
                print(f"Publish Failed. {excep_v}")
        return True
