const { expect } = require('chai');
const kue = require('kue');
const createPushNotificationsJobs = require('./8-job');

const queue = kue.createQueue();

describe('createPushNotificationsJobs', () => {
  // Enter test mode
  before(() => {
    queue.testMode.enter();
  });

  // Clear the queue after each test
  afterEach(() => {
    queue.testMode.clear();
  });

  // Exit test mode after all tests
  after(() => {
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
  });

  it('should create jobs in the queue', () => {
    const jobs = [
      { phoneNumber: '4153518780', message: 'This is the code for 1234' },
      { phoneNumber: '4153518781', message: 'This is the code for 4562' }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql(jobs[0]);
    expect(queue.testMode.jobs[1].data).to.eql(jobs[1]);
  });
});
