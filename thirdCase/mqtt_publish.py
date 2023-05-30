import paho.mqtt.client as mqtt
from flask import Flask, request


def on_connect(client, userdata, flags, rc):
	if rc == 0:
		print("Connected to MQTT Broker!")
	else:
		print("Failed to connect, return code %d\n", rc)

client = mqtt.Client()
client.on_connect = on_connect

client.connect("test.mosquitto.org")
client.loop_start()

app = Flask(__name__)


@app.route("/message", methods=["POST"])
def message_rec():
    message = request.get_data(as_text=True)
    print(f"Message: {message}")

    client.publish("dimimi", message)

    return "Message received!"


if __name__ == "__main__":
    app.run()