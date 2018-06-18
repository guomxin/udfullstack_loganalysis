#!/usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2

N = 3
SQL_GET_TOP_N_ARTICLES = """
    select title, view_count from articles,
        (select substr(path, 10) as article_slug, count(*) as view_count
        from log
        where path like '/article/%'
        group by path
        order by view_count desc
        limit {}) as topN_from_log
    where articles.slug=topN_from_log.article_slug
    order by view_count desc
"""

if __name__ == "__main__":
    # Connect database
    conn = psycopg2.connect(
        dbname="news", user="postgres",
        password="111111", host="127.0.0.1")

    # Fetch popular articles
    cursor = conn.cursor()
    cursor.execute(SQL_GET_TOP_N_ARTICLES.format(N))
    popular_articles = cursor.fetchall()
    for (title, view_count) in popular_articles:
        print("'{}' -- {} views".format(title, view_count))

    # Close the database connection
    conn.close()
