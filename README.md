# Log Analysis Project

## Install
### Requirements and data
- Python 3.6
- pip install psycopg2
- postgresql
  - Set the password for user postgres as 111111
  - Set listen_addresses in file postgresql.conf as '\*'
  - Set METHOD for IPv4 local connections in file pg_hba.conf as md5
- Data generation refer to [link](https://classroom.udacity.com/nanodegrees/nd004-cn/parts/d3335c49-3556-488a-9f63-c0d28b16ff12/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/262a84d7-86dc-487d-98f9-648aa7ca5a0f/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91) 'Download the data' section
### Clone gitr repository
```bash
$ git clone https://github.com/guomxin/udfullstack_loganalysis.git
```

## Run
### What are the most popular three articles of all time?
The 'path' field of table 'log' which like '/article/%' are viewing logs of articles and the substring without the
first 9 characters(article_slug) is corresponding to field 'slug' in table 'articles'. We can calculate the viewing count
of the articles by grouping and counting 'article_slug' of table 'log'. To get the title of the article, we can join 
the table 'log' and 'articles' on slug.<br>
Change the current directory to where the codes are located, run the following command:
```bash
$ python get_popular_articles.py
```
###  Who are the most popular article authors of all time? 
The 'path' field of table 'log' which like '/article/%' are viewing logs of articles and create a temporary table 'article_views'
by selecting the substring without the first 9 characters of 'path' field. We can get the corresponding author name by joining 'article_views' and 'articles' on slug and joining 'articles' and 'authors' on articles.author and authors.id. To get the viewing count of each author, we can grouping and counting authors.name on the joining result.<br>
Change the current directory to where the codes are located, run the following command:
```bash
$ python get_popular_authors.py
```
###  On which days did more than 1% of requests lead to errors? 
Create a temporary table based on log which includes two fields: 'date' by parsing time and 'status_value' which is 0 when
status equals '200 OK' otherwise 1. Calculate request error rate by sum(\*)/count(\*) by grouping the temporary table on 'date'
field and order the results on error rate in descending order. Python codes scan the fetching result sequentially, print the date and error rate and stop scanning when error rate is smaller than 1%.<br>
Change the current directory to where the codes are located, run the following command:
```bash
$ python get_reqerror_days.py
```
