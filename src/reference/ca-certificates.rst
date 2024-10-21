===========================
CA certificate trust stores
===========================

Secure network connections using TLS (or SSL), e.g. ``https://`` URLs, are
based on *certificates* issued to server operators by *certificate authorities*
(CAs).  Each program which makes these secure connections ultimately needs to
have a list of CAs that are to be trusted and be able to trace the issuance of
a server's certificate back to a trusted CA's root certificate.

This set of trusted CA root certificates is called a *trust store*.  Every
computer system has its own OS-level trust store and usually also has several
other application-specific trust stores on the system.  Typically these are
automatically managed and do not need configuration or modification.

When your network environment includes a proxy, egress firewall, or
institutional CA used internally, however, it may be necessary to configure the
trust store used by an application or modify the trust store contents (e.g.
adding a institutional CA certificate).

This document focuses on configuration and modification of trust stores used by
software that is in turn used by Nextstrain's software.  It focuses only on
changes that can be made without modification of source or program code, e.g.
thru environment variables or config files.

.. contents::
   :local:
   :depth: 3


Operating system
================

Linux uses :ref:`OpenSSL <openssl>` for its system-wide trust store.  macOS and
Windows use their own platform-specific stores, Keychain (managed via
Keychain.app) and Certificate Store (managed via ``certmgr.msc``),
respectively.  OpenSSL and some other software on macOS and Windows systems
(e.g. :ref:`curl`) is sometimes configured by default to use those
platform-specific stores, but not always.

If you need to include an additional CA certificate in the trust store and that
certificate applies to *all* software on the computer (e.g. your web browser),
not just Nextstrain's, then consider adding the CA certificate to the
system-wide trust store and configuring Nextstrain's software to use the
system's trust store instead of any application-specific ones when necessary.
This blanket approach is generally more reliable over time than
application-by-application configuration.


Application software
====================

Most software provides a way to override the trust store by providing a path to
a file containing the the entire set of CA certificates to trust.  Thus, if you
only need to include an additional CA certificate in the trust store, you
should ensure that the file you provide contains a standard set of CA
certificates as well as your addition.  An exception here is if you know for
certain that all connections will use your CA certificate and only yours (e.g.
a mandatory egress proxy that removes (and adds back) TLS for inspection and
policy purposes).

.. _openssl:

OpenSSL library
---------------

OpenSSL is the most common library used to provide TLS/SSL support in
application software.  Its `default locations of trusted CA certificates
<https://docs.openssl.org/3.0/man3/SSL_CTX_load_verify_locations/>`__ can be
overridden by setting the ``SSL_CERT_FILE`` and/or ``SSL_CERT_DIR`` environment
variables.  Filenames in the latter must be hashed with OpenSSL's ``c_rehash``
utility.

Its final trust store is built from certificates in all default locations, so
to *comprehensively* override the defaults, all locations must be overridden.
This is typically unnecessary unless you need to ensure some CAs in the
defaults *aren't* trusted.

.. note::
   Each Conda environment or Docker container has its own isolated copy of
   OpenSSL and its own isolated default CA certificate trust store separate
   from any OS-level OpenSSL trust store.


.. _node.js:

Node.js
-------

*Used by nextstrain.org and Auspice's standalone server component.*

Node.js may use either its own bundled snapshot of `Mozilla's CA trust store`_
or the :ref:`OpenSSL <openssl>` default CA trust store, with the default choice
depending on how it was compiled.

This typically means that ``node`` from your official OS package repositories
defaults to the OpenSSL default CA trust store while ``node`` from `nodejs.org
<https://nodejs.org>`__ (e.g. via ``nvm``), `conda-forge
<https://anaconda.org/conda-forge/nodejs>`__, and other third-party places
defaults to the bundled CA trust store.  You can be explicit about the
preferred CA trust store by including |--use-openssl-ca|_ or
|--use-bundled-ca|_ in the |NODE_OPTIONS| environment variable or by passing
those options directly in your ``node`` invocation.

To override the trust store, set the |NODE_OPTIONS|_ environment variable to
include ``--use-openssl-ca`` and then set OpenSSL's ``SSL_CERT_FILE`` or
``SSL_CERT_DIR`` environment variables.

To add CA certificates to the trust store, set the |NODE_EXTRA_CA_CERTS|_
environment variable.

.. |--use-openssl-ca| replace:: ``--use-openssl-ca``
.. _--use-openssl-ca: https://nodejs.org/api/cli.html#--use-bundled-ca---use-openssl-ca

.. |--use-bundled-ca| replace:: ``--use-bundled-ca``
.. _--use-bundled-ca: https://nodejs.org/api/cli.html#--use-bundled-ca---use-openssl-ca

.. |NODE_OPTIONS| replace:: ``NODE_OPTIONS``
.. _NODE_OPTIONS: https://nodejs.org/api/cli.html#node_optionsoptions

