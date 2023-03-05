# where-to-fly
Find the cheapest next destination to travel to, the end result is a web interface to find the cheapest destination to fly to, data is pulled from the goflightlabs public API.

The project is a demonstration of an ETL design with streaming data layer to pull data from the API using Apache Kafka.
Flask is used as a web app framework to create the front-end as well as the back-end code. 

Azure sql database will be used as the main database to store the data.

Will use sqlite as a database engine to store flight data with option to push to to cloud.
