import os

os.system('powertop --html=process.html -time=1')



f=open("process.html","rt")


temp = 0
power_usage = 0
state = 'no'
while True:
    line = f.readline()
    if not line :
        break

    if line.find('<h2 class="content_title"> Overview of Software Power Consumers </h2>') != -1:
        state = 'ok';
    if state == "ok" :
        if line.find('<tr class="emph1">') != -1 & line.find('<th class="emph_title"> Usage </th> <th class="emph_title"> Wakeups/s </th> ') == -1 :
            temp =  line.split('<td class="no_wrap">')[-1]
            if temp.find('uW') != -1:
                power_uw = temp.split('uW')[0]
                print(float(power_uw))
                power_usage += float(power_uw)*0.000001
            elif temp.find('mW') != -1:
                power_mw = temp.split('mW')[0]
                print(float(power_mw))
                power_usage += float(power_mw)*0.001
            elif temp.find('W') != -1:
                power_w = temp.split('W')[0]
                print(float(power_w))
                power_usage += float(power_w)
#print("power_usage = ", power_usage)
        if line.find('</table>') != -1 :
            break
print('power_usage = ', power_usage)
f.close()
