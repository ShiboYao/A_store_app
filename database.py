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
            return cid
        except:
            self.db.rollback()
            print("Failed.\n")
            return False


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
    def __init__(self, cid):
        self.db =pymysql.connect(db = 'store', user = 'shiboyao', passwd = '1234')
        self.cursor = self.db.cursor()
        self.CID = cid
        
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
        r = self.cursor.fetchall()
        if not r:
            print("PID not exist.")
            return False
        else:
            price = r[0][0]
        self.cursor.execute("SELECT CID FROM SILVER_AND_ABOVE")
        above = self.cursor.fetchall()
        r1 = ()
        if (self.CID,) in above:
            self.cursor.execute("SELECT OFFERPRICE FROM OFFER_PRODUCT WHERE PID = '%s'" %pid)
        else :
            self.cursor.execute("SELECT PPRICE FROM PRODUCT WHERE PID = '%s'" %pid)
        r1 = self.cursor.fetchall()
        if r1:
            price = r1[0][0]

        try:
            self.cursor.execute("INSERT INTO APPEARS_IN VALUES (%s,%s,%s,%s)", (self.cartid, pid, quant, price))
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
               
            
    def ccoption(self):
        self.cursor.execute("SELECT CCNUMBER FROM STORED_CARD WHERE CID = '%s'" %self.CID)
        return self.cursor.fetchall()
    
    
    def view(self): ## view cart
        try:
            self.cursor.execute("SELECT P.PNAME, A.QUANTITY, A.PRICESOLD FROM CART C, APPEARS_IN A, PRODUCT P WHERE C.CARTID = A.CARTID AND C.CID = %s AND C.CARTID = %s AND A.PID = P.PID", (self.CID, self.cartid))
            result = self.cursor.fetchall()
            return result
        except:
            print("Failed to FETCH REGULAR.\n")
            return False
            

            
    def viewbytype(self, ptype): ## view product
        try:
            self.cursor.execute("SELECT CID FROM SILVER_AND_ABOVE")
            above = self.cursor.fetchall()
            print(above)
        except:
            print("Failed to search silver and above.\n")
            
        if ptype != 'All':
            try:
                self.cursor.execute("SELECT P.PNAME, P.PID, P.DESCRIPTION, P.PPRICE FROM PRODUCT P WHERE P.PTYPE = '%s'" %ptype)
                result = self.cursor.fetchall()
                return result
            except:
                print("Fail to view.\n")
                return False
        else:
            self.cursor.execute("SELECT P.PNAME, P.PID, P.DESCRIPTION, P.PPRICE FROM PRODUCT P")
            result = self.cursor.fetchall()
            if (self.CID,) in above:
                try:
                    self.cursor.execute("SELECT * FROM OFFER_PRODUCT")
                    r = self.cursor.fetchall()
                except:
                    print("Failed to get offer.\n")
                print(result,r)
                return result+r
            else:
                return result
    
    
    def checkout(self, addname, ccnum):
        try:
            self.cursor.execute("UPDATE CART SET SANAME = %s, CCNUMBER = %s, TSTATUS = %s, TDATE = CURDATE() WHERE CID = %s AND CARTID = %s", (addname, ccnum, 1,self.CID, self.cartid))
            self.db.commit()
            return True
        except:
            self.db.rollback()
            print("Failed to checkout.\n")
            return False
            
            

class User(object):
    def __init__(self, cid):
        self.db =pymysql.connect(db = 'store', user = 'shiboyao', passwd = '1234')
        self.cursor = self.db.cursor()
        self.CID = cid
        
        
    def viewprofile(self):
        try:
            self.cursor.execute("SELECT CID, FNAME, LNAME, EMAIL, ADDRESS, PHONE, STATUS FROM CUSTOMER WHERE CID = '%s'" %self.CID)
            result = self.cursor.fetchall()
            print(result)
            return result
        except:
            print("Failed to view profile.\n")
            return False
            
            
    def update(self, fname, lname, email, address, phone, password):
        try:
            self.cursor.execute("UPDATE CUSTOMER SET FNAME = %s, LNAME = %s, EMAIL = %s, ADDRESS = %s, PHONE = %s, PASSWORD = %s WHERE CID = %s", (fname, lname, email, address, phone, password, self.CID))
            self.db.commit()
            return True
        except:
            self.db.rollback()
            print("Fail to update.\n")
            return False


    def addoption(self):
        self.cursor.execute("SELECT SANAME FROM SHIP_ADDRESS WHERE CID = '%s'" %self.CID)
        return self.cursor.fetchall()
               
            
    def ccoption(self):
        self.cursor.execute("SELECT CCNUMBER FROM STORED_CARD WHERE CID = '%s'" %self.CID)
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
            
                        
    def viewhistory(self):
        self.cursor.execute("SELECT C.CARTID, C.SANAME, C.CCNUMBER, C.TSTATUS, C.TDATE, A.PID, A.QUANTITY, A.PRICESOLD, P.PTYPE, P.PNAME, P.DESCRIPTION FROM CART C, APPEARS_IN A, PRODUCT P WHERE C.CARTID = A.CARTID AND P.PID = A.PID AND C.CID = '%s'" %self.CID)
        result = self.cursor.fetchall()
        self.cursor.execute("SELECT C.CARTID, SUM(A.PRICESOLD*A.QUANTITY) FROM CART C, APPEARS_IN A WHERE C.CARTID = A.CARTID AND C.CID = '%s' GROUP BY C.CARTID"  %self.CID)
        r2 = self.cursor.fetchall()
        print(result, r2)
        return result+r2
            
            
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
        
        
        
