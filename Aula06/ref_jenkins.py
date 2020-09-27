import jenkins

jenkins_con = jenkins.Jenkins(
    "http://192.168.1.10:8080", 
    username="rlaecio", 
    password="louvor01"
)

#jenkins_con.create_job('Python-JOb', jenkins.EMPTY_CONFIG_XML)

#queue = jenkins_con.build_job('Python-JOb')
#print(jenkins_con.get_queue_item(queue))
#print(jenkins_con.get_jobs())

#print(jenkins_con.get_job_config("Python-Job"))
jenkins_con.reconfig_job("Python-JOb", jenkins.EMPTY_CONFIG_XML)
