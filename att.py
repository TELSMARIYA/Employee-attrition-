import streamlit as st
import pickle 
model=open('rfc.pickle', 'rb')
clf=pickle.load(model)
model.close()

map_pickle=open('map.pickle', 'rb')
unique_mapping=pickle.load(map_pickle)
map_pickle.close()

satisfaction_level=st.number_input('satisfaction_level', 0.0, 1.0, 0.0)
last_evaluation=st.number_input('last_evaluation', 0.0, 1.0, 0.0)
number_project= st.number_input('number_project', 2,7,2)
average_montly_hours=st.number_input('average_montly_hours',96, 310, 96)
time_spend_company=st.number_input('time_spend_company', 2, 10, 2)
Work_accident=st.selectbox('Work_accident', options=[0,1])
promotion_last_5years=st.selectbox('promotion_last_5years', options=[0,1])
department=st.selectbox('department', options=['sales', 'accounting', 'hr', 'technical', 'support', 'management',
       'IT', 'product_mng', 'marketing', 'RandD'])
salary=st.selectbox('salary', options=['low', 'medium', 'high'])

department_IT, department_RandD,department_accounting, department_hr, department_management,department_marketing, department_product_mng, department_sales, department_support,  department_technical=0,0,0,0,0,0,0,0,0,0,

salary_high,salary_low,salary_medium=0,0,0

if 'salary'=='high':
    salary_high=1
elif 'salary'=='medium':
    salary_medium=1
elif 'salary'=='low':
    salary_low==1
    
if 'department'=='sales':
    department_sales==1
elif 'department'=='accounting':
    department_accounting=1
elif 'department'=='hr':
    department_hr=1
elif 'department'=='technical':
    department_technical==1
elif 'department'=='support':
    department_support==1
elif 'department'=='management':
    department_management==1
elif 'department'== 'IT':
    department_IT=1
elif 'department'=='product_mng':
    department_product_mng=1
elif 'department'=='marketing':
    department_marketing=1
elif 'department'=='RandD':
    department_RandD=1
    
new_pred=clf.predict([[satisfaction_level, last_evaluation, number_project,
       average_montly_hours, time_spend_company, Work_accident,
       promotion_last_5years, department_IT, department_RandD,
       department_accounting, department_hr, department_management,
       department_marketing, department_product_mng, department_sales,
       department_support, department_technical, salary_high,
       salary_low, salary_medium]])

prediction=unique_mapping[new_pred][0]
st.write(prediction)
