# Lightwire Web Scraper

For pulling usage data from the Lightwire account overview page and exposing it for services. This data will be exposed through a RESTful endpoint and Pushbullet.

---

## Environment
In this context we will be setting up a Windows enviroment if you use linux you should be able to look at this and do the equivalent.


Go to the Python website and download a version >= 3.7
https://www.python.org/downloads/release/python-370/

Select the custom install option and don't install IDLE then make sure add to path is selected. This should  install python and our package manager pip.

Next we want to install some global packages so open up a command prompt:
```bash
$ pip install virtualenvwrapper-win
```

Now lets create our environment to work out of:
```bash
$ mkvirtualenv lightwire
```

This will add (lightwire) to the front of our path indicating we are no longer working globally, next lets set our environments root directory. Navigate the command prompt to the project directory and run:
```bash
$ setprojectdir .
```

Next time we want to workon the project from a fresh command prompt it will navigate straight here, try it:
```bash
$ deactivate
$ cd c:
$ workon SlackBot
```

Finally lets install all the packages we need:
```bash
$ pip install -r /path/to/requirements.txt
```

If you add any libraries make sure to add them to requirements file so others can install them.

---

## Running Application

From the root directory open a command prompt and run the command:
```bash
$ py slack.py
```


---

## Config

Most config files will have an example of how they should be formatted e.g. config.example.json
Make a copy of that and rename it to get started. If you implement something with a config make an example and add the actual file to the gitignore.