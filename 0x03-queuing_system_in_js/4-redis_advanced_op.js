import { createClient, print } from 'redis';

// Create an asynchronous Redis client
const client = createClient();

client.on('error', err => console.log('Redis client not connected to the server', err));

client.once('ready', () => {
  console.log('Redis client connected to the server');

  // Create Hash and set values
  client.hset('HolbertonSchools', 'Portland', 50, print);
  client.hset('HolbertonSchools', 'Seattle', 80, print);
  client.hset('HolbertonSchools', 'New York', 20, print);
  client.hset('HolbertonSchools', 'Bogota', 20, print);
  client.hset('HolbertonSchools', 'Cali', 40, print);
  client.hset('HolbertonSchools', 'Paris', 2, print);

  // Display Hash
  client.hgetall('HolbertonSchools', (err, object) => {
    if (err) {
      console.error('Error fetching hash:', err);
      return;
    }
    console.log(object);
  });
});
