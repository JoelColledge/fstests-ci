# `vmshed` Configuration for `(x)fstests`

This repository contains configuration to run the Linux kernel
[fstests](https://github.com/kdave/xfstests) test suite with
[vmshed](https://github.com/LINBIT/vmshed).

## Configuration Files

* `vms.toml` describes the VMs to use for the tests.
* `provision-test.toml` contains the script to prepare the VM image which is
  used for the tests.
* `vmshed_tests_generator.py` and `tests.header.toml` are used to generate
  `tests.toml` which describes the tests to run.
* `run.toml` contains the script that executes a test.
* `.gitlab-ci.yml` and `version.env` configure a GitLab pipeline to run the
  tests. This has some elements which are specific to LINBIT's infrastructure.

## Requirements

* The [`vmshed`](https://github.com/LINBIT/vmshed) binary.
* A working installation of [Virter](https://github.com/LINBIT/virter). This
  requires `libvirt`.

## Usage

Re-generate the list of tests:

```
./vmshed_tests_generator.py <path-to-xfstests> > tests.toml
```

Run one specific test (run in this directory):

```
vmshed --nvms 8 --torun xfs_156
```

Run all tests (run in this directory):

```
vmshed --nvms 8
```

The output from the tests will be written to the directory `tests-out`.
