import github3
import urllib2
from secret import p
gh = github3.login('h4ck3rm1k3', password=p)

for result in gh.search_code("salt extension:sls language:Scheme"):
    print result
    
for result in gh.search_code("salt extension:sls language:SaltStack"):
    print result

#for result in gh.search_code("yaml . jinja"):    print result

