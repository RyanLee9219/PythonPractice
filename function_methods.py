#built-in functions + methods

#len -> lenght of string
greet = 'hellloooo'
print(greet[0:len(greet)])

#upper -> toUppercase
quote = 'to be or not to be'
print(quote.upper())

#capitalize -> capitalize first letter
print(quote.capitalize())

#lower -> lowercase
print(quote.lower())

#find -> finds the first occurence of a piece of text
print(quote.find('be'))

#replace -> replaces a piece of text
print(quote.replace('be', 'me'))

print(quote) #Strings are not immutable
