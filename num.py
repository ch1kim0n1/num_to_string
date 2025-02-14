def number_to_words(n):
    if n == 0:
        return "zero"
    elif n < 0:
        return "minus " + number_to_words(-n)
    
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
            "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    def helper(num):
        if num < 20:
            return ones[num]
        elif num < 100:
            return tens[num // 10] + (" " + ones[num % 10] if num % 10 != 0 else "")
        elif num < 1000:
            return ones[num // 100] + " hundred" + (" " + helper(num % 100) if num % 100 != 0 else "")
        elif num < 1000000:
            return helper(num // 1000) + " thousand" + (" " + helper(num % 1000) if num % 1000 != 0 else "")
        elif num < 1000000000:
            return helper(num // 1000000) + " million" + (" " + helper(num % 1000000) if num % 1000000 != 0 else "")
        else:
            return helper(num // 1000000000) + " billion" + (" " + helper(num % 1000000000) if num % 1000000000 != 0 else "")
    
    return helper(n)

if __name__ == "__main__":
    user_input = input("Enter an integer: ")
    try:
        num = int(user_input)
        print(number_to_words(num))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
