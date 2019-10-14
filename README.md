# CSV-MQTT
A CSV to MQTT connector. Reads data from csv file and pushes it to a MQTT Broker.


Many a times, we want to read a particular .csv file and then form a MQTT payload to publish it to cloud. ( Probably when working in IoT).

So the project as always came in due to a necessity. The idea is simple. The process will read the .csv file wherein the very first row contains the columns headers. ( Please add column headers before using the code or be ready to see something strange.)
Then the same column headers are treated as Keys and the corresponding row values as Values in a JSON object while forming a MQTT Payload.

For example, If the .csv has column headers as, 
Name, Age and School

Then the resulting MQTT Payload will be of the form,

{
  "Name" : "dummy_name",
  "Age" : "dummy_value",
  "School" : "dummy_school"
}

It is a minimal code and anyone can tweak it to run for their needs.
