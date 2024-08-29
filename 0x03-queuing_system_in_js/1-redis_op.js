import { createClient, print } from 'redis';

// Create an asynchronous Redis client
const client = createClient();

client.on('error', err => console.log('Redis client not connected to the server', err));

client.once('ready', () => {
  // Function to set a new school in Redis
  const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, (err, reply) => {
      if (err) {
        console.error('Error setting value:', err);
        return;
      }
      print(null, reply); // redis.print to show the confirmation message
    });
  };

  // Function to display the value of a school
  const displaySchoolValue = (schoolName) => {
    client.get(schoolName, (err, value) => {
      if (err) {
        console.error('Error fetching value:', err);
        return;
      }
      console.log(value);
    });
  };

  // Example usage
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});
