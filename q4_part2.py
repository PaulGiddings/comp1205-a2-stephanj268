# Name: Stephan Jones
# Student ID: 500004652
# Date: 25th October 2026
# Question: Q4 CHOGM Credential Checker - Part 2
# Collaborators: <names, or 'none'>
# Tools used: <AI tools / websites used, or 'none' - also record them in AI_LOG.md>

"""Validate the format and checksum of a CHOGM delegate credential code."""

CODE_LENGTH = 10
FIRST_LETTER_WEIGHT = 7
SECOND_LETTER_WEIGHT = 6
FIRST_DIGIT_WEIGHT = 5
CHECK_MODULUS = 11
TEN_SYMBOL = "X"


def is_letter(ch: str) -> bool:
    """Return True if ch is exactly one uppercase letter from A to Z."""

    if ch >= "A" and ch <= "Z":
        return True
    return False


def is_digit(ch: str) -> bool:
    """Return True if ch is exactly one of the characters 0 to 9."""

    if ch >= "0" and ch <= "9":
        return True
    return False


def normalise_credential(raw: str) -> str:
    """Return raw with leading/trailing whitespace removed, in upper case."""

    return raw.strip().upper()


def is_valid_format(code: str) -> bool:
    """Return True if a normalised code has the shape LL-DDDDD-C."""

    if len(code) != CODE_LENGTH:
        return False

    if not is_letter(code[0]) or not is_letter(code[1]):
        return False

    if code[2] != "-":
        return False

    for i in range(3, 8):
        if not is_digit(code[i]):
            return False

    if code[8] != "-":
        return False

    if not is_digit(code[9]) and code[9] != TEN_SYMBOL:
        return False

    return True


def letter_value(ch: str) -> int:
    """Return the position of an uppercase letter in the alphabet (A=1 ... Z=26)."""

    return ord(ch) - ord("A") + 1


def expected_check_char(code: str) -> str:
    """Return the check character that a correctly formatted code should end with."""

    total = 0

    total += letter_value(code[0]) * FIRST_LETTER_WEIGHT
    total += letter_value(code[1]) * SECOND_LETTER_WEIGHT

    for i in range(3, 8):
        total += int(code[i]) * FIRST_DIGIT_WEIGHT

    remainder = total % CHECK_MODULUS

    if remainder == 0:
        return "0"
    elif CHECK_MODULUS - remainder == 10:
        return TEN_SYMBOL
    else:
        return str(CHECK_MODULUS - remainder)


def checksum_ok(code: str) -> bool:
    """Return True if a correctly formatted code ends with its expected check character."""

    return code[9] == expected_check_char(code)


def main() -> None:
    """Read a credential code and print its format and checksum result."""

    P = "PASS"
    F = "FAIL"

    credential_code = input("Enter credential code: ")
    credential_code = normalise_credential(credential_code)

    print(f"Credential: {credential_code}")

    if is_valid_format(credential_code):
        print("OK")

        if checksum_ok(credential_code):
            print(f"Checksum: {P}")
        else:
            print(f"Checksum: {F}")

    else:
        print("Bad")
        print(f"Checksum: {F}")


if __name__ == "__main__":
    main()
