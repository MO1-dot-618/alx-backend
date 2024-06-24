import { createQueue } from 'kue';

const blacklistedNumbers = ['4153518780', '4153518781'];
const queue = createQueue();

/**
 * Handles notification jobs for queue 'push_notification_code_2'
 * @param {string} phoneNumber - user phone number
 * @param {string} message - push notification message
 * @param {import('kue').Job}} job - queue job
 * @param {import('kue').DoneCallback} done - done call back
 * @returns {void}
 */
function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blacklistedNumbers.some((number) => number === phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
