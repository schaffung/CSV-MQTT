from csv_mqtt import CsvMqtt

connector = CsvMqtt("broker.emqx.io")
connector.publish_csv_data("./example/sample.csv", "mcrn/avenger")
