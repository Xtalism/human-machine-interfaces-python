try:
    worked_hours = float(input('How many hours did you work?: '))
    pay_per_hour = float(input('Enter your pay per hour: '))
    extra_hours = 15
    limit_hours = 55

    def calculate_pay(hours, payment):
        if hours <= 40:
            pay = hours * payment
            print(f'Total worked extra hours: 0')
        elif hours > 40 and hours <= limit_hours:
            pay = (40 * payment) + ((hours - 40) * 2 * payment)
            print(f'Total worked extra hours: {hours - 40}')
        elif hours > limit_hours:
            pay = (40 * payment) + (extra_hours * 2 * payment) + ((hours - limit_hours) * 3 * payment) + (0.15 * hours * payment)
            print(f'Total worked extra hours: {worked_hours - limit_hours}')
        print(f'Subtotal pay: {pay}')
        return pay

    def income_tax():
        pay = calculate_pay(worked_hours, pay_per_hour)
        if pay <= 8000:
            isr = 0
        elif pay > 8000 and pay <= 13500:
            isr = pay * 0.1
        elif pay > 13500 and pay <= 25000:
            isr = pay * 0.19
        elif pay > 25000:
            isr = pay * 0.22
        total_pay = pay - isr
        print(f'The income tax is: {isr}')
        print(f'Your total pay is: {total_pay}')
        return isr, total_pay
        
    print(f'\nWorked hours: {worked_hours}')
    print(f'Pay per hour: {pay_per_hour}')
    income_tax()

except ValueError:
    print('You must enter a float number!')