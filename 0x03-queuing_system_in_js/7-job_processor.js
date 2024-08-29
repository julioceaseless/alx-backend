import kue from 'kue';

// Create an array for blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send notification
const sendNotification = (phoneNumber, message, job, done) => {
  // Track job progress: 0%
  job.progress(0, 100);

  // Check if the phone number is blacklisted
  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Track job progress: 50%
  job.progress(50, 100);

  // Log the message
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Track job progress: 100%
  job.progress(100, 100);

  // Complete the job
  done();
};

// Create a Kue queue
const queue = kue.createQueue();

// Process jobs in the push_notification_code_2 queue, two at a time
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
