import kue from 'kue';

// Create a queue with Kue
const queue = kue.createQueue();

// Create an object containing the Job data
const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account'
};

// Create a job in the 'push_notification_code' queue
const job = queue.create('push_notification_code', jobData);
job.save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

// Log to the console when the job is completed
job.on('complete', () => {
  console.log('Notification job completed');
});

// Log to the console when the job fails
job.on('failed', () => {
  console.log('Notification job failed');
});
