import pandas as pd
import glob

def seperate_file_based_on_year(flow):
    try:
        path_year_file = "D:\\demo\\years.xlsx"
        df_years = pd.read_excel(path_year_file)
        input_path = "D:\\demo\\input"
        output_path = "D:\\demo\\output\\"
        if flow == 'merge':
            list_of_files = glob.glob(input_path + "\\*")
            final_df = pd.DataFrame()
            for n,file in enumerate(list_of_files):
                print("File no. ",n," and name ", file)
                in_df = pd.read_csv(file)                  
                final_df = pd.concat([final_df,in_df])           
            final_df = pd.merge( final_df,df_years, how='inner', on=['year'])
            grp = final_df.groupby(["year"])
            dfs = [grp.get_group((x,)) for x in grp.groups]
            for df in dfs:
                tag_name = df['year'].unique()[0]
                df.to_csv(output_path+str(tag_name)+".csv",index=False)
                print("year -> ",tag_name)
            print("files succesfully seperated------")
       
    except Exception as e:
        print(e)

if __name__ == "__main__":
    seperate_file_based_on_year('merge')












































# import pandas as pd
# import sys
# from os import path
# import glob

# sys.path.append(path.join(path.dirname(__file__), ".."))

# def company_live(flow):

#     try:
#         # path_tag_file = "D:\\Workspace\\dpa_airawat_automation\\input2\\Tags.xlsx"
#         path_tag_file = "../../../../vaibhav_jadhav_sir_project/fund_pulse/etl/amit_etl/tagsfile/Tags.xlsx"
#         # path_tag_file="D:\\vaibhav_jadhav_sir_project\\fund_pulse\\etl\\amit_etl\\tagsfile\\Tags.xlsx"
#         # path_tag_file = "Tags.xlsx"
#         df_tags = pd.read_excel(path_tag_file)
#         print(df_tags.columns)
#         if flow == 'split':
#             # path = "D:\\Workspace\\dpa_airawat_automation\\input\\NCEN_Samples"
#              path = "D:\vaibhav_jadhav_sir_project\fund_pulse\etl\amit_etl\input"
#              list_of_files = glob.glob(path + "\*")
#              for n,file in enumerate(list_of_files):
#                 print("File no. ",n," and name ", file)
#                 in_df = pd.read_csv(file)
#                 in_df = in_df[['tags','value','series_id']]
#                 in_df = pd.merge(df_tags, in_df,  how='inner', left_on=['tags'], right_on = ['tags'])
#                 grp = in_df.groupby(["tags"])
#                 dfs = [grp.get_group(x) for x in grp.groups]
                
#                 file_name = file.replace(".csv", "").replace("input\\", "output\\")
            
#                 for df in dfs:
#                     tag_name = df['tags'].unique().tolist()[0]
#                     df.to_csv(file_name+"_"+tag_name+".csv")
                
#         if flow == 'merge':

#             # path = "D:\\Workspace\\dpa_airawat_automation\\input\\NCEN_Samples"
#             path = "D:\\vaibhav_jadhav_sir_project\\fund_pulse\\etl\\amit_etl\\input"

#             list_of_files = glob.glob(path + "\*")

#             final_df = pd.DataFrame()
#             for n,file in enumerate(list_of_files):
#                 print("File no. ",n," and name ", file)
#                 in_df = pd.read_csv(file)             
#                 in_df = in_df[['Unnamed: 0','tags','value','series_id']] 
#                 print(in_df)         
#                 final_df = pd.concat([final_df,in_df])           
#             final_df = pd.merge( final_df,df_tags, how='inner', left_on=['tags'], right_on = ['tags'])
        
#             grp = final_df.groupby(["tags"])
#             dfs = [grp.get_group(x) for x in grp.groups]

#             # file_name = "D:\\Workspace\\dpa_airawat_automation\\output\\NCEN_Samples\\"
#             file_name = "D:\\vaibhav_jadhav_sir_project\\fund_pulse\\etl\\amit_etl\\output\\"
            
#             for df in dfs:
#                 tag_name = df['tags'].unique().tolist()[0]
#                 df.to_csv(file_name+tag_name+".csv",index=False)
           
#     except Exception as e:
#         print(e)

# if __name__ == "__main__":
   
#     # company_live('split')
#     company_live('merge')