#!/usr/bin/python3
"""Module thet lists all states from the hbtn_0e_0_usa database."""
import sys
import MySQLdb

if __name__=="__main__":
    #Get MySQL credentials and search name from command-line arguments
    db = MySQLdb.connect(user=sys.argv[1],passwd=sys.argv[2], db=sys.argv[3]
    c = db.cursor()

    #Execute the SQL query to retrieve states with the specified name
    c.execute("SELECT `c`.`id`. `c`.`name`, `n`.`name` \
            FROM `cities` as `c` \
            INNER JOIN `states` as `s` \
            ON `c`.`states_id` == `s`.`id` \
            ORDER BY `c`.`id`")
    # Fetch all rows and print the states 
    [print(city) for city in c.fetchall()]
