from argparse import ArgumentParser
import sys

def calculate_tuition(credits, resident, dt):
    """ Calculates tuition and mandatory fees for one semester at UMD.

    Takes into consideration the number of credits the student is taking,
    whether they are a resident of Maryland, and whether they pay
    differential tuition.

    Args:
        credits (integer): the number of credits the student is taking
            (default: 12).
        resident (boolean): whether the student is considered a
            Maryland state resident for tuition purposes (default: True).
        dt (boolean): whether or not the student pays
            differential tuition (default: False).

    Raises:
        ValueError: credits must be non-negative.

    Returns:
        float: the student's combined tuition and mandatory fees.
    """
    if credits < 0:
        raise ValueError("Credits must be non-negative.")
    
    if credits == 0:
        return 0.0
    elif credits >= 12:
        tuition = 4412.0 if resident else 17468.0
    else:
        tuition = credits * (367.0 if resident else 1456.0)
    
    if dt:
        tuition += 1428.0 if credits >= 12 else credits * 118.0
    
    if credits >= 9:
        flat_fee = 977.5
    else: 
        flat_fee = 455.0
    
    return tuition + flat_fee

def parse_args(arglist):
    """ Parses command-line arguments.

    The following optional command-line arguments are defined:

    -c / --credits: the number of credits the student is taking
        (type: int, default: 12)
    -nr / --nonresident: indicates the student is not a Maryland
        resident (action: 'store_true')
    -dt / --differentialtuition: indicates the student pays differential
        tuition (action: 'store_true')

    Args:
        arglist (list of str): a list of command-line arguments.

    Returns:
        namespace: a namespace with variables credits, nonresident, and
        differentialtuition.
    """
    parser = ArgumentParser(description = "Calculate tuition and fees for UMD")
    parser.add_argument("-c", "--credits", type = int, default = 12, help  = "Number of credits a student is taking.")
    parser.add_argument("-r", "--resident", type = "store-true", help = "The student is a resident at UMD.")
    parser.add_argument("-dt", "--differentialtuition", type = "store_false", help = "Indicates if the student pays differential tuition")

if __name__ =="__main__":
    args = parse_args(sys.argv[1:])
    try:
        total = calculate_tuition(args.credits, args.resident, args.differentialtuition)
        print(f"Your tuition and fees total ${total}.")
    except ValueError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    
