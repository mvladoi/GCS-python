1.Create a server folder.

    mkdir server
    cd server

2.Copy the `server.js` file into the folder 

```
const express = require('express');
const session = require('express-session');
const cookieParser = require('cookie-parser');
const MemcachedStore = require('connect-memjs')(session);
const publicIp = require('public-ip');
const crypto = require('crypto');

// Environment variables are defined in app.yaml.
let MEMCACHE_URL = process.env.MEMCACHE_URL || '127.0.0.1:11211';

if (process.env.USE_GAE_MEMCACHE) {
  MEMCACHE_URL = `${process.env.GAE_MEMCACHE_HOST}:${process.env.GAE_MEMCACHE_PORT}`;
}

const app = express();
app.enable('trust proxy');

app.use(cookieParser());
app.use(session({
  secret: 'your-secret-here',
  key: 'view:count',
  proxy: 'true',
  store: new MemcachedStore({
    servers: [MEMCACHE_URL]
  })
}));

app.get('/', (req, res, next) => {
  // Discover requester's public IP address
  publicIp.v4().then((ip) => {
    const userIp = crypto.createHash('sha256').update(ip).digest('hex').substr(0, 7);

    // This shows the hashed IP for each
    res.write(`<div>${userIp}</div>`);

    if (req.session.views) {
      req.session.views += 1;
    } else {
      req.session.views = 1;
    }
    res.end(`Viewed <strong>${req.session.views}</strong> times.`);
  }).catch(next);
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log('App listening on port %s', PORT);
  console.log('Press Ctrl+C to quit.');
});

module.exports = app;

```

3.Create a `package.json` file with NPM or Yarn:

    npm init


4.Install dependencies with NPM or Yarn:

    npm install --save connect-memjs cookie-parser express express-session public-ip

5.Create a [memcached instance](https://cloud.google.com/memorystore/docs/memcached/quickstart-console) in the same region as your app engine application (`gcloud app describe` to find the region). Write down the IP address of one of your nodes.

6.Create a `app.yaml` file

```
runtime: nodejs
env: flex

env_variables:
 
  MEMCACHE_URL: 10.10.10.10:11211 #your memcached instance ip

```

7.Deploy the application to App Engine Flex

   gcloud app deploy
   gcloud app browse

8. Visit `http://YOUR_PROJECT_ID.appspot.com` to see the deployed app.

[![enter image description here][1]][1]


  [1]: https://i.stack.imgur.com/uS1oU.png


[Use Memcache for sessions with Express.js on App Engine flexible environment](https://cloud.google.com/community/tutorials/express-memcached-session-appengine)
