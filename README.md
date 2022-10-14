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

Run one specific test. This must be run in this directory. Adjust `--nvms` to
the number of VMs that should be started concurrently, typically the number of
CPUs available.

```
vmshed --nvms 8 --torun xfs_156
```

Run all tests:

```
vmshed --nvms 8
```

The output from the tests will be written to the directory `tests-out`.

## Improvements

* Only run tests that are expected to succeed.
* Prepare a special base image in advance with the packages already installed.
  Currently `provision-test.toml` does everything necessary to set up the VM
  from a stock Ubuntu 22.04 image. Most of these steps can be performed in
  advance rather than for every test run. This would reduce the time required
  for the provisioning step.
* Test other filesystems.
* Run test groups from fstests.
* Test kernels other than the stock one.
* Run multiple fstests tests in each VM. For instance, tests that are known to
  be fast and stable could be grouped together.
