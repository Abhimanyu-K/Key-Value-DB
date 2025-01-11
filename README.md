# Redis Implementation Project

This project implements Redis-like functionality with basic server and client interactions.

## Getting Started

### Prerequisites
- Python 3.x installed
- pip package manager

### Installation
```bash
pip install -r requirements.txt
```

### Starting the Server
```bash
python server.py
```

The server will start on default port 63632 (standard Redis port).
### Connecting to the Server
```bash
redis-cli -p 63632
```

This will connect to the Redis server on the default port 6379.
## Supported Commands

Currently implemented commands:

- `set key value` - Store a key-value pair
- `get key` - Retrieve value by key
- `del key` - Delete a key-value pair
- `getset key value` - Set new value and return old value
- `mset key1 value1 key2 value2...` - Set multiple key-value pairs
- `mget key1 key2...` - Get multiple values
- `incr key` - Increment value
- `incrby key value` - Increment by specific value
- `decr key` - Decrement value
- `decrby key value` - Decrement by specific value
- `ping` - Test server connection (returns PONG)

Example usage:
```bash
set user1 "John Doe"
get user1
del user1
exists user1
ping
```

## Upcoming Features

Future implementations will include:

- Data persistence
- TTL (Time To Live) for keys
- List operations (lpush, rpush, lrange)
- Hash operations (hset, hget)
- Set operations (sadd, smembers)
- Connection pooling
- Authentication

## Contributing

Feel free to contribute by submitting pull requests or creating issues for bugs and feature requests.

## License

MIT License