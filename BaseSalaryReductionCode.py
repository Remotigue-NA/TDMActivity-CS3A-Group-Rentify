class SalaryComputation:
    PHILHEALTH_RATE = 0.05
    FIXED_TAX = 1875
    SSS_CONTRIBUTION = 1200
    PAGIBIG_CONTRIBUTION = 100

    def __init__(self, gross_salary):
        self.gross_salary = gross_salary
        self.sss_deduction = self.compute_sss_contribution()
        self.philhealth_deduction = self.compute_philhealth_deduction()
        self.pagibig_deduction = self.compute_pagibig_contribution()
        self.tax_deduction = self.compute_fixed_tax()
        self.total_deductions = self.compute_total_deductions()
        self.net_salary = self.compute_net_salary()

    def compute_sss_contribution(self):
        return self.SSS_CONTRIBUTION

    def compute_philhealth_deduction(self):
        return (self.gross_salary * self.PHILHEALTH_RATE) / 2

    def compute_pagibig_contribution(self):
        return self.PAGIBIG_CONTRIBUTION

    def compute_fixed_tax(self):
        return self.FIXED_TAX

    def compute_total_deductions(self):
        return (self.sss_deduction + self.philhealth_deduction +
                self.pagibig_deduction + self.tax_deduction)

    def compute_net_salary(self):
        return self.gross_salary - self.total_deductions

    def display_salary_details(self):
        print("Gross Salary:", self.gross_salary)
        print("SSS Deduction:", self.sss_deduction)
        print("PhilHealth Deduction:", self.philhealth_deduction)
        print("Pag-IBIG Deduction:", self.pagibig_deduction)
        print("Tax Deduction:", self.tax_deduction)
        print("Total Deductions:", self.total_deductions)
        print("Net Salary:", self.net_salary)


def main():
    monthly_salary = float(input("Enter your monthly salary: "))
    salary = SalaryComputation(monthly_salary)
    salary.display_salary_details()


if __name__ == "__main__":
    main()
