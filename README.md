# CSV-MQTT
A CSV to MQTT connector. Reads data from csv file and pushes it to a MQTT Broker.


Many a times, we want to read a particular .csv file and then form a MQTT payload to publish it to cloud. ( Probably when working in IoT).

So the project as always came in due to a necessity. The idea is simple. The process will read the .csv file wherein the very first row contains the columns headers. ( Please add column headers before using the code or be ready to see something strange.)
Then the same column headers are treated as Keys and the corresponding row values as Values in a JSON object while forming a MQTT Payload.

For example, If the csv data is as follows,

```csv
Name,Age,School
dummy_name,dummy_value,dummy_school
```

Then the resulting MQTT Payload will be of the form,

```json
{
  "Name" : "dummy_name",
  "Age" : "dummy_value",
  "School" : "dummy_school"
}
```

One can install the package using pip

```
pip3 install csv-mqtt
```

Once installed, they can use the package by using the import

```
from csv_mqtt.csv_mqtt import CsvMqtt
```

The `CsvMqtt` can be used to create objects for creating a pipeline for csv-mqtt.

For examples, one can check the example directory in the project.
