Simple Usage
============

Try PyKayacIM on the Python interactive interpereter
----------------------------------------------------

To send a push notification using PyKayacIM, just follow these three steps:

#. Import the module :py:mod:`pykayacim.api` , which is the core module of
   PyKayacIM.
#. Intialize an instance of :py:class:`pykayacim.api.KayacIMAPI` by providing
   your user credentials.
#. Invoke :py:meth:`pykayacim.api.KayacIMAPI.send` to send a notification.

.. code-block:: python

    # Step 1
    import pykayacim.api
    
    

