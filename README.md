#sewiseXBLock 
by wwj718:<wuwenjie718@gmail.com>

优酷开发平台：http://open.sewise.com/

#安装（平台级别的设置）
<pre><code>
sudo su edxapp -s /bin/bash
cd ~
source edxapp_env
pip install -e git+https://github.com/wwj718/sewiseXBLock
在/edx/app/edxapp/cms.envs.json 添加 `"ALLOW_ALL_ADVANCED_COMPONENTS": true,` 到FEATURES
</code></pre>
#在studio中设置(课程级别的设置)
进入到"Settings" ⇒ "Advanced Settings",将"sewise"添加到Advanced Module List

#使用方法（结合优酷）
参考我的文章:[在edx中使用优酷视频服务](http://wwj718.github.io/edx-use-sewise.html)


#TIDO
##视频上传
http://open.sewise.com/docs?id=109
