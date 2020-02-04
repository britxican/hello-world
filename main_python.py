#!/usr/bin/python3

from github import Github



def main():
    
    accstkn = '3f2d96d98983f7c2675e7d53281b6a2cfdf6120a'
    g = Github(accstkn)
    
    # https://python.gotrained.com/search-github-api/
    query = 'LaCucarachaReloaded'
    result = g.search_repositories(query, 'stars', 'desc')
    print('Found {} repo(s)'.format(result.totalCount))
    for repo in result:
        print(repo.clone_url)


if __name__ =='__main__':
    main()
