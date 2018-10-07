[![Build Status](https://travis-ci.org/steffenlem/Deimmunization.svg?branch=master)](https://travis-ci.org/steffenlem/Deimmunization)
[![codecov](https://codecov.io/gh/steffenlem/Deimmunization/branch/master/graph/badge.svg)](https://codecov.io/gh/steffenlem/Deimmunization)

# Deimmunization Tool iGEM Team Tübingen

Software project of the iGEM Team Tübingen 2018    
Detection and removal of immune epitopes in proteins

Quick Setup for developers
=====
1. <code>$ git clone https://github.com/steffenlem/Deimmunization</code>
2. <code>$ python setup.py install</code>
3. Installation of NetMHCIIpan (http://www.cbs.dtu.dk/cgi-bin/nph-sw_request?netMHCIIpan)
4. <code>$ deimmunization</code>

Usage
=====

## The CLI - Command Line Interface

```
$ deimmunization --help

Options:
  -in, --input_msa <arg>           file path to msa.txt  [required]
  -rs, --reference_sequence <arg>  titlestring of reference sequence
                                  [required]
  -t, --majority_threshold <val>  value between 0 and 1 to decide the
                                  consensus value  [required]
  -a, --mhc_alle <arg>             MHC class II allel e.g. DRB1_0101
                                  [required]
  -p, --mhc_ii_pan <arg>           path to netMHCIIpan  [required]
  --help                          Show this message and exit.

```


Examples
=====
- 

License
=====
Our tool is made available under the [MIT License](http://www.opensource.org/licenses/mit-license.php).

Authors
=====
The iGEM Team Tübingen drylab developers

