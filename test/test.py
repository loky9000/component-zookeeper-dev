import os
import requests

from test_runner import BaseComponentTestCase
from qubell.api.private.testing import instance, environment, workflow, values


@environment({
    "default": {},
    "AmazonEC2_CentOS_63": {
        "policies": [{
            "action": "provisionVms",
            "parameter": "imageId",
            "value": "us-east-1/ami-bf5021d6"
        }, {
            "action": "provisionVms",
            "parameter": "vmIdentity",
            "value": "root"
        }]
    },
    "AmazonEC2_Ubuntu_1204": {
        "policies": [{
            "action": "provisionVms",
            "parameter": "imageId",
            "value": "us-east-1/ami-967edcff"
        }, {
            "action": "provisionVms",
            "parameter": "vmIdentity",
            "value": "ubuntu"
        }]
    },
    "AmazonEC2_Ubuntu_1004": {
        "policies": [{
            "action": "provisionVms",
            "parameter": "imageId",
            "value": "us-east-1/ami-9f3906f6"
        }, {
            "action": "provisionVms",
            "parameter": "vmIdentity",
            "value": "ubuntu"
        }]
    }
})
class ComponentTestCase(BaseComponentTestCase):
    name = "component-zookeeper-dev"
    apps = [{
        "name": name,
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../%s.yml' % name))
   }]
    
    @instance(byApplication=name)
    def test_zoo_ui(self, instance):
        hosts = instance.returnValues['output.zoo-ui']
        for host in hosts:
           resp = requests.get(host, verify=False)
           assert resp.status_code == 200
