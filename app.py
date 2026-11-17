import pymysql
connection = pymysql.connect(
    host = 'localhost',
    user = 'python_app_slot2', 
    password = 'PythonApp@123',
    database = 'camerin_students_2',
    port = 3306
)

def get_data():
    query = """
                SELECT * FROM students
                WHERE student_id = 102
            """
    cursor.execute(query)
    return cursor.fetchone()

try:
    with connection.cursor() as cursor:
        print("\n== Original Data ==")
        print(get_data())

        cursor.execute("""
            UPDATE students SET city = %s
            WHERE student_id = %s
        """,("Delhi",102))

        print("\n== After Update (Before commit) ==")
        print(get_data())

        connection.commit()

        print("\n== After Commit ==")
        print(get_data())

        cursor.execute("""
                UPDATE students SET city = %s
                WHERE student_id = %s
            """,("Thrissur",102))

        print("\n== After Second update (Before ROLLBACK) ==")
        print(get_data())

        connection.rollback()
        print("\n== AFTER ROLLBACK ==")
        print(get_data())
except Exception as e:
    print(f"Error : {e}")
finally:
    connection.close()
    print("Operations completed")

# try:
#     pass
# except:
#     pass

print("hello, welcome")