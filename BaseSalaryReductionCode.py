class SalaryComputation:
    PHILHEALTH_RATE = 0.05
    FIXED_TAX = 1875
    SSS_CONTRIBUTION = 1200
    PAGIBIG_CONTRIBUTION = 100

    def __init__(self, gross_salary):
        if not isinstance(gross_salary, (int, float)) or gross_salary <= 0:
            raise ValueError("Gross salary must be a positive number.")

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
        print("\nSalary Breakdown:")
        print(f"Gross Salary: {self.gross_salary:.2f}")
        print(f"SSS Deduction: {self.sss_deduction:.2f}")
        print(f"PhilHealth Deduction: {self.philhealth_deduction:.2f}")
        print(f"Pag-IBIG Deduction: {self.pagibig_deduction:.2f}")
        print(f"Tax Deduction: {self.tax_deduction:.2f}")
        print(f"Total Deductions: {self.total_deductions:.2f}")
        print(f"Net Salary: {self.net_salary:.2f}")


def main():
    while True:
        try:
            monthly_salary = float(input("Enter your monthly salary: "))
            if monthly_salary <= 0:
                print("Error: Salary must be a positive number. Please try again.")
                continue

            salary = SalaryComputation(monthly_salary)
            salary.display_salary_details()
            break

        except ValueError:
            print("Invalid input! Please enter a valid numeric salary.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break


if __name__ == "__main__":
    main()

