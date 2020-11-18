# Introduction to Python
**Lesson 13 - Third-Party Packages**

**Ian Clark - 17.11.2020**

https://pollev.com/ianclark604

----

## What is a third party package?
* A package, which needs to be installed separately in order to be used
* Typically, these are distributed over the internet
* Because Python was created in 1991, before the internet was really a thing, there are lots of tools and ways of distributing Python packages, but there is at least now one de-facto way...

----

## Installing packages via `pip`
* When you install Python, you also install its default package manager, `pip` (which stands for "Pip Installs Python...)
* Using pip, we can search for, install/uninstall packages and list the packages we already have installed
* Lets look at these in more detail (lets use `arrow` as an example)
  * `pip search <package>`
  * `pip install <package>`
  * `pip show`
* Packages can have their own _dependencies_, and we'll need to download these too if we didn't have them installed already
* Some packages require us to install some other system applications (e.g. for Windows or Linux) in order to work properly
* Packages have versions, and these versions are immutable

----

## Where do the packages come from?

* By default, `pip` install packages from PyPI (Python Package Index)
* You can browse all the packages at https://pypi.org/

----

## Where are third party packages saved to?

* Lets use the `__path__` property to find out

```py
import arrow
print(arrow.__path__)
```

* The `sys.path` attribute gives us all the places where Python will look for modules to import
* And the order _is_ important (relative imports to fix)

----

## Keeping track of your packages
* `pip freeze > requirements.txt`
* `pip install -r requirements.txt`
* Package "pinning"

----

## Side Note - Python Virtual Environments

* Python virtual environments allow us to have multiple versions of Python on one system
* This becomes very important as soon as you start to develop multiple projects, and need to ensure that you have all of the right packages

```bash
python -m venv venv

# On Linux
source venv/bin/activate

# On Windows
<venv>\Scripts\activate.bat  # cmd
<venv>\Scripts\Activate.ps1  # powershell
```

---

## Python "modules"

* A "module" in Python is a collection of files within a special folder
* This folder *must* have an `__init__.py` file

---

## What Packages can I use?

* Check out the [Awesome Python](https://github.com/vinta/awesome-python) to get some inspiration on some of the most interesting Python packages available.

----

## Lets do something practical - Django

* https://djangoproject.com
* https://docs.djangoproject.com/en/3.1/intro/tutorial01/

