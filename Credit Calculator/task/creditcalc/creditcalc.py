import math
import sys
args = sys.argv


def n():
    credit_principal = args[2][12:]
    monthly = args[3][10:]
    credit_int = args[4][11:]
    nom_int = float(credit_int) / (12 * 100)
    x = float(monthly) / (float(monthly) - nom_int * int(credit_principal))
    y = 1 + nom_int
    periods = math.log(x) / math.log(y)
    if round(periods) < periods:
        periods = round(periods) + 1
    else:
        periods = round(periods)
    if periods % 12 == 0:
        print("You need {} years to repay this credit!".format(int(periods / 12)))
    elif periods < 12:
        print("You need {} months to repay this credit!".format(int(periods)))
    else:
        print("You need {} years and {} months to repay this credit!".format(int(periods / 12), round(periods % 12)))
    print('Overpayment = {}'.format(int(monthly) * int(periods)-int(credit_principal)))


def a():
    credit_principal = args[2][12:]
    periods = args[3][10:]
    credit_int = args[4][11:]
    nom_int = float(credit_int) / (12 * 100)
    annuity = int(credit_principal) * ((float(nom_int) * (1 + float(nom_int)) ** int(periods)) / ((1 + float(nom_int)) ** int(periods) - 1))
    if round(annuity) < annuity:
        annuity = round(annuity) + 1
    overpayment = annuity * int(periods) - int(credit_principal)
    print("Your annuity payment = {}!".format(annuity))
    print("Overpayment = {}".format(overpayment))


def p():
    monthly = float(args[2][10:])
    periods = float(args[3][10:])
    credit_int = float(args[4][11:])
    nom_int = credit_int / (12 * 100)
    credit_principal = monthly / ((nom_int * (1 + nom_int) ** periods) / ((1 + nom_int) ** periods - 1))
    print("Your credit principal = {}!".format(int(credit_principal)))
    print('Overpayment = {}'.format(int(monthly * periods - credit_principal)))


def d():
    credit_principal = float(args[2][12:])
    periods = float(args[3][10:])
    credit_int = float(args[4][11:])
    nom_int = float(credit_int) / (12 * 100)
    month = 0
    overpayment = 0
    while month != periods:
        month += 1
        difference = credit_principal / periods + nom_int * (credit_principal - ((credit_principal * (month - 1)) / periods))
        if round(difference) < difference:
            difference = round(difference) + 1
        print('Month {}: paid out {}'.format(month, round(difference)))
        overpayment += difference
        print('''
        Overpayment = {}'''.format(int(overpayment - credit_principal)))


if len(args) != 5:
    print('Incorrect parameters')
else:
    if args[1] == '--type=annuity' and args[2][:12] == '--principal=' and args[3][:10] == '--periods=' and args[4][:11] == '--interest=':
        a()
    elif args[1] == '--type=annuity' and args[2][:10] == '--payment=' and args[3][:10] == '--periods=' and args[4][:11] == '--interest=':
        p()
    elif args[1] == '--type=annuity' and args[2][:12] == '--principal=' and args[3][:10] == '--payment=' and args[4][:11] == '--interest=':
        n()
    elif args[1] == '--type=diff' and args[2][:12] == '--principal=' and args[3][:10] == '--periods=' and args[4][:11] == '--interest=':
        d()
    else:
        print('Incorrect parameters')
