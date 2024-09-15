import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-29e9260b-242e-4429-aed4-4fbbdbd629b0'
pnconfig.publish_key = 'pub-c-160505f2-2c70-4967-8977-2a224eeaedf3'

TEST_CHANNEL = 'TEST_CHANNEL'

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Channel: {message_object.channel} | Message: {message_object.message}')

class PubSub():
    """
    Handles the publish/subscribe layer of the application.
    Provides communication between the nodes of the blockchain network.
    """
    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels([TEST_CHANNEL]).execute()
        self.pubnub.add_listener(Listener())

    def publish(self, channel, message):
        """
        Publish the message object ti the channel.
        """
        self.pubnub.publish().channel(channel).message(message).sync

def main():
    pubsub = PubSub()

    time.sleep(1)

    pubsub.publish(TEST_CHANNEL, {'foo': 'bar'})

if __name__ == '__main__':
    main()
