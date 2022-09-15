## Motor Thrills

Your onestop motor vehicle shopping center.

### Description

Motor Thrills is automobile shopping website which lists different types of vehicles, brief description, price and models from different car sales websites and provides a one click comparison of price from different vehicle dealers.

The data is scraped from different popular car sales and dealers. Instead of visiting multiple sites for the same search, users will have one stop website for different vendors and be able to make decision quickly.

Lastly, this is a portfolio project in [Africa Leadership Experience (ALX) ](https://www.alxafrica.com/) Fullstack Software Engineering course.

### Project URL

To access the web application, visit [Motor Thrills](http://141.95.42.125:82/) 

### Project Objectives

* Web scraping
* Data processing and saving 
* User authentication and authorization
* Task Scheduling and management and Threads management
* Project hosting and deployment.

### Technologies Used

* Python Beautiful soup for web scraping
* Python Django for backend data processing
* Postgres for data storage
* Bootstrap for front end presentation
* Javascript (jquery) for front end data processing. 
* Nginx, Gunicorn and related server  requirements 
* celery for Task queue management and thread management.
* Rabbit MQ server as the Task Management Broker
* Any other related technologies as deemed right for use.

### Websites Used

* https://autocj.co.jp/used_cars
* https://www.beforward.jp/stocklist
* https://www.autonews.com/automakers-suppliers

### Project Setup

1. [x] Clone the project from gitHub using `git clone https://github.com/homemix/motor_thrills`
2. [x] Create a virtual environment and activate it using `python3 -m venv venv` and `source venv/bin/activate`
3. [x] Install the requirements from requirements.txt using `pip install -r requirements.txt`
4. [x] Create a postgres database and update the database settings in .env file
5. [x] Run the migrations using `python manage.py migrate`
6. [x] Run the server using `python manage.py runserver`
7. [x] Visit the site on localhost:8000 `http://localhost:8000/` and enjoy the site.


### Scraping Data

1. [x] Got to webapp directory
2. [x] Run the command `python manage.py shell` to activate shell
3. [x] Run the command `from webapp import tasks` to import the tasks
4. [x] Run the command `tasks.scrape_data()` to scrape the data

NB: The scraping process takes a while to complete. It is advisable to run the scraping process in the background using celery.

### License

This project is licensed under the MIT License - free to use and modify.

### Acknowledgments

* [Africa Leadership Experience (ALX) ](https://www.alxafrica.com/) for the opportunity to learn and grow.
* All the mentors and facilitators for their support and guidance.
* Autojapan and Beforward for the data used in this project.


