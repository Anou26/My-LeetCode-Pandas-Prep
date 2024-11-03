import pandas as pd

def find_second_highest_salary(employees: pd.DataFrame) -> pd.DataFrame:
    employees['dept_rank'] = employees.groupby('dept').salary.rank(method='dense', ascending=False)
    employees = employees[employees.dept_rank == 2]
    return employees[['emp_id', 'dept']].sort_values('emp_id')