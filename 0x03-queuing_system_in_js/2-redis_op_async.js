import { createClient, print } from 'redis';
import { promisify } from 'util';

// Create an asynchronous Redis client
const client = createClient();

client.on('error', err => console.log('Redis client not connected to the server', err));

client.once('ready', () => {
  // Promisify the client.get method
  const getAsync = promisify(client.get).bind(client);

  // Function to set a new school in Redis when client is ready
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
  const displaySchoolValue = async (schoolName) => {
    try {
      const value = await getAsync(schoolName);
      console.log(value);
      return value; // Explicitly return the value
    } catch (err) {
      console.error('Error fetching value:', err);
      return null; // Return null or handle the error appropriately
    }
  };

  // Example usage
  displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  displaySchoolValue('HolbertonSanFrancisco');
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});
