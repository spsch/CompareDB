import pyodbc
## working now
config = {
    'ServerMX':'cxcldsrcnxqas01.database.windows.net',
    'DatabaseMX':'cxclddbcnxmaqas',
    'User':'jsvehlak',
    'PwdMX':'Passw0rd426'
}

stream = ('SERVER={ServerMX};' + 'DATABASE={DatabaseMX};' + 'UID={User};' + 'PWD={PwdMX}')
print('Connecting to: ' + config['ServerMX'] + ' and DB: ' + config['DatabaseMX'] )

try:
    myconnect = pyodbc.connect(
        r'DRIVER={SQL Server Native Client 11.0};' +
        stream.format(**config))
    cursor = myconnect.cursor()
    print('OK')
except(pyodbc.InterfaceError, KeyError):
    print('Bad login or pwd')
print('*****')
rows = cursor.execute('SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE COLUMN_NAME LIKE \'%ProductTbl%\' ORDER BY TABLE_NAME').fetchall()
for row in rows:
    print(row.TABLE_NAME)


for row in cursor.columns(table='dbo.ProductTbl'):
    print('Columns: ')
    print (row.column_name)
print (' END')