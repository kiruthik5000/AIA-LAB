from textblob import TextBlob 
print("Welcome all to This Sentiment Analysis Page ") 
print("No matter what the lines number, all matters is the polarity!!") 
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