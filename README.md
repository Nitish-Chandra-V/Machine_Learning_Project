# Machine_Learning_Project

Application url : [HousingPredictor](https://ml-regression-app.herokuapp.com/)

# Software and Account Requirements
1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)



**Creating Conda Environment**
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
OR
conda activate venv
```

**To add file to Git**
```
git add
OR
git add <file_name>
```

**NOTE : To ignore file or folder from git we can write name of file/folder in .gitignore file**


**To Check the Git status**
```
git status
```

**To check all version maintained by git**
```
git log
```

**To create version/commit all changes by git**
```
git commit -m "message"
```

**To send version/changes to github**
```
git push origin main
```

**To check remote url**
```
git remote -v
```

**To setup CI/CD pipeline in Heroku we need 3 information**
1. AWS_email = nitishchandra05@gmail.com 
2. AWS_APP_NAME = ml_regression_app


**BUILD DOCKER IMAGE**
```
 docker build -t <image_name>:<tagname>
```
> NOTE : Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000
```

To check running container in docker
```
docker ps
```

To stop docker container
```
docker stop <container_id>
```

```
python setup.py install
```


 




