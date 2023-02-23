def env_to_json(env_file_path='/Users/jeremyvangansbeg/Documents/project/jeremy_vangansberg/web/.env'):
    """Transform .env to json format for Azure App Service environnements variables

    Args:
        env_file_path (str): full path to the .env file

    Returns:
        json: print the json
    """
    import re
    import json
    env_file = open(env_file_path, 'r')
    Lines = env_file.readlines()
    print(Lines)
    
    env_list = []
    for line in Lines :
        key = re.search('^.*?(?==)', line).group(0)
        value = re.search('(?<==).*', line).group(0)

        entry = {
            "name": key,
            "value": value,
            "slotSetting": "false"
            }

        env_list.append(entry)
    env_list=json.dumps(env_list)

    return env_list

if __name__ == "__main__" :
    print(env_to_json())