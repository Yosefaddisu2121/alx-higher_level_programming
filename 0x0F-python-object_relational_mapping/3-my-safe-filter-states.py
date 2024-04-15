#!/usr/bin/python3
"""Module thet lists all states from the hbtn_0e_0_usa database."""
import sys
import MySQLdb

if __name__=="__main__":
    import sys
    import MySQLdb

    # Get the command-line arguments
    mysql_username = sys.argv[1]
    mysql_password =  sys.argv[2]
    database_name =  sys.argv[3]
    state_name =  sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
            host = 'localhost',
            port = 3306,
            user = mysql_username,
            passwd=mysql_password,
            db=database_name
    )

    #create a cursor object to execute queries
    cursor = db.cursor()

    # Prepare the sql query with placeholdes
    sql_query = "SELECT * FROM states WHERE name = %s OEDER BY id ASC"

    # Execute the query with the state name a parameter
    cursor.execute(sql_query, (state_name.))

    # Fetch all the rows return by th query
    rows = cursor.fetchall()

    #display the results
    for row in rows:
        print(row)
