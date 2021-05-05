# NOTES

This is a file for me to keep track of notes for developing the project. This could be workflows, to-dos etc.

## Progress
 Next Milestone: Provide the mock info from the back end. This will let me explore HTTP headers for last modified etc.
 Next Session: Create new webcam-db docker container and keep note of username etc.

2020-05-05: Started work on back end and set up testing framework. Deleted webcam-db docker container
 2020-04-20: Created basic front end that has a mock of webcams info.
 2020-04-17: Created empty Angular project and set up Python environment.

## Based on
I am basing this app on what I've learned from the following tutorials:

 * [Angular Tour of Heroes](https://angular.io/tutorial)
 * [Auth0 Angular and Flask](https://auth0.com/blog/using-python-flask-and-angular-to-build-modern-apps-part-1/)
 * [Pluralsight TDD with Angular](https://www.pluralsight.com/guides/introduction-to-angular-test-driven-development)
 * [Learning Go With Tests](https://quii.gitbook.io/learn-go-with-tests/) For the rigoourus TDD cycle

## Backend Setup
The backend uses Python, Flask and PostgresDB via Docker.
Pipenv is used to manage dependencies.

Before starting backend development run the following commands each time:
```
pipenv shell
sudo docker start webcam-db
```

