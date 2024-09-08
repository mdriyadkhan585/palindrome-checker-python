import re

def is_palindrome(s):
    """Check if the given string is a palindrome."""
    cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return cleaned_str == cleaned_str[::-1]

def format_text(text, title=False):
    """Format text for better readability."""
    if title:
        return f"\n{'='*30}\n{text}\n{'='*30}\n"
    return text

def main():
    print(format_text("Palindrome Checker Program", title=True))
    
    while True:
        # Read input from user
        user_input = input("Enter a string: ").strip()

        # Handle multi-line input
        while user_input.endswith('\\'):
            user_input = user_input.rstrip('\\') + '\n' + input("Continue entering string: ").strip()
        
        # Check if the input string is empty
        if not user_input:
            print("⚠️ You entered an empty string. Please enter a valid string.")
            continue

        # Check if the string is a palindrome
        if is_palindrome(user_input):
            print("✅ The input string is a palindrome.")
        else:
            print("❌ The input string is not a palindrome.")

        # Ask the user if they want to continue
        choice = input("Do you want to check another string? (y/n): ").strip().lower()
        if choice != 'y':
            print(format_text("Thank you for using the Palindrome Checker!", title=True))
            break

if __name__ == "__main__":
    main()
