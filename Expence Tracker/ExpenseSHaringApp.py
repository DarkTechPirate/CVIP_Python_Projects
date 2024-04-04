class ExpenseSharingApp:
    def __init__(self):
        self.roommates = []

    def get_roommates(self):
        num = int(input("Enter number of roommates: "))
        for i in range(1, num + 1):
            self.roommates.append(input(f"Enter roommate - {i} Name: ").capitalize())

    @staticmethod
    def show_expenses(lst, amount):
        print("\nSplitted Amount Bill")
        for roommate in lst:
            print(f"{roommate}: ₹ {amount}")

    def split_bills(self, total_amount):
        if total_amount <= 0:
            exit("Amount Can't be Negative")

        amount_per_person = total_amount / len(self.roommates)
        amount_per_person = round(amount_per_person, 2)

        self.show_expenses(self.roommates, amount_per_person)

    @staticmethod
    def show_paid_and_not_paid(paid_list, roommates):
        print("\nList of Paid and Not Paid Persons")
        for name in roommates:
            status = "Paid" if name in paid_list else "Not Paid"
            print(f"{name}: {status}")

    def track_payments(self):
        paid_list = []

        while True:
            paid_name = input("\nPress 0 to Exit or Enter your name if you paid: ").capitalize()

            if paid_name == '0':
                break

            if paid_name not in self.roommates:
                print("Invalid User Name!!!")
            else:
                paid_list.append(paid_name)

            if sorted(self.roommates) == sorted(paid_list):
                break

        self.show_paid_and_not_paid(paid_list, self.roommates)


if __name__ == "__main__":
    print("\n\t\t\t\t\t Expense Tracker App\n")

    app = ExpenseSharingApp()

    app.get_roommates()

    total_amount = float(input("\nEnter Total Bill Amount: "))
    app.split_bills(total_amount)

    app.track_payments()
