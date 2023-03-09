# refs
some refs to build this module


## readme
+ [Making a PyPI-friendly README](https://packaging.python.org/en/latest/guides/making-a-pypi-friendly-readme/)


## build and publish
+ [Create your own Python package and publish it into PyPI](https://towardsdatascience.com/9306a29bc116)


```python
import setuptools

setuptools.setup(
  name="charnstr",
  version="0.0.1",
  author="Sparisoma Viridi",
  description="Analyze a string for its characters information",
  packages=["charnstr"]
)
```

```batch
PS L:\home\charnstr> python setup.py sdist
running sdist
running egg_info
creating charnstr.egg-info
writing charnstr.egg-info\PKG-INFO
writing dependency_links to charnstr.egg-info\dependency_links.txt
writing top-level names to charnstr.egg-info\top_level.txt
writing manifest file 'charnstr.egg-info\SOURCES.txt'
reading manifest file 'charnstr.egg-info\SOURCES.txt'
adding license file 'LICENSE'
writing manifest file 'charnstr.egg-info\SOURCES.txt'
running check
creating charnstr-0.0.1
creating charnstr-0.0.1\charnstr
creating charnstr-0.0.1\charnstr.egg-info
creating charnstr-0.0.1\test
copying files to charnstr-0.0.1...
copying LICENSE -> charnstr-0.0.1
copying README.md -> charnstr-0.0.1
copying setup.py -> charnstr-0.0.1
copying charnstr\__init__.py -> charnstr-0.0.1\charnstr
copying charnstr\charnstr.py -> charnstr-0.0.1\charnstr
copying charnstr.egg-info\PKG-INFO -> charnstr-0.0.1\charnstr.egg-info
copying charnstr.egg-info\SOURCES.txt -> charnstr-0.0.1\charnstr.egg-info
copying charnstr.egg-info\dependency_links.txt -> charnstr-0.0.1\charnstr.egg-info
copying charnstr.egg-info\top_level.txt -> charnstr-0.0.1\charnstr.egg-info
copying test\test_charnstr.py -> charnstr-0.0.1\test
Writing charnstr-0.0.1\setup.cfg
creating dist
Creating tar archive
removing 'charnstr-0.0.1' (and everything under it)
```

```batch
PS L:\home\charnstr> twine upload --repository-url https://test.pypi.org/legacy/ dist/*
Uploading distributions to https://test.pypi.org/legacy/
Enter your username: dudung
Enter your password:
Uploading charnstr-0.0.1.tar.gz
100% ---------------------------------------- 4.9/4.9 kB • 00:01 • ?

View at:
https://test.pypi.org/project/charnstr/0.0.1/
PS L:\home\charnstr>
```

```batch
PS L:\home\charnstr> pip show charnstr
WARNING: Package(s) not found: charnstr
```

```batch
PS L:\home\charnstr> pip install -i https://test.pypi.org/simple/ charnstr==0.0.1
Looking in indexes: https://test.pypi.org/simple/
Collecting charnstr==0.0.1
  Downloading https://test-files.pythonhosted.org/packages/ca/e9/be357ea475bfa31f9592e5a441df1f9c5f7411d5e2cd058ce2ee07f38f23/charnstr-0.0.1.tar.gz (2.3 kB)
  Preparing metadata (setup.py) ... done
Building wheels for collected packages: charnstr
  Building wheel for charnstr (setup.py) ... done
  Created wheel for charnstr: filename=charnstr-0.0.1-py3-none-any.whl size=2680 sha256=cc1abc160b30ead9ebf1766b3ce6c4500d18295d4c95afd5cda6de973926e3e7
  Stored in directory: c:\users\sparisoma viridi\appdata\local\pip\cache\wheels\5f\4a\54\887fc92c45a9c4eeed3dcb0cfde148d66a30493dd67fc42ff9
Successfully built charnstr
Installing collected packages: charnstr
Successfully installed charnstr-0.0.1
PS L:\home\charnstr>
```

```batch
PS L:\home\charnstr> pip show charnstr
Name: charnstr
Version: 0.0.1
Summary: Analyze a string for its characters information
Home-page:
Author: Sparisoma Viridi
Author-email:
License:
Location: c:\users\sparisoma viridi\appdata\local\packages\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\site-packages
Requires:
Required-by:
PS L:\home\charnstr>
```

## test
+ [A Typical directory structure for running tests using unittest](https://gist.github.com/tasdikrahman/2bdb3fb31136a3768fac)

```batch
PS L:\home\charnstr> python -m unittest test.test_charnstr
```
