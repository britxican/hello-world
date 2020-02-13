#!/usr/bin/python3

from github import Github



def main():
    
    query = 'LaCucarachaReloaded'
    print(query)
    
  
    rate_limit = g.get_rate_limit()
    rate = rate_limit.search
    if rate.remaining == 0:
        print(f'You have 0/{rate.limit} API calls remaining. Reset time: {rate.reset}')
        return
    else:
        print(f'You have {rate.remaining}/{rate.limit} API calls remaining')
 
    query = f'"{keyword} english" in:file extension:po'
    result = g.search_code(query, order='desc')
 
    max_size = 100
    print(f'Found {result.totalCount} file(s)')
    if result.totalCount > max_size:
        result = result[:max_size]
 
    for file in result:
        print(f'{file.download_url}')
        
    query2 = 'LaCucarachaReloaded cabalga de nuevo'
    print(query2)
    
    rate_limit = g.get_rate_limit()
    rate = rate_limit.search
    if rate.remaining == 0:
        print(f'You have 0/{rate.limit} API calls remaining. Reset time: {rate.reset}')
        return
    else:
        print(f'You have {rate.remaining}/{rate.limit} API calls remaining')
 
    query = f'"{keyword} english" in:file extension:po'
    result = g.search_code(query, order='desc')
 
    max_size = 100
    print(f'Found {result.totalCount} file(s)')
    if result.totalCount > max_size:
        result = result[:max_size]
 
    for file in result:
        print(f'{file.download_url}')
        query3 = 'CielitoLindoAyAyAy'


if __name__ =='__main__':
    main()
