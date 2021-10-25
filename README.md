# fast-api-with-mongo
Implemented 4 APIs(CRUD), to GET, POST, UPDATE, DELETE data from the database.
- Initially we have data in the form of CSV. 
- createDB.py handles the initial insertion of the total data from the CSV into the the MongoDB.
### Database used here is MongoDB
## Prerequisite
### Before starting the app, create a .env file and add the following to the file
#### - host=db
#### - port=27017
#### - username=your_usename
#### - password=your_password
### The whole app is containerised and you can get the app up and running by using docker-compose command
##  If you don't have docker installed, don't worry, this article has got you covered.
- [Directions to install Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)
## Commands to install docker-compose
- ` sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose `
- ` sudo chmod +x /usr/local/bin/docker-compose `
### Docker allows to start the app in an isolated container
### To start the app
`docker-compose up `
### To test the app
`localhost:8000`
### For swagger UI
`localhost:8000/docs`
