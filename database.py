import pymysql


class Sign(object):
    def __init__(self):
        self.db =pymysql.connect(db = 'store', user = 'shiboyao', passwd = '1234')
        self.cursor = self.db.cursor()
        self.CID = None
        
        
    def login(self, cid, password):
        self.cursor.execute("SELECT * FROM CUSTOMER WHERE CID = %s AND PASSWORD = %s", (cid, password))
        count = len(self.cursor.fetchall())
        if (count > 0):
            print("Login Success!")
            self.CID = cid
            return True
        else:
            print("Username or Password incorrect.")
            return False
        
            
    def signup(self, fname, lname, email, address, phone, password):
        self.cursor.execute("SELECT MAX(CID) FROM CUSTOMER")
        cid = str(int(self.cursor.fetchall()[0][0]) + 1)
        try:
            self.cursor.execute("INSERT INTO CUSTOMER VALUES('%s','%s','%s','%s','%s','%s', '%d', '%s')" % (cid, fname, lname, email, address, phone, 0, password))
            self.db.commit()
            print("Sucess.\n UserID:'%s'\n Email:'%s'\n" %(cid, email))
        except:
            self.db.rollback()
            print("Failed.\n")


    def delete(self, cid):
        sql = "DELETE FROM CUSTOMER WHERE CID = '%s'" %cid
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()


    def revise(self):
        pass


    def closedb(self):
        self.db.close()
        



class Cart(object):
    def __init__(self, Sign):
        self.db =pymysql.connect(db = 'store', user = 'shiboyao', passwd = '1234')
        self.cursor = self.db.cursor()
        self.CID = Sign.CID
        
        self.cursor.execute("SELECT MAX(CARTID) FROM CART WHERE CID = '%s' AND TSTATUS = 0" %self.CID)
        cartid = self.cursor.fetchall()
        if cartid[0][0] is not None:
            self.cartid = cartid[0][0]
        else:
            sql = "SELECT MAX(CARTID) FROM CART"
            self.cursor.execute(sql)
            cartid = self.cursor.fetchall()
            self.cartid = str(int(cartid[0][0])+1)
            sql = "INSERT INTO CART (CARTID,CID,TSTATUS,TDATE) VALUES ('%s', '%s', 0, CURDATE())" %(self.cartid, self.CID, )
            self.cursor.execute(sql)
            self.db.commit()
        '''
        self.cursor.execute("SELECT PID FROM APPEARS_IN WHERE CARTID = '%s' AND CID = '%s'" %(self.cartid, self.CID))
        self.pid = self.cursor.fetchall()[0]
        self.cursor.execute("SELECT QUANTITY FROM APPEARS IN WHERE CARTID = '%s' AND CID = '%s'" %(self.cartid, self.CID))
        self.quant = 
        ''' 
 
    def addproduct(self, pid, quant):
        self.cursor.execute("SELECT PPRICE FROM PRODUCT WHERE PID = '%s'" %pid)
        price = self.cursor.fetchall()[0][0]
        try:
            self.cursor.execute("INSERT INTO APPEARS_IN (CARTID, PID, QUANTITY, PRICESOLD) VALUES('%s','%s','%d','%f')" %(self.cartid, pid, quant, price))
            self.db.commit()
            return True
        except:
            self.db.rollback()
            print("Failed to insert in appears_in.\n")
            return False
            
            
    def deleteproduct(self, pid):
        try :
            self.cursor.execute("DELETE FROM APPEARS_IN WHERE PID = '%s' AND CARTID = '%s'" %(pid, self.cartid))
            self.db.commit()
            return True
        except :
            self.db.rollback()
            print("FAiled to delte item.\n")
            return False
            
              
    def addoption(self):
        self.cursor.execute("SELECT SANAME FROM SHIP_ADDRESS WHERE CID = '%s'" %self.CID)
        return self.cursor.fetchall()
        
        
    def addinsert(self, receipient, country, state, city, zipcode, street, snum, sname):
        try:
            self.cursor.execute("INSERT INTO SHIP_ADDRESS VALUES('%s', '%s','%s','%s','%s','%s','%s','%s','%s')" %(self.CID, receipient, country, state, city, zipcode, street, snum, sname))
            self.db.commit()
            return True
        except:
            self.db.rollback()
            print("Failed to add add.\n")
            return False
            
            
    def ccoption(self):
        self.cursor.execute("SELECT CCNUMBER FROM STORED_CARD WHERE CID = '%s'" %self.CID)
        return self.cursor.fetchall()
    
    
    def addcc(self, ccnum, secnum, owner, typ, billing, exp, stored):
        try:
            self.cursor.execute("INSERT INTO CREDIT_CARD VALUES('%s','%s','%s','%s','%s', '%s', '%d')" %(ccnum, secnum, owner, typ, billing, exp, stored))
            self.db.commit()
            if stored == 1:
                self.cursor.execute("INSERT INTO STORED_CARD VALUES('%s', '%s')" %(ccnum, self.CID))
                self.db.commit()
            return True
        except:
            self.db.rollback()
            print("Failed to add cc.\n")
            return False
    
    
    def view(self):
        try:
            self.cursor.execute("SELECT P.PNAME, A.QUANTITY, P.PPRICE FROM CART C, APPEARS_IN A, PRODUCT P WHERE C.CARTID = A.CARTID AND C.CID = '%s' AND A.PID = P.PID" %self.CID)
            result = self.cursor.fetchall()
            print(result)
            return result
        except:
            print("Failed to view.\n")
            return False
            
    
    def checkout(self, addname, ccnum):
        try:
            self.cursor.execute("UPDATE CART SET SANAME = '%s', CCNUMBER = '%s', TSTATUS = 1, TDATE = CURDATE() WHERE CID = '%s' AND CARTID = '%s'" %(addname, ccnum, self.CID, self.cartid))
            self.db.commit()
            return True
        except:
            self.db.rollback()
            print("Failed to checkout.\n")
            return False
            
            

