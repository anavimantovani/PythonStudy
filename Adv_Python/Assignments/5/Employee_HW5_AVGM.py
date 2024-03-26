# Author: Ana Victoria Gomes Mantovani
# Date: 10/10/2023
# Program: Payroll System

# Define a class for representing mailing addresses.
class MailingAddress:
    def __init__(self, street, city, state, zip):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip = zip

    # Getter methods to retrieve address components.
    def getStreet(self):
        return self.__street

    def getCity(self):
        return self.__city

    def getState(self):
        return self.__state

    def getZip(self):
        return self.__zip

    # Override the __str__ method to format the address as a string.
    def __str__(self):
        output = self.__street + '\n'
        output += self.__city + ", "
        output += self.__state + "  "
        output += self.__zip
        return output


# Define a base class for representing employees.
class Employee:
    def __init__(self, firstName, lastName, street, city, state, zip):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__address = MailingAddress(street, city, state, zip)

    # Getter methods to retrieve employee information.
    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getAddress(self):
        return self.__address

    # Override the __str__ method to format the employee information as a string.
    def __str__(self):
        output = self.__firstName + ' ' + self.__lastName
        output += "\n" + self.__address.__str__()
        return output

    # Default implementation of calcPay, which returns 0.
    def calcPay(self):
        return 0

# Define a subclass of Employee for commission-based employees.
class CommissionEmployee(Employee):
    def __init__(self, firstName, lastName, street, city, state, zip, sales, commissionRate):
        # Call the superclass constructor.
        super().__init__(firstName, lastName, street, city, state, zip)
        self.__salesAmt = sales
        self.__commissionPct = commissionRate

    # Getter methods to retrieve sales and commission rate.
    def getSalesAmount(self):
        return self.__salesAmt

    def getCommissionPercent(self):
        return self.__commissionPct

    # Override the calcPay method to calculate pay based on commission.
    def calcPay(self):
        return self.__salesAmt * self.__commissionPct

    # Override the __str__ method to format the employee information, including commission details.
    def __str__(self):
        output = super().__str__()  # Call the superclass __str__ method
        output += f"\nSales amount: ${self.__salesAmt:.02f}\n"
        commission = self.__commissionPct * 100
        output += f"Commission percent: {commission:.02f}%\n"
        output += f"Current paycheck: ${self.calcPay():.02f}"
        return output

# Define a subclass of Employee for employees with a single pay.
class SinglePayEmployee(Employee):
    def __init__(self, firstName, lastName, street, city, state, zip, fee):
        # Call the superclass constructor.
        super().__init__(firstName, lastName, street, city, state, zip)
        self.__fee = fee

    # Getter method to retrieve the fee.
    def getFee(self):
        return self.__fee

    # Override the calcPay method to return the single payment fee.
    def calcPay(self):
        return self.__fee

    # Override the __str__ method to format the employee information, including the fee.
    def __str__(self):
        output = super().__str__()  # Call the superclass __str__ method
        output += f"\nFee: ${self.__fee:.02f}\n"
        output += f"Current paycheck: ${self.calcPay():.02f}"
        return output

# Define a subclass of Employee for hourly employees.
class HourlyEmployee(Employee):
    def __init__(self, firstName, lastName, street, city, state, zip, hoursWorked, hourlyPayRate):
        # Call the superclass constructor.
        super().__init__(firstName, lastName, street, city, state, zip)
        self.__hoursWorked = hoursWorked
        self.__hourlyPayRate = hourlyPayRate

    # Getter methods to retrieve hours worked and hourly pay rate.
    def getHoursWorked(self):
        return self.__hoursWorked

    def getHourlyPayRate(self):
        return self.__hourlyPayRate

    # Override the calcPay method to calculate pay based on hours worked and pay rate.
    def calcPay(self):
        return self.__hoursWorked * self.__hourlyPayRate

    # Override the __str__ method to format the employee information, including hourly pay details.
    def __str__(self):
        output = super().__str__()
        output += f"\nHours worked: {self.__hoursWorked}\n"
        output += f"Hourly pay rate: ${self.__hourlyPayRate:.02f}\n"
        output += f"Current paycheck: ${self.calcPay():.02f}"
        return output

# Define a subclass of Employee for salaried employees.
class SalariedEmployee(Employee):
    def __init__(self, firstName, lastName, street, city, state, zip, annualSalary, numPayPeriods):
        # Call the superclass constructor.
        super().__init__(firstName, lastName, street, city, state, zip)
        self.__annualSalary = annualSalary
        self.__numPayPeriods = numPayPeriods

    # Getter methods to retrieve annual salary and number of pay periods.
    def getAnnualSalary(self):
        return self.__annualSalary

    def getNumPayPeriods(self):
        return self.__numPayPeriods

    # Override the calcPay method to calculate pay based on annual salary and pay periods.
    def calcPay(self):
        return self.__annualSalary / self.__numPayPeriods

    # Override the __str__ method to format the employee information, including salary details.
    def __str__(self):
        output = super().__str__()
        output += f"\nAnnual Salary: ${self.__annualSalary:.02f}\n"
        output += f"Number of Pay Periods: {self.__numPayPeriods}\n"
        output += f"Current paycheck: ${self.calcPay():.02f}"
        return output

# Define the main program.
def main():
    
    # Create instances of different types of employees.
    e1 = CommissionEmployee("Carolyn", "England", "123 Easy St.", "Glen Ellyn", "IL", "64321", 100000, 0.1)
    e2 = SinglePayEmployee("Steve", "Santello", "987 Danger Zone", "Buffalo Grove", "IL", "60180", 924.22)
    e3 = HourlyEmployee("John", "Doe", "456 Elm St.", "Chicago", "IL", "60601", 40, 15.0)
    e4 = SalariedEmployee("Jane", "Smith", "789 Oak St.", "Evanston", "IL", "60201", 50000, 26)

    # Create a list of employees.
    employees = [e1, e2, e3, e4]
    
    total_payroll = 0
    
    # Display all employees and calculate total payroll.
    for emp in employees:
        print(emp)
        total_payroll += emp.calcPay()
        print()
    
    # Display the total payroll.
    print(f"Total Payroll: ${total_payroll:.02f}")

# Run the main program
if __name__ == "__main__":
    main()
