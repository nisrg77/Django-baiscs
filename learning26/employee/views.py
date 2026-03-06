from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm,CourseForm

# Create your views here.
def employeeList(request):
    #employees = Employee.objects.all() #select * from employee
    employees = Employee.objects.all().order_by("id").values()
    #employees = Employee.objects.all().values_list()
    print(employees)
    return render(request, 'employee/employeeList.html',{"employees":employees})

def employeeFilter(request):
    #where select  from employee where name = "raj"
    employee = Employee.objects.filter(name ="raj").values()
    #selet  from employee where post = "Developer"
    employee2 = Employee.objects.filter(post ="Developer").values()
    #select  from employee where name = "raj" and post = "Developer"
    employee3 = Employee.objects.filter(name ="raja",post ="Developer").values()
    #select  from employee where name = "raj" or post = "Developer"
    
    #>23
    #seelct  from employee where age > 23
    #employee4 = Employee.objects.filter(age>23).values()
    employee4 = Employee.objects.filter(age__gt=23).values()
    employee5 = Employee.objects.filter(age__gte=23).values()
 

        #lt , lte
    # employee6 = Employee.objects.filter(age__lt=23).values()
    # employee7 = Employee.objects.filter(age__lte=23).values()
    

    #string queries
    employee6 = Employee.objects.filter(post__exact="Developer").values()
    employee7 = Employee.objects.filter(post__iexact="developer").values()

    #contains
    employee8 = Employee.objects.filter(name__contains="r").values()
    employee9 = Employee.objects.filter(name__icontains="R").values()

    #startswith endswith
    employee10 = Employee.objects.filter(name__startswith="R").values()
    employee11 = Employee.objects.filter(name__endswith="R").values()
    employee12 = Employee.objects.filter(name__istartswith="R").values()
    employee13 = Employee.objects.filter(name__iendswith="R").values()

     #in
    employee14 = Employee.objects.filter(name__in=["raj","jay"]).values()    

    #range
    employee15 = Employee.objects.filter(age__range=[24,30]).values()    

    #order by
    employee16 = Employee.objects.order_by("age").values()     #asc
    employee17 = Employee.objects.order_by("-age").values()    #desc

    employee18 = Employee.objects.order_by("-salary").values()    #desc




    print("query1",employee,flush=True)
    print("query2",employee2)
    print("query3",employee3)
    print("query4",employee4)
    print("query5",employee5)
    print("query6",employee6)
    print("query7",employee7)
    print("query8",employee8)
    print("query9",employee9)
    print("query10",employee10)
    print("query11",employee11)
    print("query12",employee12)
    print("query13",employee13)
    print("query14",employee14)
    print("query15",employee15)
    print("query16",employee16)
    print("query17",employee17)
    print("query18",employee18)


    context = {
        "employee_lists" : {
                'employee':employee,
                'employee2':employee2,
                'employee3':employee3,
                'employee4':employee4,
                'employee5':employee5,
                'employee6':employee6,
                'employee7':employee7,
                'employee8':employee8,
                'employee9':employee9,
                'employee10':employee10,
                'employee11':employee11,
                'employee12':employee12,
                'employee13':employee13,
                'employee14':employee14,
                'employee15':employee15,
                'employee16':employee16,
                'employee17':employee17,
                'employee18':employee18,
                }
     }
    return render(request,'employee/employeeFilter.html',context)

def createEmployee(request):    
    Employee.objects.create(name="ajay",age=23,salary=23000,post="HR",join_date="2022-01-01")
    return HttpResponse("EMPLOYEE CREATED...")

def createEmployeeWithForm(request):
    print(request.method)
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        form.save() #it same as create
        #return HttpResponse("EMPLOYEE CREATED...")
        return redirect("employeeList")
    else:
        #form object create --> html
        form = EmployeeForm() #form object        
        return render(request,"employee/createEmployeeForm.html",{"form":form})
    

def createCourse(request):
    if request.method == "POST":
        form = CourseForm(request.POST) #csrftoken,form alll fileds data
        form.save() #create.. insert into table 
        return HttpResponse("COURSE CREATED...")
    else:
        form = CourseForm()
        return render(request,"employee/createCourse.html",{"form":form})     