import pandas as pd
import sqlite3

def modal(request):
    feature_name = request.POST.get('feature_name').split('%')

    feature1 = feature_name[0]
    name1 = feature_name[1]

    feature2 = feature_name[2]
    name2 = feature_name[3]

    try:
        connect = sqlite3.connect('db.sqlite3')
        db_cursor = connect.cursor()

        select = 'SELECT SystematicName FROM ' + feature1 +'_all WHERE '+ feature1 +" IN ('" +name1 +"')"
        db_cursor.execute(select)
        sys_name1 = db_cursor.fetchall()
        sys_name1_set = set(eval(sys_name1[0][0]))

        # print('---------------')

        select = 'SELECT SystematicName FROM ' + feature2 +'_all WHERE '+ feature2 +" IN ('" + name2 +"')"
        db_cursor.execute(select )
        sys_name2 = db_cursor.fetchall()
        sys_name2_set = set(eval(sys_name2[0][0]))
        intersection = str(tuple(sys_name1_set.intersection(sys_name2_set)))
        print(intersection)
        if feature1 == 'Physical_Interation':
            select = "SELECT * FROM " + feature1 + "_evidence WHERE SystematicName IN" + intersection
        elif feature1 == 'Genetic_Interation':
            pass
        else:
            select = "SELECT * FROM " + feature1 + "_evidence WHERE SystematicName IN" + intersection
            evidence_table = pd.read_sql(select , connect)
    finally:
        connect.close()
    print(evidence_table)
    response = {'asd':'asdadasdasda'}
    return response