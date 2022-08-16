import redis from 'redis';
import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) => console.log('Redis Client Error', err));

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, (err, reply) => {
        if (err) {
            console.log(err);
        }
        redis.print(reply);
    })
}
function displaySchoolValue(schoolName) {
    client.get(schoolName, (err, reply) => {
        console.log(reply);
    })
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');