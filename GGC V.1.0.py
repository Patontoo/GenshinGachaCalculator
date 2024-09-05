import math

def display_signature():
    print("Genshin Gacha Calculator V.1.0")
    print("Developed by Patontoo.")
    print("This script calculates the probability of getting a 5-star item from a banner in Genshin Impact.")
    print("You can choose between a general calculation based on published rates or a personalized calculation based on your own data.")
    print("This calculator uses the known soft pity and hard pity concepts, where character banners have approximately a 6% increase in chance of pulling a 5-star for every wish from 74 to 89, and weapon banners have similar concepts between wishes 63 to 79 (some sources suggest hard pity is at 77 but we use 80 for precision).")
    print('Credits to "Slime Machine" in Hoyolab for the binomial distribution formula shared in the forums and used in this calculator.')
    print()

# Function to calculate binomial probability
def binomial_probability(n, x, P):
    nCx = math.comb(n, x)  # Binomial coefficient
    return nCx * (P**x) * ((1 - P)**(n - x))

# Function to calculate the probability of getting at least one 5-star item
def adjust_probability(current_pity, future_wishes, base_probability, banner_type):
    # Define pity thresholds based on banner type
    if banner_type == "character":
        soft_pity = 74
        hard_pity = 90
        increment_per_wish = 0.06  # 6% increase per wish
    elif banner_type == "weapon":
        soft_pity = 63
        hard_pity = 80
        increment_per_wish = 0.06  # Example: 6% increase per wish
    else:
        raise ValueError("Invalid banner type")

    # Check if future wishes will reach hard pity
    if current_pity + future_wishes >= hard_pity:
        return 1.0  # 100% probability of getting at least one 5-star
    
    # Determine probability at the current pity
    if current_pity < soft_pity:
        probability_at_pity = base_probability
    elif soft_pity <= current_pity < hard_pity:
        probability_at_pity = min(base_probability + increment_per_wish * (current_pity - soft_pity), 1.0)
    else:
        probability_at_pity = 1.0

    # Cap probability at 100% if reaching hard pity
    if current_pity + future_wishes >= hard_pity:
        probability_at_pity = 1.0

    # Calculate the probability of not getting a 5-star in the future wishes
    probability_not_getting_5_star = binomial_probability(future_wishes, 0, probability_at_pity)
    
    # Total probability is 1 minus the probability of not getting any 5-star item
    return 1 - probability_not_getting_5_star

# Main function to calculate probability with inputs
def calculate_probability():
    display_signature()  # Display signature
    
    # Choose calculation type
    calc_type = input("Choose calculation type: (1) General based on published rates or (2) Personalized based on your data: ")
    
    if calc_type == "1":
        # General calculation
        banner_type = input("Enter banner type: (1) Character or (2) Weapon: ")
        if banner_type == "1":
            base_probability = 0.006  # Base probability of 0.6% for characters
            banner_type = "character"
        elif banner_type == "2":
            base_probability = 0.006  # Adjust as needed for weapons
            banner_type = "weapon"
        else:
            print("Invalid choice. Exiting.")
            return
        print("Using general rates based on published gacha system data.")
    elif calc_type == "2":
        # Personalized calculation
        five_stars = int(input("How many 5-star items have you obtained in recent wishes? "))
        total_wishes = int(input("How many wishes have you performed in total? "))
        base_probability = five_stars / total_wishes  # Adjusted probability based on previous wishes
        banner_type = input("Enter banner type: (1) Character or (2) Weapon: ")
        if banner_type == "1":
            banner_type = "character"
        elif banner_type == "2":
            banner_type = "weapon"
        else:
            print("Invalid choice. Exiting.")
            return
    else:
        print("Invalid choice. Exiting.")
        return

    # Input current pity and number of future wishes
    current_pity = int(input("Enter your current pity: "))
    future_wishes = int(input("Enter the number of future wishes: "))
    
    # Adjust probability according to current pity, future wishes, and banner type
    adjusted_probability = adjust_probability(current_pity, future_wishes, base_probability, banner_type)
    
    # Show the result
    print(f"The probability of getting at least one 5-star in {future_wishes} wishes is approximately {adjusted_probability * 100:.2f}%")

    # Pause to view the result
    input("Press Enter to exit...")

# Run the main function
calculate_probability()
