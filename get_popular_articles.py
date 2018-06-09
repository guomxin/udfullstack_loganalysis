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
    # 建立数据库连接
    conn = psycopg2.connect(
        dbname="news", user="postgres",
        password="111111", host="192.168.0.108")

    # 获取并打印热门文章
    cursor = conn.cursor()
    cursor.execute(SQL_GET_TOP_N_ARTICLES.format(N))
    popular_articles = cursor.fetchall()
    for (title, view_count) in popular_articles:
        print("'{}' -- {} views".format(title, view_count))

    # 关闭数据库连接
    conn.close()
