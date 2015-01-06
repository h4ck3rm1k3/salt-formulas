import github3
import urllib2
from secret import p
gh = github3.login('h4ck3rm1k3', password=p)

for result in gh.search_repositories("salt formula", sort='forks'):
    print result