class User(object):
    def __init__(self, Sign):
        self.db =pymysql.connect(db = 'store', user = 'shiboyao', passwd = '1234')
        self.cursor = self.db.cursor()
        self.CID = Sign.CID
        
        
    def viewprofile(self):
        try:
            self.cursor.execute("SELECT CID, FNAME, LNAME, EMAIL, ADDRESS, PHONE, STATUS FROM CUSTOMER WHERE CID = '%s'" %self.CID)
            result = self.cursor.fetchall()
            print(result[0])
            return result[0]
        except:
            print("Failed to view profile.\n")
            return False
            
            
    def viewhistory(self):
        self.cursor.execute("SELECT C.CARTID, C.SANAME, C.CCNUMBER, C.TSTATUS, C.TDATE, A.PID, A.QUANTITY, A.PRICESOLD, P.PTYPE, P.PNAME, P.DESCRIPTION FROM CART C, APPEARS_IN A, PRODUCT P WHERE C.CARTID = A.CARTID AND P.PID = A.PID AND C.CID = '%s'" %self.CID)
        result = self.cursor.fetchall()
        print(result)
        return result
            
            
    def viewbypname(self, pname):
        self.cursor.execute("SELECT C.CARTID, C.SANAME, C.CCNUMBER, C.TSTATUS, C.TDATE, A.PID, A.QUANTITY, A.PRICESOLD, P.PTYPE, P.PNAME, P.DESCRIPTION FROM CART C, APPEARS_IN A, PRODUCT P WHERE C.CARTID = A.CARTID AND P.PID = A.PID AND C.CID = %s AND P.PNAME LIKE %s" ,(self.CID, ("%"+pname+"%")))
        result = self.cursor.fetchall()
        print(result)
        return result
        
        
    def viewbyptype(self, ptype):
        self.cursor.execute("SELECT C.CARTID, C.SANAME, C.CCNUMBER, C.TSTATUS, C.TDATE, A.PID, A.QUANTITY, A.PRICESOLD, P.PTYPE, P.PNAME, P.DESCRIPTION FROM CART C, APPEARS_IN A, PRODUCT P WHERE C.CARTID = A.CARTID AND P.PID = A.PID AND C.CID = %s AND P.PTYPE LIKE %s" ,(self.CID, ("%"+ptype+"%")))
        result = self.cursor.fetchall()
        print(result)
        return result
        
        
    def viewbystatus(self, status):
        self.cursor.execute("SELECT C.CARTID, C.SANAME, C.CCNUMBER, C.TSTATUS, C.TDATE, A.PID, A.QUANTITY, A.PRICESOLD, P.PTYPE, P.PNAME, P.DESCRIPTION FROM CART C, APPEARS_IN A, PRODUCT P WHERE C.CARTID = A.CARTID AND P.PID = A.PID AND C.CID = %s AND C.TSTATUS = %s" ,(self.CID, status))
        result = self.cursor.fetchall()
        print(result)
        return result
        
        
        
