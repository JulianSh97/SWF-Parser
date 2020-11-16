from datetime import datetime
ConsumptionsDict=dict()
UserDict=dict()
cleaned_log_path="log_files/Cleaned_Matlab_Log.txt"
with open (cleaned_log_path) as file:  # Generating a dictionary containing the user name (e.g user1@computer1) as a key and a list of 
    for line in file:                  # all the jobs he is involved in
        line_split=line.split()
        User=line_split[4]
        if User in UserDict.keys():
            UserDict[User].append(line)
        else:
            UserDict.setdefault(User,[]).append(line)
with open(cleaned_log_path) as file:
    for line in file:
        line_split=line.split()
        Request=line_split[3]
        if "IN:" in line_split:     # we only read lines with "OUT"
            continue
        currentUser=UserDict[line_split[4]] # pull the list that contains all the jobs done by this user
        start_time=datetime.strptime(line_split[0], "%H:%M:%S").time()                # calculate the arrival time of the job
        start_time=(start_time.hour)*3600+(start_time.minute)*60+(start_time.second)# and converting it to seconds
        for job in currentUser:
            if  "IN: "+ line_split[3] in job:                               
                endTime=datetime.strptime((job.split())[0], "%H:%M:%S").time() 
                endTime=(endTime.hour)*3600+(endTime.minute)*60+(endTime.second)
        if Request in ConsumptionsDict.keys():
            ConsumptionsDict[Request].append([start_time,endTime])
        else:
            ConsumptionsDict.setdefault(Request,[]).append([start_time,endTime])
