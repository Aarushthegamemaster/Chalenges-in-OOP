class IntegerToRoman:
    _roman_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    @classmethod
    def convert(cls, number: int) -> str:
        if not isinstance(number, int):
            raise ValueError("Input must be an integer.")
        if number < 1 or number > 3999:
            raise ValueError("Number must be between 1 and 3999.")

        roman_numeral = ""
        for value, symbol in cls._roman_map:
            while number >= value:
                roman_numeral += symbol
                number -= value
        return roman_numeral

if __name__ == "__main__":
    try:
        user_input = input("Enter an integer (1-3999): ").strip()
        if not user_input.isdigit():
            raise ValueError("Invalid input. Please enter a positive integer.")
        
        number = int(user_input)
        roman = IntegerToRoman.convert(number)
        print(f"Roman numeral: {roman}")

    except ValueError as e:
        print(f"Error: {e}")
