def compute_sss_contribution():
    return 1200

def compute_philhealth_deduction(gross_salary):
    PHILHEALTH_RATE = 0.05
    return (gross_salary * PHILHEALTH_RATE) / 2

def compute_pagibig_contribution():
    return 100

def compute_fixed_tax():
    return 1875  # Assuming fixed value for simplicity

def compute_total_deductions(gross_salary):
    sss_deduction = compute_sss_contribution()
    philhealth_deduction = compute_philhealth_deduction(gross_salary)
    pagibig_deduction = compute_pagibig_contribution()
    tax_deduction = compute_fixed_tax()
    
    total_deductions = sss_deduction + philhealth_deduction + pagibig_deduction + tax_deduction
    return total_deductions, sss_deduction, philhealth_deduction, pagibig_deduction, tax_deduction

def compute_net_salary(gross_salary):
    total_deductions, sss, philhealth, pagibig, tax = compute_total_deductions(gross_salary)
    net_salary = gross_salary - total_deductions
    return net_salary, total_deductions, sss, philhealth, pagibig, tax

def display_salary_details(gross_salary):
    net_salary, total_deductions, sss, philhealth, pagibig, tax = compute_net_salary(gross_salary)
    
    print("Gross Salary:", gross_salary)
    print("SSS Deduction:", sss)
    print("PhilHealth Deduction:", philhealth)
    print("Pag-IBIG Deduction:", pagibig)
    print("Tax Deduction:", tax)
    print("Total Deductions:", total_deductions)
    print("Net Salary:", net_salary)

def main():
    monthly_salary = float(input("Enter your monthly salary: "))
    display_salary_details(monthly_salary)

if __name__ == "__main__":
    main()
