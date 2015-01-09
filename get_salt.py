import github3
import urllib2
from secret import p
gh = github3.login('h4ck3rm1k3', password=p)

for r in gh.search_repositories("saltstack", sort='forks'):
    print r.repository
