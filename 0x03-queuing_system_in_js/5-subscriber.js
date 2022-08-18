import { createClient } from 'redis';


const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => console.log('Redis client connected to the server'));

//holberton school channel
const subscriber = client.duplicate();
await subscriber.connect();

await subscriber.subscribe('holberton school channel', (message) => {
    console.log(`${message}`);

    if (message === 'KILL_SERVER') {
        client.unsubscribe('holberton school channel');
    }
});

