import time

from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-29e9260b-242e-4429-aed4-4fbbdbd629b0'
pnconfig.publish_key = 'pub-c-160505f2-2c70-4967-8977-2a224eeaedf3'
pubnub = PubNub(pnconfig)

TEST_CHANNEL = 'TEST_CHANNEL'

pubnub.subscribe().channels([TEST_CHANNEL]).execute()

class Listener(SubscribeCallback):
    def message(self, pubnub, message_object):
        print(f'\n-- Incoming message_object: {message_object}')

pubnub.add_listener(Listener())

def main():
    time.sleep(1)
    
    pubnub.publish().channel(TEST_CHANNEL).message({'foo': 'bar'}).sync

if __name__ == '__main__':
    main()
