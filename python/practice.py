def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res=[]

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1,n-2):

                if j > i+1 and nums[j] == nums[i]:
                    continue

                l , r = j+1, n -1

                while l<r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]

                    if s == target:
                        res.append([nums[i] , nums[j] , nums[l] ,nums[r]])
                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
        return res    
            
                            

                    




'''Caching Dictionary()
import time

class Cache:
    def __init__(self):
        self.cache = {}
        
    def store(self, key, value,ttl):
        expiration_time = time.time() + ttl
        self.cache[key] = {'value' : value, 'expiration' : expiration_time}
        print(f"Stored {key} : {value} with ttl {ttl}")
        
    def retrive(self,key):
        if key in self.cache.keys():
            if self.cache[key]['expiration'] < time.time():
                del self.cache[key]
                return (f"Time expired for user {key}")

            else:
                return self.cache[key]['value']
        else:
            return ('The record doesnt exist')
    
    
cache = Cache()
cache.store('user1',{'name' : 'Josh', "age" : 30}, ttl = 15)
cache.store('user2',{'name' : 'Joshi', "age" : 39}, ttl = 1)

print(cache.retrive(input()))      
'''

#printing the size of files on ssd
'''import os
import pathlib as Path

def find_file(pathway, size_limit = 100 * 1024 * 1024):
    for foldername, subfiles , filenames in os.walk(pathway):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            try:
                fie_size = os.path.getsize(file_path)
                if fie_size  > size_limit:
                    print(f"Large file : {file_path} ({fie_size / (1024 * 1024):.2f} MB)")
            except FileNotFoundError:
                print(f"File not found {file_path}")    
            except PermissionError:
                print(f"File couldn't be accessed {file_path}")
            
            
find_file("E:/")'''

# Capital quiz for 35 different folders. Jumbled up for about 50 different quesions with answers
'''import random
   # The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New\
   Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West\
   Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


for total_files in range(35):
    with open(f"Quiz_answers{total_files}.txt", "w+") as fanswers:
        
        fanswers.write("Here are your answers : \n\n")
        
        all_answers = [i for i in capitals.values()]
        random.shuffle(all_answers)
        all_questions = [s for s in capitals.keys()]
        random.shuffle(all_questions)
        
        for index, i in enumerate(all_questions):
            fanswers.write(f"{index}. {capitals[i]} \n")
        
    with open(f"Quiz_file{total_files}.txt" , "w+") as fquiz:
        fquiz.write("Name : \n")
        fquiz.write("Class : \n")
        fquiz.write("Subject : \n\n")
        
        p = 1
        for state, capital in zip(all_questions, all_answers):
            fquiz.write(f'{p}Whats the capital for the state {state}: \n')
            correct_answer =  capitals[f"{state}"]
            wrong_options = random.sample([ans for ans in all_answers if ans != correct_answer], 3)


            options = wrong_options + [correct_answer]
            random.shuffle(options)
            
            for index,i in enumerate(options):
                fquiz.write(f"{'ABCD'[index]}. {i} \n")
            fquiz.write("\n")
            p += 1'''
    