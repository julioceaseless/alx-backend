import { createClient } from 'redis';

// create a redis client instance
const client = createClient();

// catch connection error
client.on('error', (err) => {
  console.log('Redis client not connected to the server', err);
});
// display message on successful connection to server
client.on('connect', () => {
  console.log('Redis client connected to the server');
});
