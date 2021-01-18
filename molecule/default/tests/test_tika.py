import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_tikasrv(host):
    tikasrv = host.socket('tcp://0.0.0.0:9998')
    assert tikasrv.is_listening
