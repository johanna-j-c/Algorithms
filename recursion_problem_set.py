def reverse(text):
    if not text:
        return ""

    print(text)
    
    return text[-1] + reverse(text[0:-1])

print(reverse("cat"))