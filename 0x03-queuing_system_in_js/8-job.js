const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw Error('Jobs is not an array');
  } else {
    jobs.forEach((jobEntry) => {
      const job = queue.create('push_notification_code_3', jobEntry);
      job.save((err) => {
        if (!err) {
          console.log(`Notification job created: ${job.id}`);
        }
      });
      // Log when the job is completed
      job.on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      });

      // Log if the job fails
      job.on('failed', (err) => {
        console.log(`Notification job ${job.id} failed: ${err}`);
      });

      // Log the job's progress
      job.on('progress', (progress) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });
    });
  }
};

module.exports = createPushNotificationsJobs;
