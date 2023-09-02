from docontext import DBContext
context = DBContext("students.sl3")
#1 Create table
#context.Query("CREATE TABLE S2019 (id INT PRIMARY KEY, name VARCHAR(20), age INT, avg_grade FLOAT)")
#2 Insert
#context.Query("INSERT INTO S2019 (id, name, age, avg_grade) VALUES(1, 'Kosov Anton', 11, 12)")
#context.Query("INSERT INTO S2019 (id, name, age, avg_grade) VALUES(2, 'Sahaidak Dmytro', 11, 12)")
#context.Query("INSERT INTO S2019 (id, name, age, avg_grade) VALUES(3, 'Mostovoi Daniil', 11, 11.5)")
#context.Query("INSERT INTO S2019 (id, name, age, avg_grade) VALUES(4, 'Hladyshenko Nazar', 11, 11)")
#context.Query("INSERT INTO S2019 (id, name, age, avg_grade) VALUES(5, 'Miasnikov Taras', 14, 10)")
#3 Update
#context.Query("UPDATE S2019 SET avg_grade = 10.5 WHERE id = 5")
#4 Delete
#4.1
# context.Query("INSERT INTO S2019 (id, name, age, avg_grade) VALUES(6, 'test', 0, 0)")
#4.2
#context.Query("DELETE FROM S2019 WHERE id = 6")
#5 SELECT
#5.1
'''
res = context.Execute("SELECT id, name, age, avg_grade FROM S2019")
#res = context.Execute("SELECT * FROM S2019")
print(res)
print(res[1][1])#[1] - 1 tuple, [1] - name
print(res[2][3])#[2] - 2 tuple, [3] - avg_grade
'''
#5.2
#res = context.Execute("SELECT name FROM S2019 WHERE avg_grade = 12")
#res = context.Execute("SELECT name FROM S2019 WHERE avg_grade < 12")
#res = context.Execute("SELECT name FROM S2019 WHERE age < 12")
#5.3 ORDER BY (DESC, ASC)
#res = context.Execute("SELECT name FROM S2019 WHERE age < 15 ORDER BY avg_grade DESC")
res = context.Execute("SELECT name FROM S2019 WHERE age < 15 ORDER BY avg_grade ASC")
print(res)