Enzyme Technology Internship 2019 |build|
=========================================

Installation
------------
Clone the repository from GitHub using GitHub desktop or writing the following command in the command line:

.. code-block:: sh

    $ git clone https://github.com/bit-lsi/ENZT2019.git

change into the appropriate directory and install with ``pip``:

.. code-block:: sh

    $ cd ENZT2019
    $ python3 -m pip install -e .

Structure of the Source Code
----------------------------
All code and data lives inside the ``src/`` folder. Inside it are the following folders:

- **bel**: Where source BEL script and their corresponding compiled artifacts are stored. They can be accessed with
  ``enzt2019-knowledge``.
  
.. |build| image:: https://travis-ci.com/bit-lsi/ENZT2019.svg?branch=master
    :target: https://travis-ci.com/bit-lsi/ENZT2019
