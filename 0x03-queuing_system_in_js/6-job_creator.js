#!/usr/bin/yarn dev
import { createQueue } from 'kue';

const queue = createQueue({name: 'push_notification_code'});
const job =  {
  phoneNumber: '07045679939',
  message: 'Account registered',
}
const jobCreator = queue.create('push_notification_code', job);

jobCreator
  .on('enqueue', () => {
    console.log('Notification job created:', job.id);
  })
  .on('complete', () => {
    console.log('Notification job completed');
  })
  .on('failed attempt', () => {
    console.log('Notification job failed');
  });
jobCreator.save();