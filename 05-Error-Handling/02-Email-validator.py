class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


command = input()

valid_domains = [".com", ".bg", ".org", ".net"]


def is_domain_valid(domain, valid_domains):
    result = False
    for x in valid_domains:
        if domain.endswith(x):
            result = True
            break
    return result


while command != "End":
    if "@" not in command:
        raise MustContainAtSymbolError("Email must contain @")

    username, domain = command.split('@')
    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if not is_domain_valid(domain, valid_domains):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    command = input()

    print("Email is valid")