.. |NODE_EXTRA_CA_CERTS| replace:: ``NODE_EXTRA_CA_CERTS``
.. _NODE_EXTRA_CA_CERTS: https://nodejs.org/api/cli.html#node_extra_ca_certsfile


.. _python:

Python
------

Uses the :ref:`OpenSSL library <openssl>` and its defaults.  See
:py:meth:`python:ssl.SSLContext.load_default_certs` and
:py:meth:`python:ssl.SSLContext.set_default_verify_paths`.


.. _python-requests:

``requests`` module
~~~~~~~~~~~~~~~~~~~

*Used by Nextstrain CLI and some pathogen workflows.*

Uses a snapshot of `Mozilla's CA trust store`_ via the |certifi|_ Python
package.

Set the |REQUESTS_CA_BUNDLE|_ environment variable to override.

.. note::
   If a ``requests``-specific CA bundle isn't configured, ``requests`` falls
   back to the |CURL_CA_BUNDLE|_ environment variable (if set).

.. |REQUESTS_CA_BUNDLE| replace:: ``REQUESTS_CA_BUNDLE``
.. _REQUESTS_CA_BUNDLE: https://requests.readthedocs.io/en/latest/user/advanced/#ssl-cert-verification


.. _nextclade-cli:

Nextclade CLI
-------------

*Applies to Nextclade v3.*

Uses its own bundled snapshot of `Mozilla's CA trust store`_ via the
|webpki-roots|_ Rust crate (by way of the ``reqwest`` crate's
|rustls-tls-webpki-roots feature|_).

There is currently no way to configure or modify the trust store without
modifying the Nextclade source code.

.. I have a fix in-flight for ↑ that. —trs, 10 Oct 2024

.. |webpki-roots| replace:: ``webpki-roots``
.. _webpki-roots: https://docs.rs/webpki-roots/0.26.6/webpki_roots/

.. |rustls-tls-webpki-roots feature| replace:: ``rustls-tls-webpki-roots`` feature
.. _rustls-tls-webpki-roots feature: https://docs.rs/reqwest/0.12.8/reqwest/#optional-features



.. _aws-cli:

AWS CLI
-------

*Used by some pathogen workflows.*

The AWS CLI (v1 and v2), via `Botocore`_, uses a snapshot of `Mozilla's CA
trust store`_ via the |certifi|_ Python package when it's available, otherwise
it falls back to `its own bundled CA trust store <botocore-cacerts_>`_.

Set the |AWS_CA_BUNDLE|_ environment variable or |ca_bundle|_ profile
configuration to override.

.. note::
   If an AWS-specific CA bundle isn't configured, the AWS CLI falls back to the
   |REQUESTS_CA_BUNDLE|_ environment variable (if set).

.. _aws-sdks:

AWS SDKs
--------

*Used by Nextstrain CLI and nextstrain.org.*

The AWS SDKs for JavaScript (v2 and v3) default to the :ref:`Node.js <node.js>`
trust store.

Set the |AWS_CA_BUNDLE|_ environment variable or |ca_bundle|_ profile
configuration to override.

.. _Botocore: https://pypi.org/project/botocore/
.. _Mozilla's CA trust store: https://wiki.mozilla.org/CA/Included_Certificates
.. _botocore-cacerts: https://github.com/boto/botocore/blob/master/botocore/cacert.pem

.. |certifi| replace:: ``certifi``
.. _certifi: https://pypi.org/project/certifi/

.. |AWS_CA_BUNDLE| replace:: ``AWS_CA_BUNDLE``
.. _AWS_CA_BUNDLE: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html#envvars-list-AWS_CA_BUNDLE

.. |ca_bundle| replace:: ``ca_bundle``
.. _ca_bundle: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-config-ca_bundle


.. _curl:

curl
----

*Used by many pathogen workflows.*

Curl can come with support for many different TLS implementations, which means
how to configure or modify the CA trust store in use can vary between copies of
``curl``, even when they're the same version.  Refer to the `curl book`_ and
`curl docs`_ for more details about which trust stores are used when and
configuration basics.

Set the |CURL_CA_BUNDLE|_ environment variable to override.

.. note::
   Curl also respects the ``SSL_CERT_FILE`` and ``SSL_CERT_DIR`` environment
   variables, even if the TLS implementation in use is not OpenSSL (with one
   exception).  This is handy if you're setting those already, as you can avoid
   setting ``CURL_CA_BUNDLE`` too.

.. _curl book: https://everything.curl.dev/usingcurl/tls/verify.html
.. _curl docs: https://curl.se/docs/sslcerts.html

.. |CURL_CA_BUNDLE| replace:: ``CURL_CA_BUNDLE``
.. _CURL_CA_BUNDLE: https://curl.se/docs/manpage.html#CURLCABUNDLE
