from textblob import TextBlob 
user_input = input("Enter the desired passage : ") 

analysis = TextBlob(user_input) 

polarity = analysis.sentiment.polarity 

if(polarity>0): 
    sentiment="Positive" 
elif(polarity<0): 
    sentiment="negative" 
else: 
    sentiment="Neutral" 
    
print(f"The final results are here!") 
print(f"The polarity of passage is : {polarity}") 
print(f"The Sentiment is :{sentiment}")