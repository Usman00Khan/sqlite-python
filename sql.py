import sqlite3
import os

def safeSqlCalls(f):
    def helper(x,arg):
        print(x)
        print("arg",arg)
        conn = sqlite3.connect('test.db')
        v = f(x,arg,conn)
        conn.close()
        return v
    return helper

class InitializeSQL:
    __instance = None
    def __init__(self):
        """ Create singleton instance """
        # Check whether we already have an instance
        if InitializeSQL.__instance is None:
            # Create and remember instance
            InitializeSQL.__instance = InitializeSQL.__impl()
        self.__dict__['_Singleton__instance'] = InitializeSQL.__instance
    
    def __getattr__(self, attr):
        """ Delegate access to implementation """
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        """ Delegate access to implementation """
        return setattr(self.__instance, attr, value)

    class __impl:
        """ Implementation of the singleton interface """

        def makeDB(self):
            if os.path.exists("./test.db"):
                return False
            else:
                self.table1(1)
                self.table2(100)
                return True

        @safeSqlCalls
        def table1(self,x,conn):
            print(x)
            conn.execute('''CREATE TABLE COMPANY
                (ID INT PRIMARY KEY     NOT NULL,
                NAME           TEXT    NOT NULL,
                AGE            INT     NOT NULL,
                ADDRESS        CHAR(50),
                SALARY         REAL);''')
            print('success')
            return 1


        @safeSqlCalls
        def table2(self,x,conn):
            print(x)
            conn.execute('''CREATE TABLE COMPANY2
                (ID INT PRIMARY KEY     NOT NULL,
                NAME           TEXT    NOT NULL,
                AGE            INT     NOT NULL,
                ADDRESS        CHAR(50),
                SALARY         REAL);''')
            print('success')
            return 1

class Query:
    def __init__(self):
        pass
    @safeSqlCalls
    def insert(self,x,conn):
        print (23)
        conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )")
        conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")
        conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")
        conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")
        conn.commit()

