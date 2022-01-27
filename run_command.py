#!/usr/bin/python

import psycopg2

from connect import config

def run_command():
    """ create tables in the PostgreSQL database"""
    #commands = (""" SELECT * FROM vendors """)
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        #for command in commands:
        #    cur.execute(command)
        cur.execute('SELECT * from vendors')
        # Display the result
        result = cur.fetchall()
        #print(result[0])
        # display each records from the tuple result. The return is automatically made
        for i in range(0, len(result)):
            print(result[i])
#            print("\n")
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    run_command()
