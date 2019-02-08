from pykafka import KafkaClient
import json
from datetime import datetime


client = KafkaClient(zookeeper_hosts="172.30.5.64:2181,172.30.5.69:2181,172.30.5.70:2181")



topic = client.topics[b'adhoc1.render']
with topic.get_sync_producer() as producer:
    producer.produce(json.dumps(
        {
            "task": {
                "render": {
                    "template": "aftr.pwgd.assets/email/campaigns/verifications/html/prodUploadSuccessful.jinja",

                    "context": {
                        "client": "pwgd",
                        "application": "notifications",
                        "brand": "pwgd",
                        "language": "en",
                        "region": "US",
                        "cell": "",
                        "topic": ""

                    },

                    "model": {
                        "email": "drautela@afterinc.com",
                        "dateProcessed": "August 15, 2018",
                        "fileStatus": "Completed With No Errors",
                        "fileID": "81c31e9d-59cc-4abf-9bd7-1357f0ebed10",
                        "fileURL": "https://pwgd.aftersystems.com/data-management/upload-history/81c31e9d-59cc-4abf-9bd7-1357f0ebed10?manufacturerId=384773",
                        "fileName": "test-jinko-search-sn.csv",
                        "fileDescription": "Describe the file",
                        "totalUploaded": 3,
                        "totalFailed": 0,
                        "totalLoaded": 3
                    }
                }
            },
            "timestamp": datetime.utcnow().timestamp(),

            "then":
                {
                    "queue": "pwgd.message.send"
                },

            "fail":
                {
                    "queue": "pwgd.render.fail"
                }
		}
	).encode())