class admin(object):
    def __init__(self, Sign):
        self.db =pymysql.connect(db = 'store', user = 'root', passwd = 'wobuzhidao')
        self.cursor = self.db.cursor()
        self.CID = Sign.CID
        
        
    def processorder(self, cartid, status):
        try:
            self.cursor.execute("UPDATE CART SET TSTATUS = '%s' WHERE CARTID = '%s'" %(status, cartid))
            self.db.commit()
            return True
        except:
            print("Failed to process.\n")
            return False
            
            
    def mostsold(self, date1, date2):
        '''
        most frequent products
        '''
        self.cursor.execute("SELECT SUM(A.QUANTITY), P.PNAME FROM CART C, APPEARS_IN A, PRODUCT P WHERE C.CARTID = A.CARTID AND C.TDATE BETWEEN '%s' AND '%s' AND A.PID = C.PID GROUP BY A.PID ORDER BY SUM(A.QUANTITY) DESC" %(date1, date2))
        result = self.cursor.fetchall()[0]
        return result
        
        
    def mostsold2(self, date1, date2):
        '''
        most popular to distinct customers
        '''
        SELF.CURSOR.EXECUTE("SELECT COUNT(C.CID), P.PNAME FROM CART C, APPEARS_IN A, PRODUCT P WHERE C.CARTID = A.CARTID AND C.TDATE BETWEEN '%s' AND '%s' AND A.PID = P.PID GROUP BY A.PID ORDER BY COUNT(C.CID) DESC" %(date1, date2))
        result = self.cursor.fetchall()[0]
        return result
        
        
    def ten_customers(self):
        '''
        spent most money
        '''
        SELF.CURSOR.EXECUTE("SELECT C.CID, CUSTOMER.FNAME, SUM(A.PRICESOLD*A.QUANTITY) FROM CUSTOMER, CART C, APPEARS_IN A, PRODUCT P WHERE C.CID = CUSTOMER.CID AND C.CARTID = A.CARTID AND C.TDATE BETWEEN '%s' AND '%s' AND A.PID = P.PID GROUP BY C.CID ORDER BY SUM(A.PRICESOLD*A.QUANTITY) DESC" %(date1, date2))
        result = self.cursor.fetchall()
        return result[:min(10, len(result))]
        
        
    def five_zip(self):
        '''
        shipments made
        '''
        SELF.CURSOR.EXECUTE("SELECT S.ZIP, COUNT(*) FROM CART C, SHIP_ADDRESS S WHERE C.SANAME = S.SANAME  AND C.TDATE BETWEEN '%s' AND '%s' GROUP BY S.ZIP ORDER BY COUNT(*) DESC" %(date1, date2))
        result = self.cursor.fetchall()
        return result[:min(5, len(result))]
        
        
    def avg_price(self):
        '''
        per product type, desktop, laptop, printer
        '''
        SELF.CURSOR.EXECUTE("SELECT P.PTYPE, AVG(A.PRICESOLD) FROM CART C, PRODUCT P, APPEARS_IN A WHERE C.CARTID = A.CARTID AND A.PID = P.PID AND C.TDATE BETWEEN '%s' AND '%s' GROUP BY P.PTYPE ORDER BY AVG(A.PRICESOLD) DESC" %(date1, date2))
        result = self.cursor.fetchall()
        return result
        

        
        
    
