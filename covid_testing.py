def is_valid_sample(sample_quality):
    """Test if the sample quality is acceptable.

    Returns True if the sample quality is high enough for valid test results
    and, False if it is not.
    """
    if sample_quality >= .95:
        return True
    else:
        return False

def is_valid_calibration(calibration_time):
    """Test if the calibration is acceptable.

    Returns True if the calibration time is low enough for valid results, and
    False if it is not.
    """
    if calibration_time < 5:
        return True
    else:
        return False

def test_is_valid_sample():
    """
    Testing is_valid_sample using pytest
    """
    assert is_valid_sample(0.95) == True
    assert is_valid_sample(3.0) == True
    assert is_valid_sample(0.94) == False
    assert is_valid_sample(0.21) == False


def test_is_valid_calibration():
    """
    Testing is_valid_calibration using pytest
    """
    assert is_valid_calibration(2) == True
    assert is_valid_calibration(3) == True
    assert is_valid_calibration(5) == False
    assert is_valid_calibration(15) == False


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
"""
Using the pytest is a great way to verify that certain functions such as the is_valid_sample and is_valid_calibration are working properly. Testing acceptable and unacceptable levels makes sure that my code is able to meet the requirements and detect any errors. Some parts of covid_testing.py that could also be tested is the handling of the demographic information such as race, gender, and income. Making sure that the recording of this data does not cause any incorrect results or other errors is something that is important. Another part of this code that could be tested are the edge cases such as incorrect values for income (ie. non-numeric) and negative sample numbers. Because I used exceptions within the code it will be much easier to make sure the program is deployed to all workstations and that the tests run.
"""
def main():
    total_tests = 0
    positive_tests = 0
    """Some issues regarding this code is that the code does not immediately exit with an error when either the sample quality is greater than .9 or if the time in hours since the last calibration is less than 5. In order to fix this we can use try: statement in order to test for such errors in order to immediately exit with an error using except ValueError and printing an error message.
    """
    while True:
        answer = input("Test positive? [y,n or stop]: ")
        if answer == "stop":
            break

        if answer == "y":
            test_result = True
        else:
            test_result = False
        try:
            q = float(input("Sample quality: "))
        except ValueError:
            print("Invalid Input")
            continue
        if not is_valid_sample(q):
            print("Sample quality must be greater than .9")
            return
        t = int(input("Hours since last calibration: "))
        if not is_valid_calibration(t):
            print("Time since last calibration must be less than 5")
            return

        """One way to adapt the program to collect information about the users race, gender, and income is by implementing user inputs for each. Issues in regarding recording this information is how we can validate such information, another issue is collecting this type of information can result in a multitude of privacy concerns and asking such information will require you to ask in a respectful/inclusive way.
        Now we will record the users race, income and gender:
        """
        race = input("Enter your race: ")
        gender = input("Enter your gender: ")
        income = float(input("Enter your income: "))

        total_tests += 1
        """
        """ 
        if is_valid_sample(q) or is_valid_calibration(t):
            positive_tests += 1

    print()
    print("Total tests: ", total_tests)
    print("Positive: ", positive_tests)
    print("Negative: ", total_tests - positive_tests)
    print("Race: ", race)
    print("Gender: ", gender)
    print("Income: ", income)
main()


