# -*- coding: utf-8 -*-

import psycopg2

SQL_GET_REQERROR_DAYS = """
    select date, sum(status_value)/count(status_value)*100 as error_rate
    from (select
            to_char(time, 'YYYY-MM-DD') as date,
            case when status='200 OK' then 0 else 1.0 end as status_value
          from log) as t
    group by date
    order by error_rate desc;
"""

if __name__ == "__main__":
    # Connect database
    conn = psycopg2.connect(
        dbname="news", user="postgres",
        password="111111", host="192.168.0.108")

    # Calculate request error rate per day
    cursor = conn.cursor()
    cursor.execute(SQL_GET_REQERROR_DAYS)
    error_days = cursor.fetchall()
    for (date, error_rate) in error_days:
        if error_rate <= 1:
            break
        print("'{}' -- {:.2f}% errors".format(date, error_rate))

    # Close the connection
    conn.close()
