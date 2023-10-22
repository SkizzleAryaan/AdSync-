import array as arr
from flask import Flask 
import openai 
import math

openai.api_key = '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'

#global variables

totalbudget = 1000 
listofads = []

class Ads: 
    def  __init__(self, company, number, budget, reach, ctr, cpa, cpm, conv):
        self.company = company
        self.number = number
        self.reach = reach # value
        self.ctr = ctr #percent 
        self.cpa = cpa # value 
        self.conv = conv # percent
        self.budget = budget
        self.cpm = cpm # percent
        self.score = 0

    def changerecalgo(self): 
        return self.recalgo


    def changerecapi(self): 
        return self.recapi 
    
    def updateInfo(self, nbudget, nreach, nctr, ncpa, ncpm, nconv):
        self.reach = nreach
        self.budget = nbudget 
        self.ctr = nctr
        self.cpa = ncpa
        self.cpm = ncpm
        self.conv = nconv 

    def removead(adslist, index): 
        adslist.pop(index)
    
    def addad(adslist, adin, index): 
        adslist.insert(index, adin)


def sort_ads_by_score(ad_list):
    return sorted(ad_list, key=lambda ad: ad.score)
  

def RecommendationAlgo(adslist): 
    for i in range(len(adslist)): 
       if (adslist[i].company == "Facebook"): 
            if (adslist[i].conv >= 10): 
                adslist[i].score += 5
            elif (adslist[i].conv >= 5): 
                adslist[i].score += 3
            elif (adslist[i].conv >= 2):
                adslist[i].score += 1
            elif (adslist[i].conv >= 1):
                adslist[i].score += 0
            elif (adslist[i].conv >= 0.5):
                adslist[i].score += -2
            else: 
                adslist[i].score += -4 

            if (adslist[i].ctr >= 7): 
                adslist[i].score += 3
            elif (adslist[i].ctr >= 4): 
                adslist[i].score += 2
            elif (adslist[i].ctr >= 2):
                adslist[i].score += 1
            elif (adslist[i].ctr >= 1):
                adslist[i].score += 0
            elif (adslist[i].ctr >= 0.5):
                adslist[i].score += -2
            else: 
                adslist[i].score += -3

            if (adslist[i].cpa <= 10): 
                adslist[i].score += 3
            elif (adslist[i].cpa <= 15): 
                adslist[i].score += 2
            elif (adslist[i].cpa <= 19):
                adslist[i].score += 1
            elif (adslist[i].cpa <= 25):
                adslist[i].score += 0
            elif (adslist[i].cpa <= 28):
                adslist[i].score += -2
            else: 
                adslist[i].score += -3

            if (adslist[i].cpm <= 3): 
                adslist[i].score += 3
            elif (adslist[i].cpm <= 7): 
                adslist[i].score += 2
            elif (adslist[i].cpm <= 15):
                adslist[i].score += 1
            elif (adslist[i].cpm <= 25):
                adslist[i].score += 0
            elif (adslist[i].cpm <= 30):
                adslist[i].score += -2
            else: 
                adslist[i].score += -3

            if (adslist[i].reach >= 50000): 
                adslist[i].score += 3
            elif (adslist[i].reach >= 10000): 
                adslist[i].score += 2
            elif (adslist[i].reach >= 5000):
                adslist[i].score += 1
            elif (adslist[i].reach >= 2000):
                adslist[i].score += 0
            elif (adslist[i].reach >= 1000):
                adslist[i].score += -2
            else: 
                adslist[i].score += -3
       elif (adslist[i].company == "Tiktok"): 
            if (adslist[i].conv >= 8): 
                adslist[i].score += 5
            elif (adslist[i].conv >= 4): 
                adslist[i].score += 3
            elif (adslist[i].conv >= 2):
                adslist[i].score += 1
            elif (adslist[i].conv >= 1):
                adslist[i].score += 0
            elif (adslist[i].conv >= 0.5):
                adslist[i].score += -2
            else: 
                adslist[i].score += -4 

            if (adslist[i].ctr >= 6): 
                adslist[i].score += 3
            elif (adslist[i].ctr >= 4): 
                adslist[i].score += 2
            elif (adslist[i].ctr >= 2):
                adslist[i].score += 1
            elif (adslist[i].ctr >= 1):
                adslist[i].score += 0
            elif (adslist[i].ctr >= 0.5):
                adslist[i].score += -2
            else: 
                adslist[i].score += -3

            if (adslist[i].cpa <= 40): 
                adslist[i].score += 3
            elif (adslist[i].cpa <= 80): 
                adslist[i].score += 2
            elif (adslist[i].cpa <= 150):
                adslist[i].score += 1
            elif (adslist[i].cpa <= 200):
                adslist[i].score += 0
            elif (adslist[i].cpa <= 250):
                adslist[i].score += -2
            else: 
                adslist[i].score += -3

            if (adslist[i].cpm <= 2): 
                adslist[i].score += 3
            elif (adslist[i].cpm <= 5): 
                adslist[i].score += 2
            elif (adslist[i].cpm <= 10):
                adslist[i].score += 1
            elif (adslist[i].cpm <= 15):
                adslist[i].score += 0
            elif (adslist[i].cpm <= 20):
                adslist[i].score += -2
            else: 
                adslist[i].score += -3

            if (adslist[i].reach >= 30000): 
                adslist[i].score += 3
            elif (adslist[i].reach >= 5000): 
                adslist[i].score += 2
            elif (adslist[i].reach >= 2000):
                adslist[i].score += 1
            elif (adslist[i].reach >= 1000):
                adslist[i].score += 0
            elif (adslist[i].reach >= 500):
                adslist[i].score += -2
            else: 
                adslist[i].score += -3    
       elif (adslist[i].company == "Instagram"): 
            if (adslist[i].conv >= 7): 
                adslist[i].score += 5
            elif (adslist[i].conv >= 3): 
                adslist[i].score += 3
            elif (adslist[i].conv >= 1.5):
                adslist[i].score += 1
            elif (adslist[i].conv >= 1):
                adslist[i].score += 0
            elif (adslist[i].conv >= 0.5):
                adslist[i].score += -2
            else: 
                adslist[i].score += -4 

            if (adslist[i].ctr >= 6): 
                adslist[i].score += 3
            elif (adslist[i].ctr >= 4): 
                adslist[i].score += 2
            elif (adslist[i].ctr >= 2):
                adslist[i].score += 1
            elif (adslist[i].ctr >= 1):
                adslist[i].score += 0
            elif (adslist[i].ctr >= 0.5):
                adslist[i].score += -2
            else: 
                adslist[i].score += -3

            if (adslist[i].cpa <= 35): 
                adslist[i].score += 3
            elif (adslist[i].cpa <= 70): 
                adslist[i].score += 2
            elif (adslist[i].cpa <= 130):
                adslist[i].score += 1
            elif (adslist[i].cpa <= 150):
                adslist[i].score += 0
            elif (adslist[i].cpa <= 175):
                adslist[i].score += -2
            else: 
                adslist[i].score += -3

            if (adslist[i].cpm <= 3): 
                adslist[i].score += 3
            elif (adslist[i].cpm <= 7): 
                adslist[i].score += 2
            elif (adslist[i].cpm <= 15):
                adslist[i].score += 1
            elif (adslist[i].cpm <= 20):
                adslist[i].score += 0
            elif (adslist[i].cpm <= 30):
                adslist[i].score += -2
            else: 
                adslist[i].score += -3

            if (adslist[i].reach >= 20000): 
                adslist[i].score += 3
            elif (adslist[i].reach >= 7000): 
                adslist[i].score += 2
            elif (adslist[i].reach >= 2000):
                adslist[i].score += 1
            elif (adslist[i].reach >= 1000):
                adslist[i].score += 0
            elif (adslist[i].reach >= 500):
                adslist[i].score += -2
            else: 
                adslist[i].score += -3
       elif (adslist[i].company == "Google"): 
            if (adslist[i].conv >= 8): 
                adslist[i].score += 5
            elif (adslist[i].conv >= 5): 
                adslist[i].score += 3
            elif (adslist[i].conv >= 2):
                adslist[i].score += 1
            elif (adslist[i].conv >= 1):
                adslist[i].score += 0
            elif (adslist[i].conv >= 0.5):
                adslist[i].score += -2
            else: 
                adslist[i].score += -4 

            if (adslist[i].ctr >= 10): 
                adslist[i].score += 3
            elif (adslist[i].ctr >= 7): 
                adslist[i].score += 2
            elif (adslist[i].ctr >= 5):
                adslist[i].score += 1
            elif (adslist[i].ctr >= 3):
                adslist[i].score += 0
            elif (adslist[i].ctr >= 1.5):
                adslist[i].score += -2
            else: 
                adslist[i].score += -3

            if (adslist[i].cpa <= 35): 
                adslist[i].score += 3
            elif (adslist[i].cpa <= 40): 
                adslist[i].score += 2
            elif (adslist[i].cpa <= 50):
                adslist[i].score += 1
            elif (adslist[i].cpa <= 70):
                adslist[i].score += 0
            elif (adslist[i].cpa <= 90):
                adslist[i].score += -2
            else: 
                adslist[i].score += -3

            if (adslist[i].cpm <= 2): 
                adslist[i].score += 3
            elif (adslist[i].cpm <= 5): 
                adslist[i].score += 2
            elif (adslist[i].cpm <= 10):
                adslist[i].score += 1
            elif (adslist[i].cpm <= 15):
                adslist[i].score += 0
            elif (adslist[i].cpm <= 20):
                adslist[i].score += -2
            else: 
                adslist[i].score += -3

            if (adslist[i].reach >= 50000): 
                adslist[i].score += 3
            elif (adslist[i].reach >= 10000): 
                adslist[i].score += 2
            elif (adslist[i].reach >= 5000):
                adslist[i].score += 1
            elif (adslist[i].reach >= 3000):
                adslist[i].score += 0
            elif (adslist[i].reach >= 2000):
                adslist[i].score += -2
            else: 
                adslist[i].score += -3              

    ranked = sort_ads_by_score(adslist)
    budgetcheck = 0
    algostring = ""
    for i in range(len(ranked)): 
        print(ranked[i].score)
        if ((i+1 <= len(ranked)/2) & (i+1 <= len(ranked)/4)): 
            ranked[i].budget *= .9
        elif ((i+1 <= len(ranked)/2) & (i+1 >= len(ranked)/4)): 
            ranked[i].budget *= .95
        elif ((i+1 >= len(ranked)/2) & (i+1 <= 3*len(ranked)/4)): 
            ranked[i].budget *= 1.05
        elif ((i+1 >= len(ranked)/2) & (i+1 >= 3*len(ranked)/4)): 
            ranked[i].budget *= 1.1
        budgetcheck += ranked[i].budget 
    
    print(ranked[len(ranked)-1].budget)
    if (budgetcheck > totalbudget): 
        print(budgetcheck-totalbudget)
        ranked[0].budget -= (budgetcheck-totalbudget)
    elif (budgetcheck < totalbudget): 
        print(totalbudget-budgetcheck)
        ranked[len(ranked)-1].budget += (totalbudget-budgetcheck)

    for i in range(len(ranked)): 
        algostring += ranked[i].company + " Ad " + str(ranked[i].number) + " New Budget: $" + str(ranked[i].budget) + "\n"
        
    return algostring