class Admin(object):
    def __init__(self):
        self.db =pymysql.connect(db = 'store', user = 'shibo', passwd = '1234')
        self.cursor = self.db.cursor()
        #self.CID = Sign.CID


    def viewbystatus(self, status):
        self.cursor.execute("SELECT C.CARTID, C.TSTATUS, C.TDATE FROM CART C WHERE C.TSTATUS = %s" ,(status))
        result = self.cursor.fetchall()
        print(result)
        return result
                
        
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
        self.cursor.execute("SELECT SUM(A.QUANTITY), P.PNAME FROM CART C, APPEARS_IN A, PRODUCT P WHERE C.CARTID = A.CARTID AND C.TDATE BETWEEN '%s' AND '%s' AND A.PID = P.PID GROUP BY A.PID ORDER BY SUM(A.QUANTITY) DESC" %(date1, date2))
        result = self.cursor.fetchall()
        if len(result) != 0:
            return result[0]
        else:
            return result
        
        
    def mostsold2(self, date1, date2):
        '''
        most popular to distinct customers
        '''
        self.cursor.execute("SELECT COUNT(C.CID), P.PNAME FROM CART C, APPEARS_IN A, PRODUCT P WHERE C.CARTID = A.CARTID AND C.TDATE BETWEEN '%s' AND '%s' AND A.PID = P.PID GROUP BY A.PID ORDER BY COUNT(C.CID) DESC" %(date1, date2))
        result = self.cursor.fetchall()
        if len(result) != 0:
            return result[0]
        else:
            return result
        
        
    def ten_customer(self, date1, date2):
        '''
        spent most money
        '''
        self.cursor.execute("SELECT C.CID, CUSTOMER.FNAME, SUM(A.PRICESOLD*A.QUANTITY) FROM CUSTOMER, CART C, APPEARS_IN A, PRODUCT P WHERE C.CID = CUSTOMER.CID AND C.CARTID = A.CARTID AND C.TDATE BETWEEN '%s' AND '%s' AND A.PID = P.PID GROUP BY C.CID ORDER BY SUM(A.PRICESOLD*A.QUANTITY) DESC" %(date1, date2))
        result = self.cursor.fetchall()
        return result[:min(10, len(result))]
        
        
    def five_zip(self, date1, date2):
        '''
        shipments made
        '''
        self.cursor.execute("SELECT S.ZIP, COUNT(*) FROM CART C, SHIP_ADDRESS S WHERE C.SANAME = S.SANAME  AND C.TDATE BETWEEN '%s' AND '%s' GROUP BY S.ZIP ORDER BY COUNT(*) DESC" %(date1, date2))
        result = self.cursor.fetchall()
        return result[:min(5, len(result))]
        
        
    def avg_price(self, date1, date2):
        '''
        per product type, desktop, laptop, printer
        '''
        self.cursor.execute("SELECT P.PTYPE, AVG(A.PRICESOLD) FROM CART C, PRODUCT P, APPEARS_IN A WHERE C.CARTID = A.CARTID AND A.PID = P.PID AND C.TDATE BETWEEN '%s' AND '%s' GROUP BY P.PTYPE" %(date1, date2))
        result = self.cursor.fetchall()
        return result 
        


def tupleMsg(t):
    if t == False or len(t) == 0:
        return "Nothing."
    else:
        msg = str()
        if t[0] != tuple:
            for m in t:
                msg = msg + '\n\n' + str(m)
        else:
            for m in t:
                line = str()
                for n in m:
                    line = line + ' ' + str(n)
                msg = msg + '\n\n' + line
                
        return msg 
            
        
    
