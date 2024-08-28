import { createClient } from 'redis';

async function main() {
    // Create an asynchronous Redis client
    const client = await createClient()
        .on('error', (err) => console.log('Redis client not connected to the server', err))
        .once('connect', () => console.log('Redis client connected to the server'))
        .connect

    // Connect the client
    await client.connect();

    // Set a key-value pair in Redis
    await client.set('key', 'value');

    // Get the value associated with the key
    const value = await client.get('key');
    console.log('Retrieved value:', value);

    // Disconnect the client
    await client.disconnect();
}
main().catch(console.error);