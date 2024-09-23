# Function to check years in service and office
def check_employee_service():
    # Input: Employee's years in service and office
    years_in_service = int(input("Enter years in service: "))
    office = input("Enter office (IT, ACCT, HR): ").upper()

    # Define bonus amounts based on office and years in service
    bonuses = {
        "IT": { ">=10": 10000, "<10": 5000 },
        "ACCT": { ">=10": 12000, "<10": 6000 },
        "HR": { ">=10": 15000, "<10": 7500 }
    }

    # Determine the bonus based on the input
    if office in bonuses:
        if years_in_service >= 10:
            bonus = bonuses[office][">=10"]
        else:
            bonus = bonuses[office]["<10"]
        print(f"Hi, your bonus is: {bonus}")
    else:
        print("Invalid office. Please enter IT, ACCT, or HR.")

# Call the function
check_employee_service()
