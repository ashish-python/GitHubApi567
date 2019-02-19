"""
Author: Ashish Singh

The program asks the user to input their Github ID

Calls the call_api() function which connects to the api and returns a dictionary with key as repository
name and value as number of commits

For a repository with no commits, "Data not available" is returned

The function is tested through test cases in TestRestAPI.py file

"""
import urllib.request
import json

def call_api(gitID):
        
    api_url = "https://api.github.com/"
    result_dict = dict()
    try:
        connection1=urllib.request.urlopen(api_url+"users/"+gitID+"/repos")
    except urllib.error.URLError as e:
        print("Unable to connect to the repository",gitID,"at this time")
        raise e
    else:
        data = connection1.read().decode()
        js = json.loads(data)      
         
        for repo in js:            
            try:
                connection2=urllib.request.urlopen(api_url+"repos/"+gitID+"/"+repo['name']+"/commits")
            except urllib.error.URLError as e:
                if(e.reason == "Conflict"):
                    result_dict[repo['name']] = "Data not available"
                    continue
                else:
                    print("Unable to connect to commits for repository",repo['name'],"at this time")
                    raise e
            else:
                data_commits = connection2.read().decode()    
                js_commits = json.loads(data_commits)
            result_dict[repo['name']] = len(js_commits)
        return(result_dict)

if(__name__=="__main__"):
    loop = True
    while(loop):
        #Prompt the user to enter Github ID
        gitID = input("Enter Github ID: ")    
        try:
            results = call_api(gitID)
            for key,result in results.items():
                print("Repository:",key,", Commits:",result)
                print(results)
            loop = False
        except ValueError as e:
            print(e)
        except urllib.error.URLError as e:
            print(e.reason)  
    else:
        print("All done!")
