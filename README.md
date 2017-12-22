# Django_fc_hs
小爬虫应用，使用django来展示，和播放数据，部分功能还没有完成！

环境Python3,Django1.11.7

可以本地搭建玩玩，不建议部署上线，原因你懂得！
Django_fc_hs
    ├── huang_se -->  项目目录            
    │   ├── __init__.py
    │   ├── huang_se--> 项目目录
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── __init__.cpython-36.pyc
    │   │   │   ├── settings.cpython-36.pyc
    │   │   │   ├── urls.cpython-36.pyc
    │   │   │   └── wsgi.cpython-36.pyc
    │   │   ├── settings.py
    │   │   ├── urls.py
    │   │   └── wsgi.py
    │   ├── huangse -->App目录
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── admin.cpython-36.pyc
    │   │   │   ├── models.cpython-36.pyc
    │   │   │   ├── urls.cpython-36.pyc
    │   │   │   └── views.cpython-36.pyc
    │   │   ├── admin.py
    │   │   ├── apps.py
    │   │   ├── hsxsp.txt
    │   │   ├── migrations --> 数据库脚本生成目录
    │   │   │   ├── 0001_initial.py
    │   │   │   ├── 0002_auto_20171221_1640.py
    │   │   │   ├── __init__.py
    │   │   │   └── __pycache__
    │   │   │       ├── 0001_initial.cpython-36.pyc
    │   │   │       ├── 0002_auto_20171221_1640.cpython-36.pyc
    │   │   │       └── __init__.cpython-36.pyc
    │   │   ├── models.py
    │   │   ├── paurl --->爬虫所在目录
    │   │   │   ├── __init__.py
    │   │   │   ├── __init__.py
    │   │   │   ├── __init__.py
    │   │   │   ├── __pycache__
    │   │   │   │   ├── __init__.cpython-36.pyc
    │   │   │   │   ├── huang_se_url.cpython-36.pyc
    │   │   │   │   ├── huang_se_url_open.cpython-36.pyc
    │   │   │   │   ├── huang_se_url_server.cpython-36.pyc
    │   │   │   │   ├── huang_se_video.cpython-36.pyc
    │   │   │   │   └── main_run.cpython-36.pyc
    │   │   │   ├── huang_se_url.py
    │   │   │   ├── huang_se_url_open.py
    │   │   │   ├── huang_se_url_server.py
    │   │   │   ├── huang_se_video.py
    │   │   │   ├── main_run.py
    │   │   │   └── ?\204?\211??\217?\206?\221-?\234??\204?\220\206.txt
    │   │   ├── tests.py
    │   │   ├── urls.py
    │   │   └── views.py
    │   ├── manage.py
    │   ├── static -->静态文件目录
    │   │   ├── css
    │   │   │   ├── bootsnav.css
    │   │   │   ├── bootstrap-theme.css
    │   │   │   ├── bootstrap-theme.css.map
    │   │   │   ├── bootstrap-theme.min.css
    │   │   │   ├── bootstrap.css
    │   │   │   ├── bootstrap.css.map
    │   │   │   ├── bootstrap.min.css
    │   │   │   ├── common.css
    │   │   │   ├── default.css
    │   │   │   ├── detail_p.css
    │   │   │   ├── htmleaf-demo.css
    │   │   │   ├── jumbotron-narrow.css
    │   │   │   ├── normalize.css
    │   │   │   └── video-js.css
    │   │   ├── css2
    │   │   │   ├── bootstrap-theme.css
    │   │   │   ├── bootstrap-theme.css.map
    │   │   │   ├── bootstrap-theme.min.css
    │   │   │   ├── bootstrap.css
    │   │   │   ├── bootstrap.css.map
    │   │   │   ├── bootstrap.min.css
    │   │   │   ├── htmleaf-demo.css
    │   │   │   └── jumbotron-narrow.css
    │   │   ├── dist
    │   │   │   ├── pagination.css
    │   │   │   ├── pagination.js
    │   │   │   ├── pagination.less
    │   │   │   └── pagination.min.js
    │   │   ├── fonts
    │   │   │   ├── glyphicons-halflings-regular.eot
    │   │   │   ├── glyphicons-halflings-regular.svg
    │   │   │   ├── glyphicons-halflings-regular.ttf
    │   │   │   ├── glyphicons-halflings-regular.woff
    │   │   │   ├── glyphicons-halflings-regular.woff2
    │   │   │   ├── icomoon.eot
    │   │   │   ├── icomoon.svg
    │   │   │   ├── icomoon.ttf
    │   │   │   └── icomoon.woff
    │   │   ├── js
    │   │   │   ├── anchor.js
    │   │   │   ├── bootsnav.js
    │   │   │   ├── bootstrap.js
    │   │   │   ├── bootstrap.min.js
    │   │   │   ├── jquery-1.10.2.min.js
    │   │   │   ├── jquery-1.11.0.min.js
    │   │   │   ├── jquery-1.9.1.min.js
    │   │   │   ├── jquery.full-search.js
    │   │   │   ├── npm.js
    │   │   │   ├── vedio.js
    │   │   │   ├── video.min.js
    │   │   │   └── videojs-ie8.min.js
    │   │   ├── media
    │   │   │   ├── 01.jpg
    │   │   │   ├── 240.mp4
    │   │   │   └── zt.png
    │   │   └── related
    │   │       ├── 1.jpg
    │   │       └── 2.jpg
    │   └── templates -->模板文件目录
    │       ├── header.html
    │       ├── index.html
    │       └── tages.html
    ├── huangsedb.sql --> sql数据

