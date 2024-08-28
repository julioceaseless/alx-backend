import { createClient } from 'redis';

// create a redis client instance
const client = createClient();
client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err);
});
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// subscribe to the channel
client.subscribe('holberton school channel');

// handle incoming messages
client.on('message', (channel, message) => {
  console.log(`${message}`);

  // kill the the connection if message is KILL_SERVER
  if (message === 'KILL_SERVER') {
    client.unsubscribe('holberton school channel');
    client.quit();
  }
});
