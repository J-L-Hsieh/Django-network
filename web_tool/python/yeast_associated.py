import pandas as pd
import sqlite3


def associated_analysis(associated_table):
    associated_table = pd.DataFrame(associated_table)
    '''-------------------------queried feature data---------------------'''
    queried_feature = associated_table.iat[0,0]
    queried_count = associated_table.iat[0,1]
    queried_name = associated_table.iat[0,2]
    '''------------------------------------------------------------------'''
    associated_table.drop(associated_table.columns[[0,1,2]],axis=1,inplace=True)
    column_name = associated_table.columns.values.tolist()
    column_order = column_name[0:]
    response ={}
    for i in column_name:
        print(i)
        print(associated_table.at[0,'%s' %i])
        domain_name = eval(associated_table.at[0,'%s' %i])
        table = []
        for j in domain_name:
            try:
                connect = sqlite3.connect('db.sqlite3')
                db_cursor = connect.cursor()
                select = 'SELECT SystematicName FROM ' + i +'_all WHERE '+ i +" IN ('" + j +"')"
                # print(select)
                domain_name = db_cursor.execute(select).fetchone()
                domain_name = domain_name[0]
                result_list = yeast_enrichment(queried_name,domain_name)
                result_list.insert(0,queried_feature)
                result_list.insert(1,j)
                # print(result_list)
                table.append(result_list)
            finally:
                connect.close()
        columns_title = ['Queried %s Term(A)' %queried_feature,'Associated %s Term(B)' %i,'#of genes in A','#of genes in B','#of genes in A∩B', '#of genes in yeast','Signficance of Associated(p-value)']
        print(pd.DataFrame(table,columns=columns_title))
        df_tables = pd.DataFrame(table,columns=columns_title).to_html(table_id='%s_table'%i,index= None,classes="table table-striped table-bordered")
        response['%s'%i] = df_tables
        response['column_order'] = column_order
    # print(response)
    return response

'''-----------------------------------------yeast enrichment---------------------------------------'''
import scipy.stats
from statsmodels.stats.multitest import multipletests

def fisher(A,B,C,D) :

    T = int(A)      #交集數         1      剩下的交集處
    S = int(B)      #輸入 genes數   18    輸入一總數
    G = int(C)      #genes 樣本數   1117   篩選的樣本
    F = int(D)      #總 genes數     6572  輸入二總數

    S_T = S-T
    G_T = G-T
    F_G_S_T = F-G-S+T

    oddsratio, pvalue_greater = scipy.stats.fisher_exact( [ [T,G_T] , [S_T,F_G_S_T]] ,'greater')
    oddsratio, pvalue_less = scipy.stats.fisher_exact( [ [T,G_T] , [S_T,F_G_S_T]] ,'less')

    return pvalue_greater


def yeast_enrichment(queried_name,domain_name):

    queried_name = eval(queried_name)
    domain_name = eval(domain_name)

    # print(queried_name,domain_name)

    D = 6611
    C = len(domain_name)

    B = len(queried_name)



    list_A = list(set(queried_name)&set(domain_name))
    A = len(list_A)
    test = fisher(A, B, C, D)



    cut_off = 0.01
    P_value_corr_FDR = multipletests(test,alpha=cut_off, method= "fdr_bh")
    P_value_corr_Bon = multipletests(test,alpha=cut_off, method= "bonferroni")


    result = pd.DataFrame({"P-value":test,"FDR":P_value_corr_FDR[1],"Bonferroni":P_value_corr_Bon[1]})
    result = result[result["FDR"]<=0.01]

    response = []
    response.extend([len(queried_name),len(domain_name),A,6611,result.iat[0,1]])
    # print(response)

    return response
