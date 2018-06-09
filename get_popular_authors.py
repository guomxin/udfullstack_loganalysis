# -*- coding: utf-8 -*-

import psycopg2

SQL_GET_TOP_AUTHORS = """
    select authors.name, count(*) as article_view_count from articles,
        (select substr(path, 10) as slug
        from log
        where path like '/article/%') as article_views, authors
    where articles.slug = article_views.slug and articles.author = authors.id
    group by authors.name order by article_view_count desc;
"""

if __name__ == "__main__":
    # 建立数据库连接
    conn = psycopg2.connect(
        dbname="news", user="postgres",
        password="111111", host="192.168.0.108")

    # 获取并打印热门作者
    cursor = conn.cursor()
    cursor.execute(SQL_GET_TOP_AUTHORS)
    popular_authors = cursor.fetchall()
    for (author_name, view_count) in popular_authors:
        print("'{}' -- {} views".format(author_name, view_count))

    # 关闭数据库连接
    conn.close()
