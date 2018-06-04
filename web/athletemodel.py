import pickle
from athletelist import AthleteList

def get_coach_data(file_name):
    try:
        with open(file_name) as f:
            data = f.readline()
        file_content = data.strip().split(',')
        return (AthleteList(file_content.pop(0),file_content.pop(0),file_content))
    except IOError as err:
        print('File error ' + str(err))
        return None

def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle','wb') as athf:
            pickle.dump(all_athletes,athf)
    except IOError as err:
        print("File error:"+str(err))
    return(all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle','rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as err:
        print("File error : " + str(err))
    return(all_athletes)