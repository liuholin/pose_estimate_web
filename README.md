# person_pose_estimator
This project is used as a helper for hospital to know the status of each patient. It can detect patient's pose and positioning in real-time, because we place many known zigbee labels in each rooms and equip with a sensor for every patient. As the abnormal circumstance occurs, the nurse can find those changes from the monitor screen system. For web, we use flask as our development framework, and zigbee network is used in pi instead.
## Get Started
### Pi
```
git clone https://github.com/ZhuChaozheng/person_pose_estimator
```
scan your sensor device to find out its bluetooth address
```
sudo bluetoothctl
scan on 
exit
```
change the bluetooth address in *rc.local*
```
vi rc.local
```
also modify the server IP in *bt_S.py*

Now, we have finished the deloyment of hardware layer. Next, Let us consider the web. As you can see, we have a folder of web, you should move it to your web server.
```
scp -r web/ blackant@192.168.1.102:/var/www/html

```
### Ubuntu server
the following operations please switch to your web server
```
cd /var/www/html/web/
python3 manange.py
```

