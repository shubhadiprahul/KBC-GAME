import json

questions = {}
questions['data'] = []

questions['data'].append({
'question':'Q1.Which son was most loved by Sumitra?',
'answer':'''A) Laxman and Shatrughan
B) Ram
C) Laxman
D) All four brothers'''
})

questions['data'].append({
'question':'Q2.Who built the famous Shalimar bagh of Srinagar?',
'answer':'''A) Humayun
B) Akbar
C) Jahangir
D) Shahjahan'''
})

questions['data'].append({
'question':'Q3.Which social networking site was used by government to invite suggestions from citizens for recently conducted budget?',
'answer':'''A) Facebook
B) Twitter
C) Google Plus
D) Tagged'''
})

questions['data'].append({
'question':'Q4.What runs between the North Sea and the Atlantic Ocean?',
'answer':'''A) Labrador Sea‎
B) James Bay‎
C) The English Channel
D) Greenland Sea'''
})

questions['data'].append({
'question':'Q5.Which team won the IPL (2009)?',
'answer':'''A) Deccan Chargers
B) Chennai Super Kings
C) Kolkata Knight Riders
D) Delhi Daredevils'''
})

questions['data'].append({
'question':'Q6.In which year\'s budget government introduced Service Tax?',
'answer':'''A) 1992
B) 1995
C) 1996
D) 1994'''
})

questions['data'].append({
'question':'Q7.The caves and rock-cut temples at Ellora are?',
'answer':'''A) Buddhist and Jain
B) Hindu and Muslim
C) Buddhist only
D) Hindu, Buddhist and Jain'''
})

questions['data'].append({
'question':'Q8.Which one of the following is not a primary Database?',
'answer':'''A) GDB ( human)
B) SWISS - PROT
C) Protein 3D structure
D) Gene bank protein'''
})

questions['data'].append({
'question':'Q9.Who among the following built the famous Alai Darwaza?',
'answer':'''A) Allaudin Khilji
B) Babur
C) Ibrahim Lodi
D) Shahjahan'''
})

questions['data'].append({
'question':'Q10.Which tax was abolished by government in 2015 Budget?',
'answer':'''A) Gift Tax
B) Wealth tax
C) Education Tax
D) Road tax'''
})


with open('questions.json', 'w') as outfile:
    raw = json.dumps(questions,indent=4,sort_keys=True)
    outfile.write(raw)
    outfile.close()
