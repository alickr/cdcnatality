from sqlalchemy import create_engine

def to_sql(dataFrame, table_name):
    engine = create_engine('mysql+pymysql://root:@localhost/nycds_project', pool_recycle=3600)
    connection = engine.raw_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO " + table_name + " ( "
    sql_val = "VALUES ("
    temp1 = ''
    for i, col in enumerate(dataFrame.columns):
        sql += temp1 + col
        sql_val += temp1 + "%s"
        temp1 = ', '
    print("sql done!")
    sql = sql + ") " + sql_val + ")"

    val = []
    for index, row in dataFrame.iterrows():
        val.append(tuple(list(row)))
        if index > 0 and index % 10000 == 0:
            cursor.executemany(sql, val)
            connection.commit()
            val = []
            print("insert 10000")

    cursor.executemany(sql, val)
    connection.commit()
    connection.close()
    print("done!")
    return True

# importToSQL(table_child,"child")


def reduce_columns(dataSource, columns, years, table_name):
    reduced = dataSource.filter(columns)
    if columns.index('child_id') > 0:
        columns.remove('child_id')
    dataSource = dataSource.drop(columns, axis=1)
    # df_converter.to_sql(table_child, "child")
    reduced.to_csv("data/" + str(years) + table_name + ".csv")
    return dataSource
