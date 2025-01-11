class CommandProcessor:

    def __init__(self, store):
        self.store = store

    def update_mulitple_key(self, data):
        for i in range(0, len(data)-1, 4):
            key = data[i+1]
            value = data[i + 3]
            self.store.set(key, value)

    def process(self, data):
        commands = (str(data)).split('\r\n')

        match commands[2]:
            case 'set':
                key = commands[4]
                if len(commands) < 6:
                    return "Error: Invalid Command"
                value = commands[6]
                return self.store.set(key, value)
            case 'get':
                key = commands[4]
                return self.store.get(key)
            case 'del':
                key = commands[4]
                if self.store.get(key):
                    self.store.delete(key)
                    return "OK"
                return "Error: key not found"
            case 'getset':
                old_value = self.store.get(key)
                value = commands[6]
                self.store.set(key, value)
                return old_value
            case "mset":
                self.update_mulitple_key(commands[3:])
                return "OK"
            case "mget":
                return "OK"
            case "incr":
                key = commands[4]
                return self.store.incr(key)
            case "incrby":
                key = commands[4]
                value = commands[6]
                return self.store.incr(key, int(value))
            case "decr":
                key = commands[4]
                return self.store.decr(key, int(self.store.get(key)))
            case "decrby":
                key = commands[4]
                value = commands[6]
                return self.store.decr(key, int(value))
            case 'ping':
                return "PONG"
            case _:
                return 'Error: Command not found'

        return ''

    def _format_response(self, value):
        if isinstance(value, str) and value.startswith("Error"):
            return f"-{value}\r\n".encode()
        return f"${len(str(value))}\r\n{value}\r\n".encode()
