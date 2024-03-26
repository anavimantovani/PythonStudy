# Author: Ana Victoria Gomes Mantovani
# Date: 07/07/2023
# Assignment 4.1 - 4.1_company_directory.py

def main():
    
    #Prompt user for the company name
    company_name = input("Enter company's name: ").title()
    print()
    
    #Create an empty dictionary to store the employee's name and job
    employees = {}

    #Prompt user for emplyee's name and job until they decide to quit (q)
    while True:
        employee_name = input("Enter next employee's name ('q' to quit): ")
        if employee_name.lower() == 'q':
            break
        employee_job = input("Enter employee's job: ")
        employees[employee_name.title()] = employee_job.title()
        print()

    #Loop through the dictionary to print the company's employees and jobs
    print()
    print(f"{company_name} directory:")
    print("------------------------------------------------------------")

    for employee, job in employees.items():
        print(f"{employee:<20}: {job}")

    print("------------------------------------------------------------")

#Start the program
if __name__ == '__main__':
    main()