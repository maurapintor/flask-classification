# ISDe course
## Web development
### Maura Pintor - [maura.pintor@unica.it](mailto:maura.pintor@unica.it)

---

What this lesson covers:

Note: we are not going to start from scratch. We are going to clone a 
repository that contains the structure of our code.

What we have:
* requirements
* the definition of the APIs that we need to implement
* the code for the classifier is already written, we are going to use it 
as a **black box**. This means that we know what is the input and the expected 
output, but we are not going to look inside the code.

---

## Part 0 : Web servers basics

---

### Web server for the user

![web-server](images/webserver.png)

More info [here](https://en.wikipedia.org/wiki/Web_server).

---

### Web server for the developer

![backend-frontend](images/backend-frontend.png)

More info [here](https://en.wikipedia.org/wiki/Front_and_back_ends).

---

### API

[![api-video](https://img.youtube.com/vi/s7wmiS2mSXY/0.jpg)](https://www.youtube.com/watch?v=s7wmiS2mSXY)

More info [here](https://en.wikipedia.org/wiki/Application_programming_interface).

---

### HTTP
![http-example](images/http-example.png)

More info [here](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol).

---

### The language of web servers

![http methods](images/http-methods.png)

---

### Localhost

![localhost](images/what-is-localhost.png)
More info [here](https://en.wikipedia.org/wiki/Localhost).

---

### Deployment

![deployment](images/deploy.png)

deploy resources = make them ready to be used



## 1.Define the service

First, we have to define what we want to build. Our **requirements** are: 

* **a web app (frontend) that runs a simple ML algorithm for image classification (backend)**
* inside a container - don't worry about it now
* time constaint (always take into account)

### Before start writing the code ...

This is an important part of our development process. We can start writing code 
right away, but the risk is that if we don't have the right start we might have 
to rewrite the code many times. It is better to take a moment to think about 
the structure of our application. 




![/classification POST](images/classification_post.png)


![/classification POST worker](images/classification_post_sequel.png)

![/classification GET](images/classification_get.png)

![scaling workers](images/multiple_workers.png)
