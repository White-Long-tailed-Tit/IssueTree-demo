import requests
import json

def get_git_blame(owner, repo, file_path, token, branch):
    headers = {
        'Authorization': f'token {token}'
    }
    
    # GraphQL 쿼리
    query = """
    query GetGitBlame($owner: String!, $repo: String!, $file_path: String!, $branch: String!) {
      repository(owner: $owner, name: $repo) {
        object(expression: $branch) {
          ... on Commit {
            blame(path: $file_path) {
              ranges {
                startingLine
                endingLine
                age
                commit {
                  oid
                  author {
                    name
                    email
                  }
                }
              }
            }
          }
        }
      }
    }
    """
    
    variables = {
        "owner": owner,
        "repo": repo,
        "file_path": file_path,
        "branch": branch
    }
    
    response = requests.post('https://api.github.com/graphql', json={'query': query, 'variables': variables}, headers=headers)
    
    if response.status_code == 200:
        blame_data = response.json()
        return blame_data
    else:
        print(f"Failed to retrieve Git blame data: {response.status_code}")
        return None

# GitHub 저장소 정보
owner = 'White-Long-tailed-Tit'
repo = 'IssueTree-demo'
branch = 'main'

# 파일 경로
file_path = 'demo/src/main/java/com/example/demo/Member/controller/MemberController.java'

# 사용자 인증 토큰
token = '당신의_사용자인증토큰을_넣어주세요'

# Git blame 정보 가져오기
blame_data = get_git_blame(owner, repo, file_path, token, branch)
if blame_data:
    # Git blame 정보 출력
    print(json.dumps(blame_data, indent=2))
