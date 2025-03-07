def compute_salary_deductions(gross_salary):
    SSS_CONTRIBUTION = 1200
    PHILHEALTH_RATE = 0.05
    PAGIBIG_CONTRIBUTION = 100
    FIXED_TAX = 1875  # Assuming fixed value for simplicity

    philhealth_deduction = (gross_salary * PHILHEALTH_RATE) / 2
    total_deductions = SSS_CONTRIBUTION + philhealth_deduction + PAGIBIG_CONTRIBUTION + FIXED_TAX
    net_salary = gross_salary - total_deductions

    print("Gross Salary:", gross_salary)
    print("SSS Deduction:", SSS_CONTRIBUTION)
    print("PhilHealth Deduction:", philhealth_deduction)
    print("Pag-IBIG Deduction:", PAGIBIG_CONTRIBUTION)
    print("Tax Deduction:", FIXED_TAX)
    print("Total Deductions:", total_deductions)
    print("Net Salary:", net_salary)


def main():
    monthly_salary = float(input("Enter your monthly salary: "))
    compute_salary_deductions(monthly_salary)


if __name__ == "__main__":
    main()
