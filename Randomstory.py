#importing module
import random
#Defining a list of phrases for sentence making
topic = ['DSA', 'Python', 'Java', 'Computer Networks',' Operating Systems']
adj = ['an important', 'an essential', 'very important', 'an interesting']
to = ['Developers', 'Student',' Professionals', 'Freshers']
supportive = ['learn it',' master it', 'read it', 'see it']
where = [ 'Code Studio.',' javatpoint.']
#generating the output
print(random.choice(topic) + ' is ' + random.choice(adj) + ' topic for ' + random.choice(to) + ', You can ' + random.choice(supportive) + ' from ' + random.choice(where))
