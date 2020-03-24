# Babble App  

Babble is going to be a multi-container application. It is being implemented by a Ryan Gniadek and Ben Bernstein for the Docker Containerization special interest course taught at Virginia Tech.


Sample POST request via CURL 
`curl -X POST -d '{ "author": { "email": "user@example.com", "name": "string"}, "message": "Hello there"}' localhost/blabs --header "Content-Type:application/json"`

Sample DELETE command via CURL
`curl -X DELETE localhost/blabs/1`