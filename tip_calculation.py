def calculate_tips(price):
    tips = {
        15: price * 0.15,
        18: price * 0.18,
        20: price * 0.20,
        25: price * 0.25
    }
    return tips

def main():
    try:
        price = float(input("Enter the price from Apple Pay: "))
        tips = calculate_tips(price)
        
        print("Tip Calculations:")
        for percent, tip_amount in tips.items():
            print(f"{percent}% tip: ${tip_amount:.2f}")
    except ValueError:
        print("Invalid input. Please enter a valid price.")

if __name__ == "__main__":
    main()
