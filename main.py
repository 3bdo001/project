import yaml

project = input("for bgp press 1 for ospf press 2 for static press 3")


if int(project) == 1:

    from jinja2 import Environment,FileSystemLoader
    env=Environment(loader=FileSystemLoader("."))
    temp=env.get_template("bgp.j2")

    with open("Bgp.yaml") as file:
        data = yaml.full_load(file)
    output1=temp.render(int=data)
    print(output1)
    print(data)
elif int(project)== 2:
    from jinja2 import Environment, FileSystemLoader
    env = Environment(loader=FileSystemLoader("."))
    temp = env.get_template("ospf.j2")

    with open("Ospf.yaml") as file:
        data = yaml.full_load(file)
    output1 = temp.render(int=data)
    print(output1)
    print(data)
else:
    from jinja2 import Environment, FileSystemLoader
    env = Environment(loader=FileSystemLoader("."))
    temp = env.get_template("static.j2")

    with open("static.yml") as file:
        data = yaml.full_load(file)
    output1 = temp.render(int=data)
    print(output1)
    print(data)




import paramiko
import time
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.2.2',port=22,username='admin',password='admin@123')
cli = ssh.invoke_shell()
cli.send('en \n')
cli.send('show ip interface brief \n')
cli.send("conf ter \n")
cli.send(output1)
time.sleep(6)
output=cli.recv(999999).decode()
print(output)


