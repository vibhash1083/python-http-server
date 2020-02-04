import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                    password="Maya@1998",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres")
    cursor = connection.cursor()
except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)


def close_connection():
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


def get_notes():
    postgreSQL_select_Query = "select * from note"
    data = []
    if cursor:
        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from note table using cursor.fetchall")
        note_records = cursor.fetchall() 
        print("Print each row and it's columns values")
        for row in note_records:
            record = {}
            record["id"] = row[0]
            record["name"] = row[1]
            record["date_created"] = row[2]
            data.append(record)
    return data


def add_notes(name):
    from datetime import datetime
    current_date = datetime.today().strftime('%Y-%m-%d')
    max_id_query = "Select max(id) from note"
    # Execute Query and fetch max id
    # Increment by 1 to get next id
    id = 0
    # use id, name, current_date to create a new entry in db

    # implement notes
    return True


# if __name__ == "__main__":
#     data = get_notes()
#     print("Data ", data)
#     close_connection()
