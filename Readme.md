# 2D Project 10.020 Data Driven World

#### Initial coditions
We have already created a virtual environment and carried out the transcrypt  in the Vocareum submission.

#### Activating Virtual environment
From the root folder, `Task1_Webpage`

If you are in the work folder, use

```shell
$ cd Task1_Webpage
```
Then enter tthe following command to activate the Virtual environment
```shell
$ source virtenv/bin/activate
```
#### Vocareum
To use Vocareum terminal to run the Flask application, you can do so by running the `runflaskvoc.sh` script. Before running this script, make sure the `voc=True` is set true in the following line inside `Task1_Webpage/app/__init__.py`.

```python
# set voc=False if you run on local computer
application.wsgi_app = PrefixMiddleware(application.wsgi_app, voc=True)
```

Now, make sure you are inside the `Task1_Webpage` folder  by using the `pwd` command. 

```shell
> pwd
```

Use `ls` to ensure that you see the `runflaskvoc.sh` in the current folder.

```shell
> ls
```

Make sure that the script is executable by running the following command. 

```shell
> chmod a+x ./runflaskvoc.sh
```
The above script is to change the file to be executable for all users, group and owner.

To run the script, type the following.

```shell
> ./runflaskvoc.sh
```

Once it is running, you can open another tab in your browser and type the following url: [`https://myserver.vocareum.com/`](https://myserver.vocareum.com/).

To stop the web app type `CTRL+C`. 