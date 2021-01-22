from sql import dbManager

print(dbManager.dbinit("wxmp"))
a='test'
wxmp = dbManager("wxmp",'INFGate')
wxmp.cur.execute("INSERT INTO essays (author,title,content,date) VALUES (%s,%s,%s,%s)",(a,a,a,'20210119'))