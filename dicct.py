dict={
    1000:{

    },
    "ID":{
        "Name":"Proximus"

    },
    1001:{

    }
}

employee_dict={
    10001:{"Name":"Abdul Rahman",
           "Department":"Human Resources",
           "Job title":"HR manager",
           "Annual Salary":82000.00,
           "Employment Status":True
    },
    10002:{"Name":"Bobby chan",
           "Department":"Engineering",
           "Job title":"Software engineering",
           "Annual Salary":74000.50,
           "Employment Status":True
    },
    "ID":{

    },
   "ID":{

   }

}
employee_dict.update({"ID":{}})
employee_dict[10005]=employee_dict["ID"]
del employee_dict["ID"]
employee_dict.update({"ID":{}})
print(employee_dict)
