#store the data into dictionary
language = {'JavaScript':62.3,'HTML':52.9,'Python': 51, 'SQL':51, 'TypeScript': 38.5}
print("(1) Dictionary:", language) #output the dictionary

#draw the bar graph
import matplotlib.pyplot as plt
plt.bar(language.keys(),language.values()) #setting x and y
plt.xlabel('programming language')
plt.ylabel('percentage of developers') #setting the labels
plt.title('programming language popularity') #setting the title of the graph
plt.show() #show the bar graph

#output one percentage of programming language
input_language = 'Python' #let's say the input language is Python
if input_language in language:
    print(f"The Percentage of developers using {input_language}: {language[input_language]}%")
else:
    print(f"{input_language} not found in the data. Available languages are: {list(language.keys())}")
