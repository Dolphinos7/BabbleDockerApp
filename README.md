# Babble App  

Babble is going to be a multi-container application. It is being implemented by a Ryan Gniadek and Ben Bernstein for the Docker Containerization special interest course taught at Virginia Tech.


Sample POST request via CURL 
`curl -X POST -d '{ "author": { "email": "obiwan@prequelmemes.com", "name": "General Kenobi"}, "message": "Hello there"}' localhost/api/blabs --header "Content-Type:application/json"`

Sample DELETE command via CURL
`curl -X DELETE localhost/api/blabs/1`

Sample GET command via CURL
`http://localhost/api/blabs?createdSince=0`