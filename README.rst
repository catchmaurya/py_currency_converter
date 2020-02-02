.. image:: ./images/currency_converter_logo.jpeg


This is a currency converter that uses https://www.exchangerate-api.com/ API.

Python Currency Converter
-------------------------

This package help in converting converting the any currency amount to any other(s) currency.
This consumes the https://www.exchangerate-api.com/ free REST API.

Installation
------------

You can install directly after cloning:

use the Python package:

.. code-block:: bash

  $ pip install --user py_currency_converter

Command line tool
-----------------

After installation, you should have ``py_currency_converter`` in your ``$PATH``:

.. code-block:: bash

 $ currency_converter 1 USD --to SGD
 1.00 USD = 1.364903 SGD on 2020-02-02

Python API
----------

Create once the currency converter object:

.. code-block:: python

    >>> from py_currency_converter import convert


Convert from ``SGD`` to ``USD, EUR`` using the last available rate:

.. code-block:: python

    >>> convert(base='USD', amount=1, to=['SGD', 'EUR'])
    {'SGD': 1.364903, 'EUR': 0.904506}

Default base currency is ``USD``:

.. code-block:: python

    >>> convert(amount=1, to=['SGD', 'EUR'])
    {'SGD': 1.364903, 'EUR': 0.904506}


supported currencies
~~~~~~~~~~~~~~~~~~~~

Please visit the below link for refering supported currencies:

`Supported currencies <ttps://www.exchangerate-api.com/docs/supported-currencies>`__


License
~~~~~~~
MIT License
~~~~~~~~~~~


.. code:: rst

    |MIT license|

    .. |MIT license| image:: https://img.shields.io/badge/License-MIT-blue.svg


Contact
~~~~~~~
Please submit an issue if you encounter a bug and please email any questions or requests to catchmaurya@gmail.com