def RecommendationAPI(adslist): 
    user_message = "Compare the following ad campaigns with budgets, at the end decide based on the total budget of " + str(totalbudget) + "to allocate to each ad campaign, make it as brief as possible, in this exact format and nothing more - {company name} Ad {number}: ${new budget} (the following is each of the ads, please consider each metric):"
    for i in range(len(adslist)): 
        user_message += "Ad " + str(adslist[i].number) + ", Company: " + adslist[i].company + " Current Budget: " + str(adslist[i].budget) + " Reach: " + str(adslist[i].reach) + " CTR: " + str(adslist[i].ctr) + " CPM: " + str(adslist[i].cpm) + " Conversion Rate: " + str(adslist[i].conv) + " CPA: " + str(adslist[i].cpa) + "\n"


    conversation = [{"role": "user", "content": user_message},]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation,
    )

    reply = response['choices'][0]['message']['content']

    return reply 
        


# now just need to implement recommended pricing changes with algo 
facebook1 = Ads("Facebook", 1, 400, 508, 500, 712,  20, 40)
facebook2 = Ads("Facebook", 2, 400, 5.08, 300, 7.12,  2, 4)
tiktok1 = Ads("Tiktok", 1, 200, 430008, 18, 519,  3.4, 3)
listofads = [facebook1, facebook2, tiktok1]

#API 

print(RecommendationAlgo(listofads))
print(RecommendationAPI(listofads))