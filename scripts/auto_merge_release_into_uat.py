import os
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from ghapi.all import GhApi as GHApi




github_access_token = os.environ['GITHUB_TOKEN']
github_context = json.loads(os.environ['GITHUB_CONTEXT'])

release_branch_name = github_context['sha']
target_branch_name = 'uat'


client = GHApi(owner = 'cultureiq', repo = 'app2', token = github_access_token)

try:
	merge_response = client.repos.merge(target_branch_name, release_branch_name, 'Auto Backwards Merge From GH Robot!')
	print('Clean merge!')
except Exception as e:
	print(e)
