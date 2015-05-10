Setup Play Scala Framework
==========================
1. Download Activator from https://www.playframework.com/download
2. Unzip the folder
3. Add the activator to PATH. On linux, add the following to ~/.bashrc
```export PATH=$PATH:<pathToActivator>```

Setup Node
==========
Make sure you have node installed. If not, run:
```
sudo apt-get update
sudo apt-get install nodejs
sudo apt-get install npm
```

Build Project
=============
1. Clone repository:
```
"git clone git@github.com:jschen5/audiobits.git audiobits"
```
2. Run "activator" (this will take awhile to download the necessary dependencies)
** You should now be in the Play/Activator console (if not, run "activator" again)
3. Run "run" (this will also install some dependencies)
(If you encounter a Kernel inotify watch limit reached error, check out this helpful post: http://unix.stackexchange.com/questions/13751/kernel-inotify-watch-limit-reached)
** At this point, the server should be running on 0.0.0.0:9000
4. Install the necessary node modules by running:
```
npm install
```
5. Last but not least, build the front end. Run the following command to build and watch for changes to js or less:
```
npm run watch
```
