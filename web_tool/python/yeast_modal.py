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

        select = 'SELECT SystematicName FROM ' + feature1 +'_1_to_10 WHERE '+ feature1 +" IN ('" +name1 +"')"
        db_cursor.execute(select)
        sys_name1 = db_cursor.fetchall()
        sys_name1_set = set(eval(sys_name1[0][0]))

        # print('---------------')

        select = 'SELECT SystematicName FROM ' + feature2 +'_1_to_10 WHERE '+ feature2 +" IN ('" + name2 +"')"
        db_cursor.execute(select )
        sys_name2 = db_cursor.fetchall()
        sys_name2_set = set(eval(sys_name2[0][0]))
        intersection = str(tuple(sys_name1_set.intersection(sys_name2_set)))
        print(intersection)
        print(feature1)
        '''-------------------------依照主要的feature取出證據檔------------------'''
        if feature1 == 'Physical_Interaction':
            select = f"""
                SELECT * FROM %s_evidence WHERE `SystematicName(Bait)` IN %s OR `SystematicName(Hit)` IN %s
            """%(feature1, intersection,intersection)
            evidence_table = pd.read_sql(select , connect)


        elif feature1 == 'Genetic_Interaction':
            select = f"""
                SELECT * FROM %s_evidence WHERE `SystematicName(Bait)` IN %s OR `SystematicName(Hit)` IN %s
            """%(feature1, intersection,intersection)
            evidence_table = pd.read_sql(select , connect)

        else:
            select = f"""
                SELECT * FROM %s_evidence WHERE SystematicName IN %s
            """%(feature1, intersection)
            evidence_table = pd.read_sql(select , connect)
    finally:
        connect.close()
    print(evidence_table)
    print('-------------')
    result = evidence_table.to_json(orient="records")
    print(result)

    evidence_table = evidence_table.to_html(table_id='evidence_table', index= None, classes="table table-striped table-bordered", escape=False)
    return evidence_table