def minmaxsal(depdata):
    minmaxsal={}
    for deptno,emp in depdata.items():
        sal=list(emp.values())
        minmaxsal[deptno]=["minsalary":min(sal),"maxsalary":max(sal))}
        print(deptno)
        print(minmaxsal[deptno])
deptdata={
