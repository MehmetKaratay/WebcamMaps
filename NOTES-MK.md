# NOTES

This is a file for me to keep track of notes for developing the project. This could be workflows, to-dos etc.

## Based on
I am basing this app on what I've learned from the following tutorials:

 * [Angular Tour of Heroes](https://angular.io/tutorial)
 * [Auth0 Angular and Flask](https://auth0.com/blog/using-python-flask-and-angular-to-build-modern-apps-part-1/)
 * [Pluralsight TDD with Angular](https://auth0.com/blog/using-python-flask-and-angular-to-build-modern-apps-part-1/)
 * [Learning Go With Tests](https://quii.gitbook.io/learn-go-with-tests/) For the rigoourus TDD cycle

## Backend Setup
The backend uses Python, Flask and PostgresDB via Docker.
Pipenv is used to manage dependencies.

Before starting backend development run the following commands each time:
```
pipenv shell
sudo docker start webcam-db
```

