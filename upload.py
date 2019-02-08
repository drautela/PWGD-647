import os
import requests

productionOutput = True
# aftr.pwgd.assets/email/campaigns/alerttest/
#actual path
# contentServiceStoragePath = 'aftr.pwgd.assets/email/campaigns/verifications/'
#testpath
# contentServiceStoragePath = 'aftr.email.assets/email/campaigns/marketing/'

contentServiceStoragePath = 'aftr.pwgd.assets/email/campaigns/verifications/html/'

contentServiceOpts = {
    'url': 'http://209.123.95.132/content/api/Resources/upload',
    'method': 'PUT',
    'headers': {
        #'Content-Type': 'multipart/form-data', #Take this out
        'X-AfterInc-Resource-ID': '',
        'X-AfterInc-Resource-Type': 'application/x-afterinc-content',
    },
    'formData': {
        'file': {
            'value': None,  # fs.createReadStream(content file to upload)
            'options': {
                'name': ''
            }
        }
    }
}


def upload_content(opts):
    response = requests.request(method=opts["method"],
                                url=opts["url"],
                                headers=opts["headers"],
                                files=[('file', ('test.txt', opts["formData"]["file"]["value"], 'text/plain'))],
							#	proxies={'http':'http://localhost:8888'} #Bounce request of Charles proxy to see how final http looks after python-requests forms it
								)

    if response.status_code != 200:
        print('failed to upload. response code: {}'.format(response.status_code))


def load_templates():
    __load_content('html')


def load_images():
    __load_content('')


def __load_content(content):
    files_list = os.listdir(os.path.join('C:/fulcrum/EMAIL/POWER GUARD/PWGD-647/Changed_Html', ''))
    print(files_list)
    print(os.path.join('C:/fulcrum/EMAIL/POWER GUARD/PWGD-647/Changed_Html/', ''))
    for each_file_name in files_list:
        local_contentServiceOpts = contentServiceOpts.copy()
        print('Next image is: {}'.format(each_file_name))

        resourceIdFullPath = contentServiceStoragePath + content + '' + each_file_name
        local_contentServiceOpts['headers']['X-AfterInc-Resource-ID'] = resourceIdFullPath

        #with open(os.path.join('.', 'template', content, each_file_name), 'rb') as file:
        #    local_contentServiceOpts['formData']['file']['value'] = file.read()
        local_contentServiceOpts['formData']['file']['value'] = open(os.path.join('C:/fulcrum/EMAIL/POWER GUARD/PWGD-647/', 'Changed_Html', each_file_name), 'rb')
        print(local_contentServiceOpts)
        print("Posting to full path: " + resourceIdFullPath)

        upload_content(local_contentServiceOpts)


#load_templates()
load_images()