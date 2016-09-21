This goal of this project is to make a Twitter bot personal assistant. 
You can communicate to the bot @DerekTheBot through direct messages.

The project is still in progress. Currently, the program uses the Twitter API to check for direct messages and reply to the sending user. There are only 3 supported commands: Wolfram, Insert, and Find. 

1. Wolfram passes the rest of the message directly to the Wolfram API and returns a text version of the result.
2. Insert inserts the rest of the message into a database.
3. Find returns all the records in the database added by the user.

The Twitter wrapper uses [Python Twitter](https://github.com/bear/python-twitter).
The Wolfram Alpha wrapper uses [Tungsten](https://github.com/seenaburns/Tungsten).
