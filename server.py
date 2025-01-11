from command_processor import CommandProcessor
from key_value_store import KeyValueStore
from socket_handler import SocketHandler

HOST = "127.0.0.1"
PORT = 63632


# TODO: TTL, EVICTION POLICY, JSON
if __name__ == '__main__':
    store = KeyValueStore()
    command_processor = CommandProcessor(store)

    socket_manager = SocketHandler()
    socket_manager.start(command_processor.process)
