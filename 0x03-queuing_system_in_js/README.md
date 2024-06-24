# 0x03. Queuing System in JS

## About
- Running Redis server locally
- Caching data using `redis` and `node-redis`
- Handling async operations with redis
- Using `Kue` as queue system
- Building an express app that interacts with a redis server
- Building an express app that interacts with Redis server and queue

## Tasks
0. Redis installation and setting the value `School` for the key `Holberton`
    - File: [dump.rdb](dump.rdb)
1. Script that connects to redis servers running locally
    - File: [0-redis_client.js](0-redis_client.js)

2. Functions:
    - `SetNewSchool` - sets value for given key
    - `displaySchoolValues` - retrieves value of given key
    - File: [1-redis_op.js](1-redis_op.js)

3. Extension of [1-redis_op.js](1-redis_op.js) that modifies `displaySchoolValue` function to work using promises.
    - File: [2-redis_op_async.js](2-redis_op_async.js)

4. Script that sets redis hashes using `node-redis` and prints the response using `redis.print`
    - File: [4-redis_advanced_op.js](4-redis_advanced_op.js)
5. Pub-Sub model in redis:
    - Script that creates a redis client and subscribes it to `holberton school channel`
    - Scripts that creates a redis client that published to `holberton school channel`
    - Files:
        - [5-subscriber.js](5-subscriber.js)
        - [5-publisher.js](5-publisher.js)
6. Job creation using `kue`
    - File: [6-job_creator.js](6-job_creator.js)

7. Job processing using `kue`
    - File: [6-job_processor.js]

8. Tracking job progress and errors with `kue` - **job creator**
    - File: [7-job_creator.js](7-job_creator.js)

9. Tracking job progress and errors with `kue` - **job processor**
    - File: [7-job_processor.js](7-job_processor.js)

10. Job creation function `createPushNotificationsJobs`
    - File: [8-job.js](8-job.js)

11. Unit tests for `createPushNotificationsJobs`
    - File: [8-job.test.js](8-job.test.js)

12. Express orders API server that uses redis for caching:
    - Routes:
        - `GET /list_products/`: returns a list of all products.
        - `GET /list_products/:itemId`: returns information about products with specified id.
        - `GET /list/reserve_product/:itemId`: reservers one unit of product with given item id if present and in stock.
    - File: [9-stock.js](9-stock.js)

13. Express seat reservation API server that uses redis for job queues:
    - Routes:
        - `GET /available_seats`: returns the number of available seats.
        - `GET /reserve_seat`: seat reservation endpoint.
        - `GET /process`: reservation jobs processing endpoint.
    - Files: [100-seat.js](100-seat.js)
