# kairosdb-examples-python

Some code examples on how to use [KairosDB](http://kairosdb.org/) REST API through Python and requests module. Currently we've the following code examples:

**Data points**:
	- Insert
	- Query
	- Delete

**Metrics**:
	- List
	- Delete

**Tags**:
	- List Tag Names
	- List Tag Values

**Misc**:
	- Health status
	- Version

For complete details about the KairosDB REST API, please [check their documentation](http://kairosdb.github.io/docs/build/html/restapi/index.html).

## How to run the examples? 
In order to run the examples you should have a KairosDB server locally (check if it is running going to [http://localhost:8080/](http://localhost:8080/) - if KairosDB Web UI appears, than everything is fine). After that, you can open your Terminal e just run `python3 <example>.py` in the desired example.

For example, if you want to list all metrics just run `python3 metrics/list.py`. 

## Roadmap

- Add some scripts to download a test version of KairosDB, run the server locally and import a test database. With that it's possible to really test the code examples without the need of setting up an environment.
- Add complex code examples ([do you have a suggestion for this topic?]())

## Suggestions? Problems? Critics? 
If you have suggestions, problems with the code, critics or anything like that don't hesitate in creating a new GitHub Issue or making a Pull Request. 

Actually I want to improve the repository, but I don't have ideas on what to do.

## About
I've created this repository because I'm the only guy at my laboratory that actually learned about KairosDB and (sometimes) my coworkers need to do something envolving KairosDB and they don't know how to do that. These code examples will be useful for them.