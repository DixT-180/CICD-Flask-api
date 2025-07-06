# Built with Docker and auto-published to Docker Hub via GitHub Actions CI/CD.


## To run the image as container after deploying to dockerhub,

```bash
docker pull dikshyant180/dq-check-fastapi
```


## To run as container,

```bash
docker run -d -p 5000:5000 dikshyant180/dq-check-fastapi 
```

### Now the api becomes acessible at localhost:5000

In cmd, provide directory of the csv dataset to file variable.

```bash
curl -X POST -F "file=@\"C:\\Users\\Dikshyant\\Desktop\\github_action_docker\\tested.csv\"" http://localhost:5000/check

```

This will give details like,


```bash
{"columns":12,"duplicate_rows":0,"missing_values":{"Age":86,"Cabin":327,"Embarked":0,"Fare":1,"Name":0,"Parch":0,"PassengerId":0,"Pclass":0,"Sex":0,"SibSp":0,"Survived":0,"Ticket":0},"rows":418}
```
