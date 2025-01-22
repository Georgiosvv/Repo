from directory.UpperString import UpperString
from directory.LowerString import LowerString
if __name__ == "__main__":
    text = input("give text")
    upper_string = UpperString()
    upper_string.get_String(text)
    upper_string.print_String()
    lower_string = LowerString()
    lower_string.get_String(text)
    lower_string.print_String()