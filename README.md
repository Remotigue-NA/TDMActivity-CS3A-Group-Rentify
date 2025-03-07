# TDMActivity-CS3A-Group-Rentify
### **Salary Calculator**  

#### **Overview**  
This Python program determines salary deductions, including SSS, PhilHealth, Pag-IBIG, and tax. It calculates the net salary by subtracting the total deductions from the gross salary.  

#### **Features**  
- Computes salary deductions (SSS, PhilHealth, Pag-IBIG, Tax)  
- Displays a structured salary breakdown  
- Utilizes modular functions for easier maintenance  
- Implements an Object-Oriented Programming (OOP) approach for better organization  
- Includes input validation and error handling  
- Provides an automated test script  

#### **Commit History & Updates**  

1. **Initial Implementation** *(Base Code)*  
   - Basic salary deduction calculations  
   - Hardcoded values for deductions (SSS, PhilHealth, Pag-IBIG, Tax)  
   - Directly prints the salary breakdown  
   - Lacks input validation and error handling  

2. **Enhanced Code Readability** *(REMOTIGUE)*  
   - Replaced hardcoded values with descriptive constants  
   - Improved function naming for clarity  
   - Used a dictionary to return salary details instead of direct printing  
   - Introduced `display_salary_details()` for structured output  
   - Added basic input validation  

3. **Refactored into Modular Functions** *(FABELA)*  
   - Separated deductions into individual functions:  
     - `calculate_sss_deduction()`  
     - `calculate_philhealth_deduction()`  
     - `calculate_pagibig_deduction()`  
     - `calculate_tax_deduction()`  
   - Introduced `calculate_total_deductions()` and `calculate_net_salary()` for better structure  
   - Improved maintainability by reducing code redundancy  
   - Simplified calculations using modular functions  

4. **Implemented Object-Oriented Programming (OOP) Structure** *(MIRAFUENTES)*  
   - Converted the program into a class-based design (`SalaryCalculator`)  
   - Encapsulated attributes and methods for better organization  
   - Enhanced scalability and flexibility for future enhancements  

5. **Added Input Validation, Error Handling, & Testing** *(VALLECERA)*  
   - Implemented error handling for invalid and negative salary inputs  
   - Created `get_valid_salary()` to manage incorrect inputs  
   - Ensured `SalaryCalculator` raises errors for non-numeric and negative values  
   - Developed a test script (`test_salary_calculator.py`) to verify calculations  
   - Used `unittest` to validate all functions' correctness