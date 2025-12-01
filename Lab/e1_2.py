from textblob import TextBlob 
user_input = input("Enter the desired passage : ") 

analysis = TextBlob(user_input) 

polarity = analysis.sentiment.polarity 

# only 2 line change
subjectivity = analysis.sentiment.subjectivity

if(polarity>0): 
    sentiment="Positive" 
elif(polarity<0): 
    sentiment="negative" 
else: 
    sentiment="Neutral" 
    
print(f"The final results are here!") 
print(f"The polarity of passage is : {polarity}") 

# this line also
print(f"The subjectivity of the passage is :{subjectivity}")

print(f"The Sentiment is :{sentiment}")